import os
import unittest

import bslint
import bslint.messages.handler as error
import bslint.messages.error_constants as err_const
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import LEXING_TEST_FILES_PATH
from filepaths import TRAILING_WHITE_SPACE_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestTrailingWhiteSpace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        trailing_white_space_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                        'trailing_white_space/trailing-white-space-config.json')
        bslint.load_config_file(user_filepath=trailing_white_space_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        cls.common = Common()

    def test_no_trailing_white_space(self):
        file_name = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main.brs')
        self.common.lex_file([], file_name)

    def test_trailing_white_space_first_line(self):
        file_name = os.path.join(TRAILING_WHITE_SPACE_TEST_FILES_PATH, 'trailing-white-space-first-line.brs')
        expected = [error.get_error_msg(err_const.TRAILING_WHITE_SPACE, [1])]
        self.common.lex_file(expected, file_name)

    def test_trailing_white_space_multi_lines(self):
        file_name = os.path.join(TRAILING_WHITE_SPACE_TEST_FILES_PATH, 'trailing-white-space-multi-lines.brs')
        expected = [error.get_error_msg(err_const.TRAILING_WHITE_SPACE, [2]),
                    error.get_error_msg(err_const.TRAILING_WHITE_SPACE, [3]),
                    error.get_error_msg(err_const.TRAILING_WHITE_SPACE, [7])]
        self.common.lex_file(expected, file_name)

    def test_trailing_white_space_last_line(self):
        file_name = os.path.join(TRAILING_WHITE_SPACE_TEST_FILES_PATH, 'trailing-white-space-last-line.brs')
        expected = [error.get_error_msg(err_const.TRAILING_WHITE_SPACE, [13])]
        self.common.lex_file(expected, file_name)
