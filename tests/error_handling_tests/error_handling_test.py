import unittest
import re
import os
from io import StringIO
from argparse import Namespace
import bslint
import bslint.constants as const
from bslint.messages import print_constants as print_const
from bslint.messages import handler as msg_handler
from bslint.interface_handler import InterfaceHandler
import bslint.messages.error_constants as err_const
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import LEXING_TEST_FILES_PATH
from filepaths import TESTS_RESOURCES_PATH


class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.interface_handler = InterfaceHandler()

    def test_no_warnings_in_file_with_errors(self):
        skeleton_main_with_errors_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main-with-errors.brs')
        self.interface_handler.args = Namespace(lex=True)
        self.interface_handler.lint_file(skeleton_main_with_errors_path)
        self.assertEqual(len(self.interface_handler.messages[const.ERRORS]), 1)
        self.assertEqual(len(self.interface_handler.messages[const.WARNINGS]), 0)

    def test_all_linted_correctly(self):
        out = StringIO()
        brs_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'basic-string-assignment.brs')
        result = bslint.bslint.runner(to_lex=brs_file_path, out=out).printed_output
        self.assertEqual(result,
                         msg_handler.get_print_msg(print_const.NO_MANIFEST) +
                         msg_handler.get_print_msg(print_const.NO_BSLINTRC) +
                         msg_handler.get_print_msg(print_const.LINTING_COMPLETE) +
                         msg_handler.get_print_msg(print_const.ALL_LINTED_CORRECTLY))

    def test_only_warnings_in_file_without_errors(self):
        skeleton_main_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main.brs')
        self.interface_handler.args = Namespace(lex=True)
        self.interface_handler.lint_file(skeleton_main_path)
        self.assertEqual(len(self.interface_handler.messages[const.ERRORS]), 0)
        self.assertEqual(len(self.interface_handler.messages[const.WARNINGS]), 1)

    def test_parsing_directory(self):
        self.interface_handler.args = Namespace(lex=True)
        self.interface_handler.lint_all(LEXING_TEST_FILES_PATH)
        self.assertEqual(len(self.interface_handler.messages[const.WARNINGS]), 1)
        self.assertEqual(len(self.interface_handler.messages[const.ERRORS]), 1)

    def test_printed_message(self):
        out = StringIO()
        self.interface_handler = InterfaceHandler(out)
        error_handling_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files')
        self.interface_handler.args = Namespace(lex=True)
        self.interface_handler.lint_all(error_handling_file_path)
        result = out.getvalue()
        out.close()
        second_line = re.match(r".*\n(?P<second_line>.*)\n", result).group("second_line")
        self.assertEqual(second_line,
                         '\x1b[93mWARNING: Invalid indentation, you must indent with tabs. Line number: 1[0m')

    def test_error_handled_on_last_line_without_return(self):
        error_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files/error-file.brs')
        chars = open(error_file_path, "r+").read()
        result = Lexer().lex(chars)
        exp_result = [msg_handler.get_error_msg(err_const.UNMATCHED_QUOTATION_MARK, ['"error file', 1])]
        self.assertEqual(exp_result, result["Tokens"])
