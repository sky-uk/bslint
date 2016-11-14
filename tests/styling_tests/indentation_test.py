import unittest
import os

import bslint
from bslint import constants as const
import bslint.messages.handler as error
import bslint.messages.error_constants as err_const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import STYLING_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestIndentation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.indentation_config_path = os.path.join(TESTS_CONFIG_PATH, 'indentation/indentation-config.json')
        cls.common = Common()

    def test_no_indentation(self):
        bslint.load_config_file(user_filepath=self.indentation_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        expected = None
        current_indentation_level = 0
        characters = "var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(expected, result[0])

    def test_single_indentation(self):
        bslint.load_config_file(user_filepath=self.indentation_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        expected = None
        current_indentation_level = 1
        characters = "    var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(expected, result[0])

    def test_indentation_error(self):
        bslint.load_config_file(user_filepath=self.indentation_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        basic_indentation_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'basic-indentation.txt')
        file_name = basic_indentation_file_path
        file = open(file_name, "r+").read()
        expected = [error.get_error_msg(err_const.TAB_INDENTATION_ERROR, [4, 2])]
        result = Lexer().lex(file)
        self.assertEqual(expected, result[const.WARNINGS])

    def test_advanced_indentation_success(self):
        bslint.load_config_file(user_filepath=self.indentation_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        advanced_indentation_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'advanced-indentation.txt')
        file_name = advanced_indentation_file_path
        file = open(file_name, "r+").read()
        expected = []
        result = Lexer().lex(file)
        self.assertEqual(expected, result[const.WARNINGS])

    def test_indent_with_only_tabs_with_error(self):
        tab_only_indentation_config_path = os.path.join(TESTS_CONFIG_PATH, 'indentation/tab-only-indentation.json')
        bslint.load_config_file(user_filepath=tab_only_indentation_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        indent_with_tabs_only_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'indent-with-tabs-only.txt')
        file_name = indent_with_tabs_only_file_path
        file = open(file_name, "r+").read()
        expected = [error.get_error_msg(err_const.TAB_AND_SPACES, [10])]
        result = Lexer().lex(file)
        self.assertEqual(expected, result[const.WARNINGS])

    def test_really_advanced_indentation(self):
        bslint.load_config_file(user_filepath=self.indentation_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        sample_advanced_indentation_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'sample-advanced-indentation.txt')
        file_name = sample_advanced_indentation_file_path
        file = open(file_name, "r+").read()
        expected = []
        result = Lexer().lex(file)
        self.assertEqual(expected, result[const.WARNINGS])
        self.assertEqual(const.SUCCESS, result[const.STATUS])
