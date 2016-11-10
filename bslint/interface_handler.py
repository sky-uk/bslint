# pylint: disable=too-many-instance-attributes, no-member
import os
import re
import sys
from io import StringIO
from multiprocessing import Process, Lock
import argparse
import bslint
import bslint.constants as const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer
from bslint.utilities.spinner import SpinnerProcess as SpinnerProcess

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
        self.warnings_total = 0
        self.errors_total = 0
        self.conn = conn
        self.printed_output = None
        self.config = None

    def run(self):
        args = self._get_cli_arguments()
        if args.path:
            filename = args.path
            if not os.path.exists(filename):
                self.is_lexed_correctly = False
                self.out.write(
                    const.ERROR_COLOUR + "The path you have provided does not exist." + const.END_COLOUR + "\n")
                self.send_to_pipe()
                return

        self.manifest_path = self._get_manifest_path(args.path)
        self.bslintrc = self._parse_bslintrc(self.manifest_path, self.out)

        self.out.write("\n")

        self.start_spinner()
        if args.path:
            if os.path.isfile(filename):
                self.lint_file(filename)
            else:
                self.lint_all(filename)
        else:
            pathname = os.getcwd()
            self.lint_all(pathname)
        PROCESS_LOCK.acquire()
        self.out.write(const.FILE_COLOUR + "LINTING COMPLETE" + const.END_COLOUR + "\n")
        if self.is_lexed_correctly:
            self.out.write(const.PASS_COLOUR + "All linted correctly" + const.END_COLOUR + "\n")
        else:
            self.out.write(const.TOTAL_COLOUR + "TOTAL WARNINGS: " + str(self.warnings_total) + const.END_COLOUR + "\n")
            self.out.write(const.TOTAL_COLOUR + "TOTAL ERRORS: " + str(self.errors_total) + const.END_COLOUR + "\n")
        PROCESS_LOCK.release()
        self.send_to_pipe()

    @staticmethod
    def start_spinner():
        spinner_process = SpinnerProcess(PROCESS_LOCK)
        spinner_process.daemon = True
        spinner_process.start()

    def send_to_pipe(self):
        if self.conn:
            if isinstance(self.out, StringIO):
                self.printed_output = self.out.getvalue()
            self.out.close()
            self.config = bslint.config_loader.CONFIG
            testing_dict = {"files": self.files, "messages": self.messages, "printed_output": self.printed_output,
                            "config": self.config}
            self.conn.send(testing_dict)
            self.conn.close()

    def _get_manifest_path(self, specific_part):
        try:
            if specific_part:
                if os.path.isfile(specific_part):
                    upper_dir = os.path.dirname(specific_part)
                else:
                    upper_dir = specific_part
            else:
                upper_dir = ""
            count = 0
            while self.no_manifest_in_folder(upper_dir) and count < 5:
                upper_dir = os.path.join(upper_dir, "../")
                count += 1
            if count == 5:
                raise FileNotFoundError
            return upper_dir
        except FileNotFoundError:
            self.out.write(const.ERROR_COLOUR + "No manifest file found" + const.END_COLOUR + "\n")
            return ""

    def lint_all(self, directory):
        for dir_name, subdirList, files in os.walk(directory):  # pylint: disable=C0103, W0612
            relative_path = self.get_relative_path(dir_name)
            if const.IGNORE in self.bslintrc and not self.ignore_dir(relative_path, self.bslintrc[const.IGNORE]):
                self.lint_directory(dir_name, files)
        self.print_errors()

    def lint_directory(self, dir_name, files):
        for file in files:
            filepath = os.path.join(dir_name, file)
            self.lint_file(filepath)

    def lint_file(self, filepath):
        filename = filepath.replace(os.getcwd() + '/', '')
        if filename.endswith(".brs") or filename.endswith(".bs"):
            self.files.append(filename)
            read_file = self.file_reader(filename)
            lex_result = Lexer().lex(read_file['str_to_lex'])
            if lex_result[const.STATUS] == "Error":
                self.handle_lexing_error(filepath, lex_result)
            elif lex_result[const.WARNINGS]:
                self.handle_lexing_warnings(filepath, lex_result)
        else:
            self.is_lexed_correctly = False
        self.print_warnings(filepath)

    def handle_lexing_warnings(self, filepath, lex_result):
        self.is_lexed_correctly = False
        self.messages[const.WARNINGS][filepath] = []
        for warning in lex_result[const.WARNINGS]:
            self.messages[const.WARNINGS][filepath].append(
                const.WARNING_COLOUR + str(warning) + const.END_COLOUR)

    def handle_lexing_error(self, filepath, lex_result):
        self.is_lexed_correctly = False
        self.messages[const.ERRORS][filepath] = []
        for error in lex_result[const.TOKENS]:
            self.messages[const.ERRORS][filepath].append(
                const.ERROR_COLOUR + str(error) + const.END_COLOUR)

    def print_warnings(self, file_name):
        if file_name in self.messages[const.WARNINGS]:
            PROCESS_LOCK.acquire()
            self.out.write('\r' + const.FILE_COLOUR + file_name + const.END_COLOUR + "\n")
            for message in self.messages[const.WARNINGS][file_name]:
                self.out.write(message + "\n")
            number_warnings = len(self.messages[const.WARNINGS][file_name])
            self.warnings_total += number_warnings
            self.out.write(const.TOTAL_COLOUR + "WARNINGS IN FILE: " + str(number_warnings) + const.END_COLOUR + "\n\n")
            PROCESS_LOCK.release()

    def print_errors(self):
        for file_name in self.messages[const.ERRORS]:
            self.out.write(const.FILE_COLOUR + file_name + const.END_COLOUR + "\n")
            for message in self.messages[const.ERRORS][file_name]:
                self.out.write(message + "\n")
            number_errors = len(self.messages[const.ERRORS][file_name])
            self.errors_total += number_errors
            self.out.write(const.TOTAL_COLOUR + "ERRORS IN FILE: " + str(number_errors) + const.END_COLOUR + "\n\n")

    def ignore_dir(self, relative_directory_path, directories_to_ignore):
        for directory in directories_to_ignore:
            directory = self.add_slashes_to_dir(directory)
            relative_directory_path = self.add_slashes_to_dir(relative_directory_path)

            if relative_directory_path.startswith(directory):
                return True
        return False

    def _get_cli_arguments(self):
        parser = argparse.ArgumentParser(description=const.TITLE_COLOUR + "BSLint: A linter for BrightScript. %s. \n" %
                                         self.get_version() + const.END_COLOUR)
        parser.add_argument("--path", "-p", help="Specify directory or file")
        parser.add_argument('--version', "-v", action='version', version=self.get_version(), help="Get current version")
        return parser.parse_args()

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
        return {"invalid_encoding": commands.check_file_encoding(file_to_lex), "str_to_lex": str_to_lex}

    @staticmethod
    def get_version():
        this_dir = os.path.dirname(__file__)
        return re.search(r'^__version__\s*=\s*"(.*)"', open(os.path.join(this_dir, 'bslint.py')).read(), re.M).group(1)

    @staticmethod
    def no_manifest_in_folder(upper_dir):
        return not os.path.exists(os.path.join(upper_dir, "MANIFEST")) and not os.path.exists(
            os.path.join(upper_dir, "manifest"))
