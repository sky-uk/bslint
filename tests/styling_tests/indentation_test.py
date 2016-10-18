import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer


class TestIndentation(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")

    def test_no_indentation(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        exp_result = None
        current_indentation_level = 0
        characters = "var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(result[0], exp_result)

    def test_single_indentation(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        exp_result = None
        current_indentation_level = 1
        characters = "    var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(result[0], exp_result)

    def test_indentation_error(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        file_name = self.filepath_prefix + "basic-indentation.txt"
        file = open(file_name, "r+").read()
        exp_result = [error.get_message(err_const.TAB_INDENTATION_ERROR, [4, 2])]
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def test_advanced_indentation_success(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        file_name = self.filepath_prefix + "advanced-indentation.txt"
        file = open(file_name, "r+").read()
        exp_result = []
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def test_indent_with_only_tabs_with_error(self):
        bslint.load_config_file(user_filepath="indentation/tab-only-indentation.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "indent-with-tabs-only.txt"
        file = open(file_name, "r+").read()
        exp_result = [error.get_message(err_const.TAB_AND_SPACES, [10])]
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def test_really_advanced_indentation(self):
        bslint.load_config_file(user_filepath="indentation/indentation-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "sample-advanced-indentation.txt"
        file = open(file_name, "r+").read()
        exp_result = []
        exp_status = "Success"
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])
        self.assertEqual(exp_status, result[self.STATUS])
