import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestMaxLineLength(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")

    def test_valid_line_length(self):
        bslint.load_config_file(default_filepath='test-config.json')
        file_name = self.filepath_prefix + "short-line-length.txt"
        file = open(file_name, "r+").read()
        exp_result = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_exceed_max_line_length(self):
        bslint.load_config_file(user_filepath="line_length/small-max-line-length-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "short-line-length.txt"
        file = open(file_name, "r+").read()
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_equal_max_line_length(self):
        bslint.load_config_file(user_filepath="line_length/small-max-line-length-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "equal-max-line-length.txt"
        file = open(file_name, "r+").read()
        exp_result = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_multi_line_errors(self):
        bslint.load_config_file(user_filepath="line_length/small-max-line-length-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "multiline-assignment.txt"
        file = open(file_name, "r+").read()
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1]),
                      error.get_message(err_const.LINE_LENGTH, [11, 2])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)
