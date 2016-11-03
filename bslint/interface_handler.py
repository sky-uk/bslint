# pylint: disable=too-many-instance-attributes
import os
import re
import sys

import bslint
import bslint.constants as const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer


class InterfaceHandler:
    def __init__(self, out=sys.stdout):
        self.is_lexed_correctly = True
        self.files = []
        self.messages = {"Errors": {}, "Warnings": {}}
        self.bslintrc = {"ignore": []}
        self.out = out
        self.manifest_path = ""
        self.warnings_total = 0
        self.errors_total = 0

    def main(self):
        print(const.TITLE_COLOUR + "BSLint: A linter for BrightScript. %s. \n" %
              InterfaceHandler.get_version() + const.END_COLOUR)

        if self.is_specific_path():
            filename = sys.argv[1]
            if not os.path.exists(filename):
                self.is_lexed_correctly = False
                self.out.write(
                    const.ERROR_COLOUR + "The path you have provided does not exist." + const.END_COLOUR + "\n")
                return

        self.manifest_path = self._get_manifest_path()
        self.bslintrc = self._parse_bslintrc(self.manifest_path)

        if self.bslintrc is None:
            return

        self.out.write("\n")

        if self.is_specific_path():
            if os.path.isfile(filename):
                self.lint_file(filename)
            else:
                self.lint_all(filename)
        else:
            pathname = os.getcwd()
            self.lint_all(pathname)
        self.out.write(
            const.FILE_COLOUR + "LINTING COMPLETE" + const.END_COLOUR + "\n")
        if self.is_lexed_correctly:
            print(const.PASS_COLOUR + 'All linted correctly' + const.END_COLOUR)
            print("\n")
        else:
            self.out.write(const.TOTAL_COLOUR + "TOTAL WARNINGS: " + str(self.warnings_total) + const.END_COLOUR + "\n")
            self.out.write(const.TOTAL_COLOUR + "TOTAL ERRORS: " + str(self.errors_total) + const.END_COLOUR + "\n")

    def _get_manifest_path(self):
        try:
            if self.is_specific_path():
                if os.path.isfile(sys.argv[1]):
                    upper_dir = os.path.dirname(sys.argv[1])
                else:
                    upper_dir = sys.argv[1]
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
            print(const.ERROR_COLOUR + "No manifest file found" + const.END_COLOUR)
            return ""

    def lint_all(self, directory):
        for dir_name, subdirList, files in os.walk(directory):  # pylint: disable=C0103, W0612
            relative_path = self.get_relative_path(dir_name)
            if "ignore" in self.bslintrc and not self.ignore_dir(relative_path, self.bslintrc["ignore"]):
                self.lint_directory(dir_name, files)
        self.print_errors()

    def lint_directory(self, dir_name, files):
        for file in files:
            if file.endswith(".brs") or file.endswith(".bs"):
                filepath = os.path.join(dir_name, file)
                self.lint_file(filepath)

    def lint_file(self, filepath):
        filename = filepath.replace(os.getcwd() + '/', '')
        if filename.endswith(".brs") or filename.endswith(".bs"):
            self.files.append(filename)
            read_file = self.file_reader(filename)
            lex_result = Lexer().lex(read_file['str_to_lex'])
            if lex_result["Status"] == "Error":
                self.handle_lexing_error(filepath, lex_result)
            elif lex_result["Warnings"]:
                self.handle_lexing_warnings(filepath, lex_result)
        else:
            self.is_lexed_correctly = False
        self.print_warnings(filepath)

    def handle_lexing_warnings(self, filepath, lex_result):
        self.is_lexed_correctly = False
        self.messages["Warnings"][filepath] = []
        for warning in lex_result["Warnings"]:
            self.messages["Warnings"][filepath].append(
                const.WARNING_COLOUR + str(warning) + const.END_COLOUR)

    def handle_lexing_error(self, filepath, lex_result):
        self.is_lexed_correctly = False
        self.messages["Errors"][filepath] = []
        for error in lex_result["Tokens"]:
            self.messages["Errors"][filepath].append(
                const.ERROR_COLOUR + str(error) + const.END_COLOUR)

    def print_warnings(self, file_name):
        if file_name in self.messages["Warnings"]:
            self.out.write(const.FILE_COLOUR + file_name + const.END_COLOUR + "\n")
            for message in self.messages["Warnings"][file_name]:
                self.out.write(message + "\n")
            number_warnings = len(self.messages["Warnings"][file_name])
            self.warnings_total += number_warnings
            self.out.write(const.TOTAL_COLOUR + "WARNINGS IN FILE: " + str(number_warnings) + const.END_COLOUR + "\n")
            self.out.write("\n")

    def print_errors(self):
        for file_name in self.messages["Errors"]:
            self.out.write(const.FILE_COLOUR + file_name + const.END_COLOUR + "\n")
            for message in self.messages["Errors"][file_name]:
                self.out.write(message + "\n")
            number_errors = len(self.messages["Errors"][file_name])
            self.errors_total += number_errors
            self.out.write(const.TOTAL_COLOUR + "ERRORS IN FILE: " + str(number_errors) + const.END_COLOUR + "\n")
            self.out.write("\n")

    def ignore_dir(self, relative_directory_path, directories_to_ignore):
        for directory in directories_to_ignore:
            directory = self.add_slashes_to_dir(directory)
            relative_directory_path = self.add_slashes_to_dir(relative_directory_path)

            if relative_directory_path.startswith(directory):
                return True
        return False

    @staticmethod
    def _parse_bslintrc(manifest_path):
        bslintrc_path = os.path.join(manifest_path, ".bslintrc")
        return bslint.config_loader.load_config_file(bslintrc_path)

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
        file = open(file_to_lex, "r+")
        str_to_lex = file.read()
        return {"invalid_encoding": commands.check_file_encoding(file_to_lex),
                "str_to_lex": str_to_lex}

    @staticmethod
    def get_version():
        this_dir = os.path.dirname(__file__)
        return re.search(
            r'^__version__\s*=\s*"(.*)"',
            open(os.path.join(this_dir, 'bslint.py')).read(),
            re.M
        ).group(1)

    @staticmethod
    def is_specific_path():
        return len(sys.argv) != 1

    @staticmethod
    def no_manifest_in_folder(upper_dir):
        return not os.path.exists(os.path.join(upper_dir, "MANIFEST")) and not os.path.exists(
            os.path.join(upper_dir, "manifest"))
