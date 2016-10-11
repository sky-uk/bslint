import os
import unittest

import bslint
import bslint.error_messages_builder.error_message_handler as error
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/trace_test_files/")

    def testPRINT(self):
        bslint.load_config_file(user_filepath="trace_free/trace-free-config.json", default_filepath="test-config.json")
        file_name = self.tests_filepath_prefix + "print.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TRACEABLE_CODE, [3])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testQuestionMark(self):
        bslint.load_config_file(user_filepath="trace_free/trace-free-config.json", default_filepath="test-config.json")
        file_name = self.tests_filepath_prefix + "question-mark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TRACEABLE_CODE, [3])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testPrintAndQuestionMark(self):
        bslint.load_config_file(user_filepath="trace_free/trace-free-config.json", default_filepath="test-config.json")
        file_name = self.tests_filepath_prefix + "print-and-question-mark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TRACEABLE_CODE, [3]),
                   error.get_message(err_const.TRACEABLE_CODE, [4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoPrintNoQuestionMark(self):
        bslint.load_config_file(user_filepath="trace_free/trace-free-config.json", default_filepath="test-config.json")
        file_name = self.tests_filepath_prefix + "no-print-no-question-mark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testInactivePrintAndQuestionMark(self):
        bslint.load_config_file(default_filepath="test-config.json")
        file_name = self.tests_filepath_prefix + "print-and-question-mark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)