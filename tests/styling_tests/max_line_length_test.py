import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import STYLING_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestMaxLineLength(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.small_max_line_length_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                             'line_length/small-max-line-length-config.json')
        cls.short_line_length_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'short-line-length.txt')
        cls.common = Common()

    def test_valid_line_length(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        file_name = self.short_line_length_file_path
        self.common.lex_file(file_name, [])

    def test_exceed_max_line_length(self):
        bslint.load_config_file(user_filepath=self.small_max_line_length_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        file_name = self.short_line_length_file_path
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1])]
        self.common.lex_file(file_name, exp_result)

    def test_equal_max_line_length(self):
        bslint.load_config_file(user_filepath=self.small_max_line_length_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        equal_max_line_length_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'equal-max-line-length.txt')
        file_name = equal_max_line_length_file_path
        self.common.lex_file(file_name, [])

    def test_multi_line_errors(self):
        bslint.load_config_file(user_filepath=self.small_max_line_length_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        multi_line_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'multiline-assignment.txt')
        file_name = multi_line_file_path
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1]),
                      error.get_message(err_const.LINE_LENGTH, [11, 2])]
        self.common.lex_file(file_name, exp_result)
