import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import STYLING_TEST_FILES_PATH


class TestMaxLineLength(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.small_max_line_length_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                             'line_length/small-max-line-length-config.json')
        cls.short_line_length_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'short-line-length.txt')

    def test_valid_line_length(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        file_name = self.short_line_length_file_path
        file = open(file_name, "r+").read()
        exp_result = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_exceed_max_line_length(self):
        bslint.load_config_file(user_filepath=self.small_max_line_length_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        file_name = self.short_line_length_file_path
        file = open(file_name, "r+").read()
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_equal_max_line_length(self):
        bslint.load_config_file(user_filepath=self.small_max_line_length_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        equal_max_line_length_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'equal-max-line-length.txt')
        file_name = equal_max_line_length_file_path
        file = open(file_name, "r+").read()
        exp_result = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_multi_line_errors(self):
        bslint.load_config_file(user_filepath=self.small_max_line_length_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        multi_line_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'multiline-assignment.txt')
        file_name = multi_line_file_path
        file = open(file_name, "r+").read()
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1]),
                      error.get_message(err_const.LINE_LENGTH, [11, 2])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)
