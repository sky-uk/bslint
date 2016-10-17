import unittest
import os
import re
from bslint.interface_handler import InterfaceHandler as InterfaceHandler
from io import StringIO
import bslint.error_messages.handler as err
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestConfigFileLoading(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../../bslint/config/")
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/")

    def setUp(self):
        self.InterfaceHandler = InterfaceHandler()

    def testNoWarningsInFileWithErrors(self):
        self.InterfaceHandler.lint_specific(
            self.tests_filepath_prefix + "lexing_test_files/skeleton-main-with-errors.brs")
        self.assertEqual(len(self.InterfaceHandler.messages["Errors"]), 1)
        self.assertEqual(len(self.InterfaceHandler.messages["Warnings"]), 0)

    def testOnlyWarningsInFileWithoutErrors(self):
        file_name = self.tests_filepath_prefix + "lexing_test_files/skeleton-main.brs"
        self.InterfaceHandler.lint_specific(file_name)
        self.assertEqual(len(self.InterfaceHandler.messages["Warnings"]), 1)
        self.assertEqual(len(self.InterfaceHandler.messages["Errors"]), 0)

    def testParsingDirectory(self):
        directory = self.tests_filepath_prefix + "lexing_test_files"
        self.InterfaceHandler.lint_all(directory)
        self.assertEqual(len(self.InterfaceHandler.messages["Warnings"]), 1)
        self.assertEqual(len(self.InterfaceHandler.messages["Errors"]), 1)

    def testPrintedMessage(self):
        out = StringIO()
        self.InterfaceHandler = InterfaceHandler(out)
        directory = self.tests_filepath_prefix + "error_handling_files"
        self.InterfaceHandler.lint_all(directory)
        result = out.getvalue()
        out.close()
        second_line = re.match(r".*\n(?P<second_line>.*)\n", result).group("second_line")
        self.assertEqual(second_line, '\x1b[93mWARNING: Invalid indentation, you must indent with tabs. Line number: 1[0m')

    def testErrorHandledOnLastLineWithoutReturn(self):
        file_name = self.tests_filepath_prefix + "error_handling_files/error_file.brs"
        chars = open(file_name, "r+").read()
        result = Lexer().lex(chars)
        exp_result = [err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"error fi', 1])]
        self.assertEqual(exp_result, result["Tokens"])
