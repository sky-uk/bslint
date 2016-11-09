import unittest
import re
import os
from io import StringIO

import bslint
import bslint.constants as const
from bslint.interface_handler import InterfaceHandler as InterfaceHandler
import bslint.error_messages.handler as err
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import LEXING_TEST_FILES_PATH
from filepaths import TESTS_RESOURCES_PATH


class TestErrorHandling(unittest.TestCase):
    ERRORS = "Errors"
    WARNINGS = "Warnings"

    def setUp(self):
        self.InterfaceHandler = InterfaceHandler()

    def test_no_warnings_in_file_with_errors(self):
        skeleton_main_with_errors_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main-with-errors.brs')
        self.InterfaceHandler.lint_file(skeleton_main_with_errors_path)
        self.assertEqual(len(self.InterfaceHandler.messages[self.ERRORS]), 1)
        self.assertEqual(len(self.InterfaceHandler.messages[self.WARNINGS]), 0)

    def test_all_linted_correctly(self):
        out = StringIO()
        os.chdir(LEXING_TEST_FILES_PATH)
        brs_file_path = 'basic-string-assignment.brs'
        bslint.bslint.runner(to_lex=brs_file_path, out=out)
        result = out.getvalue()
        out.close()
        self.assertEqual(result,
                         const.ERROR_COLOUR + "No manifest file found" + const.END_COLOUR + "\n" +
                         const.ERROR_COLOUR + "Cannot find bslintrc, using default config." + const.END_COLOUR +
                         "\n" + "\n" +
                         const.FILE_COLOUR + "LINTING COMPLETE" + const.END_COLOUR + "\n" +
                         const.PASS_COLOUR + 'All linted correctly' + const.END_COLOUR + "\n")

    def test_only_warnings_in_file_without_errors(self):
        skeleton_main_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main.brs')
        self.InterfaceHandler.lint_file(skeleton_main_path)
        self.assertEqual(len(self.InterfaceHandler.messages[self.WARNINGS]), 1)
        self.assertEqual(len(self.InterfaceHandler.messages[self.ERRORS]), 0)

    def test_parsing_directory(self):
        self.InterfaceHandler.lint_all(LEXING_TEST_FILES_PATH)
        self.assertEqual(len(self.InterfaceHandler.messages[self.WARNINGS]), 1)
        self.assertEqual(len(self.InterfaceHandler.messages[self.ERRORS]), 1)

    def test_printed_message(self):
        out = StringIO()
        self.InterfaceHandler = InterfaceHandler(out)
        error_handling_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files')
        self.InterfaceHandler.lint_all(error_handling_file_path)
        result = out.getvalue()
        out.close()
        second_line = re.match(r".*\n(?P<second_line>.*)\n", result).group("second_line")
        self.assertEqual(second_line,
                         '\x1b[93mWARNING: Invalid indentation, you must indent with tabs. Line number: 1[0m')

    def test_error_handled_on_last_line_without_return(self):
        error_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files/error-file.brs')
        chars = open(error_file_path, "r+").read()
        result = Lexer().lex(chars)
        exp_result = [err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"error file', 1])]
        self.assertEqual(exp_result, result["Tokens"])
