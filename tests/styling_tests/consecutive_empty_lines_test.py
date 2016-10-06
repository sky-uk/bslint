import os
import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
from bslint.lexer.lexer import Lexer as Lexer


class TestConsecutiveEmptyLines(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/empty_lines_test_files/")

    def testNoEmptyLines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "no-empty-lines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOneConsecutiveEmptyLine(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "one-consecutive-empty-line.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "only-empty-lines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [
            error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 2]),
            error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3]),
            error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtEnd(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-at-end.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3]),
                   error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtStart(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-at-start.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 2]),
                   error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddle(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-in-middle.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1,4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testCommentNotEmptyLines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "comment-not-empty-lines.brs"
        file = bslint.get_string_to_parse(file_name)
        
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultipleTokensAndEmptyLines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "multiple-tokens-and-empty-lines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1,3])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddleCustomConfig(self):
        bslint.load_config_file(user_filepath="empty_lines/double-empty-lines-config.json", default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-in-middle.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLinesCustomConfig(self):
        bslint.load_config_file(user_filepath="empty_lines/double-empty-lines-config.json", default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "only-empty-lines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [2, 3]),
                   error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [2, 4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)