# pylint: disable=too-many-instance-attributes, no-member
import argparse
import os
import re
import sys
from io import StringIO
from multiprocessing import Process, Lock

import bslint
import bslint.constants as const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer
from bslint.parser.parser import Parser as Parser
from bslint.utilities.spinner import SpinnerProcess as SpinnerProcess
from bslint.messages import handler as msg_handler
from bslint.messages import print_constants as print_const

PROCESS_LOCK = Lock()


class InterfaceHandler(Process):
    def __init__(self, out=sys.stdout, conn=None):
        Process.__init__(self)
        self.is_lexed_correctly = True
        self.files = []
        self.messages = {const.ERRORS: {}, const.WARNINGS: {}}
        self.bslintrc = {const.IGNORE: []}
        self.out = out
        self.manifest_path = ""
        self.issues_total = {const.WARNINGS: 0, const.ERRORS: 0}
        self.conn = conn
        self.printed_output = None
        self.config = None
        self.args = None

    def run(self):
        self._get_cli_arguments()
        if self.args.path and not os.path.exists(self.args.path):
            self.is_lexed_correctly = False
            self.out.write(msg_handler.get_print_msg(print_const.PATH_DOSNT_EXIST))
            self.send_to_pipe()
            return

        self.manifest_path = self._get_manifest_path(self.args.path)
        self.bslintrc = self._parse_bslintrc(self.manifest_path, self.out)

        self.start_spinner()
        self.lint()
        self.print_summary()
        self.send_to_pipe()

    def lint(self):
        if self.args.path:
            if os.path.isfile(self.args.path):
                self.lint_file(self.args.path)
            else:
                self.lint_all(self.args.path)
        else:
            pathname = os.getcwd()
            self.lint_all(pathname)

    def print_summary(self):
        PROCESS_LOCK.acquire()
        self.out.write(msg_handler.get_print_msg(print_const.LINTING_COMPLETE))
        if self.is_lexed_correctly:
            self.out.write(msg_handler.get_print_msg(print_const.ALL_LINTED_CORRECTLY))
        else:
            self.out.write(msg_handler.get_print_msg(print_const.TOTAL_WARNINGS, [self.issues_total[const.WARNINGS]]))
            self.out.write(msg_handler.get_print_msg(print_const.TOTAL_ERRORS, [self.issues_total[const.ERRORS]]))
        PROCESS_LOCK.release()

    def send_to_pipe(self):
        if self.conn:
            if isinstance(self.out, StringIO):
                self.printed_output = self.out.getvalue()
            self.out.close()
            self.config = bslint.config_loader.CONFIG
            testing_dict = {"files": self.files, "messages": self.messages,
                            "printed_output": self.printed_output, "config": self.config}
            self.conn.send(testing_dict)
            self.conn.close()

    def _get_manifest_path(self, specific_part):
        if specific_part:
            if os.path.isfile(specific_part):
                upper_dir = os.path.dirname(specific_part)
            else:
                upper_dir = specific_part
        else:
            upper_dir = ""
        count = 0
        while self.no_manifest_in_folder(upper_dir) and count < const.ALLOWED_SUB_DIR_NUM:
            upper_dir = os.path.join(upper_dir, "../")
            count += 1
        if count == const.ALLOWED_SUB_DIR_NUM:
            self.out.write(msg_handler.get_print_msg(print_const.NO_MANIFEST))
            upper_dir = ""
        return upper_dir

    def lint_all(self, directory):
        for dir_name, _, files in os.walk(directory):  # pylint: disable=C0103
            relative_path = self.get_relative_path(dir_name)
            if not self.ignore_dir(relative_path, self.bslintrc[const.IGNORE]):
                self.lint_directory(dir_name, files)
        for file_name in self.messages[const.ERRORS]:
            self.print_issues(file_name, const.ERRORS)

    def lint_directory(self, dir_name, files):
        for file in files:
            filepath = os.path.join(dir_name, file)
            self.lint_file(filepath)

    def lint_file(self, filepath):
        filename = filepath.replace(os.getcwd() + '/', '')
        if filename.endswith(".brs") or filename.endswith(".bs"):
            self.files.append(filename)
            file_content = self.file_reader(filename)['file_content']
            if self.args.lex:
                lex_result = Lexer().lex(file_content)
            else:
                lex_result = Parser().parse(file_content)
            if lex_result[const.STATUS] == const.ERROR:
                self.handle_lexing_result(filepath, const.ERRORS, lex_result[const.TOKENS])
            elif lex_result[const.WARNINGS]:
                self.handle_lexing_result(filepath, const.WARNINGS, lex_result[const.WARNINGS])
        self.print_issues(filepath, const.WARNINGS)

    def handle_lexing_result(self, filepath, error_type, messages):
        self.is_lexed_correctly = False
        self.messages[error_type][filepath] = []
        for msg in messages:
            self.messages[error_type][filepath].append(msg_handler.get_print_msg(error_type, [msg]))

    def print_issues(self, file_name, issue_type):
        if file_name in self.messages[issue_type]:
            PROCESS_LOCK.acquire()
            self.out.write(msg_handler.get_print_msg(print_const.FILE_NAME, [file_name]))
            for message in self.messages[issue_type][file_name]:
                self.out.write(message)
            number_issues = len(self.messages[issue_type][file_name])
            self.issues_total[issue_type] += number_issues
            self.out.write(msg_handler.get_print_msg(issue_type + print_const.IN_FILE, [number_issues]))
            PROCESS_LOCK.release()

    def ignore_dir(self, relative_directory_path, directories_to_ignore):
        for directory in directories_to_ignore:
            directory = self.add_slashes_to_dir(directory)
            relative_directory_path = self.add_slashes_to_dir(relative_directory_path)

            if relative_directory_path.startswith(directory):
                return True
        return False

    def _get_cli_arguments(self):
        parser = argparse.ArgumentParser(description=msg_handler.get_print_msg(print_const.DESCRIPTION))
        parser.add_argument("--path", "-p", help="Specify directory or file")
        parser.add_argument('--lex', "-l", help="Runs only the lexer, without parsing the code",
                            action='store_true', default=False)
        parser.add_argument('--version', "-v", action='version', version=self.get_version(), help="Get current version")
        self.args = parser.parse_args()

    @staticmethod
    def _parse_bslintrc(manifest_path, out):
        bslintrc_path = os.path.join(manifest_path, ".bslintrc")
        return bslint.config_loader.load_config_file(bslintrc_path, out=out)

    def get_relative_path(self, dir_name):
        directory = os.path.abspath(self.manifest_path)
        return dir_name.replace(directory, '')

    @staticmethod
    def add_slashes_to_dir(directory):
        if not directory.startswith("/"):
            directory = "/" + directory
        if not directory.endswith("/"):
            directory += "/"
        return directory

    @staticmethod
    def file_reader(file_to_lex):
        with open(file_to_lex, "r+") as file:
            str_to_lex = file.read()
        return {"invalid_encoding": commands.check_file_encoding(file_to_lex), "file_content": str_to_lex}

    @staticmethod
    def get_version():
        this_dir = os.path.dirname(__file__)
        return re.search(r'^__version__\s*=\s*"(.*)"', open(os.path.join(this_dir, 'bslint.py')).read(), re.M).group(1)

    @staticmethod
    def no_manifest_in_folder(upper_dir):
        return not os.path.exists(os.path.join(upper_dir, "MANIFEST")) and not os.path.exists(
            os.path.join(upper_dir, "manifest"))

    @staticmethod
    def start_spinner():
        spinner_process = SpinnerProcess(PROCESS_LOCK)
        spinner_process.daemon = True
        spinner_process.start()
