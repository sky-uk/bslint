import os
import unittest

import bslint
import bslint.messages.handler as error
import bslint.messages.error_constants as err_const
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import COMMAS_IN_OBJECT_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestCommasInObject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        no_commas_in_object_config_path = os.path.join(COMMAS_IN_OBJECT_PATH, 'commas-in-object-config.json')
        bslint.load_config_file(user_filepath=no_commas_in_object_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        cls.common = Common()

    def test_single_key_no_trailing_comma(self):
        input_str = "testObj = { a:1 }"
        exp_result = []
        self.common.lex_string(exp_result, input_str)

    def test_multiple_keys_commas_valid(self):
        input_str = "testObj = { a:1, b:2, c:3 }"
        exp_result = []
        self.common.lex_string(exp_result, input_str)

    def test_single_key_with_trailing_comma(self):
        input_str = "testObj = { a:1, }"
        exp_result = [error.get_error_msg(err_const.TRAILING_COMMA_IN_OBJECTS, [1])]
        self.common.lex_string(exp_result, input_str)

    def test_multiple_keys_with_trailing_comma(self):
        input_str = "testObj = { a:1, b:2, c:3, }"
        exp_result = [error.get_error_msg(err_const.TRAILING_COMMA_IN_OBJECTS, [1])]
        self.common.lex_string(exp_result, input_str)

    def test_multiple_keys_invalid(self):
        input_str = "testObj = { a:1, b:2\n c:3 }"
        exp_result = [error.get_error_msg(err_const.COMMAS_IN_OBJECTS, [1])]
        self.common.lex_string(exp_result, input_str)
