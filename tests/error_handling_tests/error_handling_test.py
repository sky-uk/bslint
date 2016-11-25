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
        self.assertEqual(1, len(self.interface_handler.messages[const.ERRORS]))
        self.assertEqual(0, len(self.interface_handler.messages[const.WARNINGS]))

    def test_all_lexed_correctly(self):
        out = StringIO()
        brs_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'basic-string-assignment.brs')
        result = bslint.bslint.runner(to_lex=brs_file_path, out=out).printed_output
        self.assertEqual(msg_handler.get_print_msg(print_const.NO_MANIFEST) +
                         msg_handler.get_print_msg(print_const.NO_BSLINTRC) +
                         msg_handler.get_print_msg(print_const.LINTING_COMPLETE) +
                         msg_handler.get_print_msg(print_const.ALL_LINTED_CORRECTLY), result)

    def test_all_parsed_correctly(self):
        out = StringIO()
        brs_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'basic-string-assignment.brs')
        result = bslint.bslint.runner(to_lex=brs_file_path, out=out, only_lex=False).printed_output
        self.assertEqual(msg_handler.get_print_msg(print_const.NO_MANIFEST) +
                         msg_handler.get_print_msg(print_const.NO_BSLINTRC) +
                         msg_handler.get_print_msg(print_const.LINTING_COMPLETE) +
                         msg_handler.get_print_msg(print_const.ALL_LINTED_CORRECTLY), result)

    def test_only_warnings_in_file_without_errors(self):
        skeleton_main_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main.brs')
        self.interface_handler.args = Namespace(lex=True)
        self.interface_handler.lint_file(skeleton_main_path)
        self.assertEqual(0, len(self.interface_handler.messages[const.ERRORS]))
        self.assertEqual(1, len(self.interface_handler.messages[const.WARNINGS]))

    def test_parsing_directory(self):
        self.interface_handler.args = Namespace(lex=True)
        self.interface_handler.lint_all(LEXING_TEST_FILES_PATH)
        self.assertEqual(1, len(self.interface_handler.messages[const.WARNINGS]))
        self.assertEqual(1, len(self.interface_handler.messages[const.ERRORS]))

    def test_warning_message_printed(self):
        out = StringIO()
        warning_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files/warning-file.brs')
        result = bslint.bslint.runner(to_lex=warning_file_path, out=out).printed_output
        self.assertEqual(msg_handler.get_print_msg(print_const.NO_MANIFEST) +
                         msg_handler.get_print_msg(print_const.NO_BSLINTRC) +
                         msg_handler.get_print_msg(print_const.FILE_NAME, ["file://" + warning_file_path]) +
                         msg_handler.get_print_msg(const.WARNINGS,
                                                   [msg_handler.get_error_msg(err_const.TAB_AND_SPACES, [1])]) +
                         msg_handler.get_print_msg(const.WARNINGS,
                                                   [msg_handler.get_error_msg(err_const.TAB_AND_SPACES, [2])]) +
                         msg_handler.get_print_msg(print_const.WARNINGS_IN_FILE, [2]) +
                         msg_handler.get_print_msg(print_const.LINTING_COMPLETE) +
                         msg_handler.get_print_msg(print_const.TOTAL_WARNINGS, [2]) +
                         msg_handler.get_print_msg(print_const.TOTAL_ERRORS, [0]), result)

    def test_error_message_printed(self):
        out = StringIO()
        error_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files/error-file.brs')
        result = bslint.bslint.runner(to_lex=error_file_path, out=out).printed_output
        print(result)
        self.assertEqual(msg_handler.get_print_msg(print_const.NO_MANIFEST) +
                         msg_handler.get_print_msg(print_const.NO_BSLINTRC) +
                         msg_handler.get_print_msg(print_const.FILE_NAME, ["file://" + error_file_path]) +
                         msg_handler.get_print_msg(const.ERRORS,
                                                   [msg_handler.get_error_msg(err_const.UNMATCHED_QUOTATION_MARK,
                                                                              ['"error file', 1])]) +
                         msg_handler.get_print_msg(print_const.LINTING_COMPLETE) +
                         msg_handler.get_print_msg(print_const.TOTAL_WARNINGS, [0]) +
                         msg_handler.get_print_msg(print_const.TOTAL_ERRORS, [1]), result)

    def test_error_handled_on_last_line_without_return(self):
        error_file_path = os.path.join(TESTS_RESOURCES_PATH, 'error_handling_files/error-file.brs')
        chars = open(error_file_path, "r+").read()
        result = Lexer().lex(chars)
        expected = [msg_handler.get_error_msg(err_const.UNMATCHED_QUOTATION_MARK, ['"error file', 1])]
        self.assertEqual(expected, result["Tokens"])
