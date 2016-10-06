import os
import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
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

    def testNoIndentation(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        exp_result = None
        current_indentation_level = 0
        characters = "var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(result[0], exp_result)

    def testSingleIndentation(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        exp_result = None
        current_indentation_level = 1
        characters = "    var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(result[0], exp_result)

    def testIndentationError(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        file_name = self.filepath_prefix + "basic-indentation.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = [error.get_message(err_const.TAB_INDENTATION_ERROR, [4, 2])]
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testAdvancedIndentationSuccess(self):
        bslint.load_config_file(user_filepath='indentation/indentation-config.json', default_filepath='test-config.json')
        file_name = self.filepath_prefix + "advanced-indentation.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = []
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testIndentWithOnlyTabsWithError(self):
        bslint.load_config_file(user_filepath="indentation/tab-only-indentation.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "indent-with-tabs-only.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = [error.get_message(err_const.TAB_AND_SPACES, [10])]
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testReallyAdvancedIndentation(self):
        bslint.load_config_file(user_filepath="indentation/indentation-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "sample-advanced-indentation.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = []
        exp_status = "Success"
        result = Lexer().lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])
        self.assertEqual(exp_status, result[self.STATUS])
