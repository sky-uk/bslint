import os
import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
import bslint.utilities.commands as commands
import bslint.lexer as lexer


class TestMaxLineLength(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/StylingTestFiles/")

    def testValidLineLength(self):
        bslint.load_config_file(default='test-config.json')
        file_name = self.filepath_prefix + "ShortLineLength.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = []
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testExceedMaxLineLength(self):
        bslint.load_config_file(user="LineLength/small-max-line-length-config.json", default='test-config.json')
        file_name = self.filepath_prefix + "ShortLineLength.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEqualMaxLineLength(self):
        bslint.load_config_file(user="LineLength/small-max-line-length-config.json", default='test-config.json')
        file_name = self.filepath_prefix + "EqualMaxLineLength.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = []
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultiLineErrors(self):
        bslint.load_config_file(user="LineLength/small-max-line-length-config.json", default='test-config.json')
        file_name = self.filepath_prefix + "MultilineAssignment.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = [error.get_message(err_const.LINE_LENGTH, [11, 1]),
                      error.get_message(err_const.LINE_LENGTH, [11, 2])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)
