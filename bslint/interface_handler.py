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

    def main(self):
        print(const.TITLE_COLOUR + "BSLint: A linter for BrightScript. %s. \n" % InterfaceHandler.get_version() + const.END_COLOUR)
        manifest_path = self._get_manifest_path()
        self.bslintrc = self._parse_bslintrc(manifest_path)

        if self.bslintrc is None:
            return

        if self.is_specific_path():
            filename = sys.argv[1]
            if not os.path.exists(filename):
                self.is_lexed_correctly = False
            else:
                if os.path.isfile(filename):
                    self.lint_specific(filename)
                else:
                    self.lint_all(filename)
        else:
            pathname = os.getcwd()
            self.lint_all(pathname)
        if self.is_lexed_correctly:
            print(const.PASS_COLOUR + 'All lexed correctly' + const.END_COLOUR)
            print("\n")

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
        for dir_name, subdirList, files in os.walk(directory):
            relative_path = self.get_relative_path(dir_name)
            if not self.ignore_dir(relative_path, self.bslintrc["ignore"]):
                self.lint_directory(dir_name, files)
        self.print_errors()

    def lint_directory(self, dir_name, files):
        for file in files:
            if file.endswith(".brs") or file.endswith(".bs"):
                filepath = os.path.join(dir_name, file)
                self.lint_specific(filepath)
                self.print_warnings(filepath)

    def lint_specific(self, filepath):
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

    def handle_lexing_warnings(self, filepath, lex_result):
        self.is_lexed_correctly = False
        self.messages["Warnings"][filepath] = []
        for warning in lex_result["Warnings"]:
            self.messages["Warnings"][filepath].append(const.WARNING_COLOUR + str(warning) + const.END_COLOUR)

    def handle_lexing_error(self, filepath, lex_result):
        self.is_lexed_correctly = False
        self.messages["Errors"][filepath] = []
        for error in lex_result["Tokens"]:
            self.messages["Errors"][filepath].append(const.ERROR_COLOUR + str(error) + const.END_COLOUR)

    def print_warnings(self, file_name):
        if file_name in self.messages["Warnings"]:
            self.out.write(const.FILE_COLOUR + file_name + const.END_COLOUR + "\n")
            for message in self.messages["Warnings"][file_name]:
                self.out.write(message + "\n")
            self.out.write("\n")

    def print_errors(self):
        for file_name in self.messages["Errors"]:
            self.out.write(const.FILE_COLOUR + file_name + const.END_COLOUR + "\n")
            for message in self.messages["Errors"][file_name]:
                self.out.write(message + "\n")
        self.out.write("\n")

    def ignore_dir(self, relative_directory_path, directories_to_ignore):
        for directory in directories_to_ignore:
            directory = self.add_slashes_to_dir(directory)
            relative_directory_path = self.add_slashes_to_dir(relative_directory_path)

            if relative_directory_path.startswith(directory):
                return True
        return False


    def _parse_bslintrc(self, manifest_path):
        try:
            bslintrc_path = os.path.join(manifest_path, ".bslintrc")
            bslint.config_loader.load_config_file(bslintrc_path)
            return bslint.config_loader.read_json(bslintrc_path)
        except ValueError:
            self.out.write(const.ERROR_COLOUR + "Unable to parse JSON in .bslintrc file" + const.END_COLOUR)
            return None
        except FileNotFoundError:
            print(const.ERROR_COLOUR + "No .bslintrc file found" + const.END_COLOUR)
            return {"ignore": ""}

    def get_relative_path(self, dir_name):
        directory = os.path.abspath(self._get_manifest_path())
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
        fo = open(file_to_lex, "r+")
        str_to_lex = fo.read()
        return {"invalid_encoding": commands.check_file_encoding(file_to_lex), "str_to_lex": str_to_lex}

    @staticmethod
    def get_version():
        this_dir = os.path.dirname(__file__)
        return re.search(
            '^__version__\s*=\s*"(.*)"',
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






