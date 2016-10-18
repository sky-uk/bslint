import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestConsecutiveEmptyLines(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/empty_lines_test_files/")

    def test_no_empty_lines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "no-empty-lines.brs"
        file = open(file_name, "r+").read()
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_one_consecutive_empty_line(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "one-consecutive-empty-line.brs"
        file = open(file_name, "r+").read()
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_only_empty_lines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "only-empty-lines.brs"
        file = open(file_name, "r+").read()
        exp_res = [
            error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 2]),
            error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3]),
            error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_empty_lines_at_end(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-at-end.brs"
        file = open(file_name, "r+").read()
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3]),
                   error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_empty_lines_at_start(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-at-start.brs"
        file = open(file_name, "r+").read()
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 2]),
                   error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1, 3])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_empty_lines_in_middle(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-in-middle.brs"
        file = open(file_name, "r+").read()
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1,4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_comment_not_empty_lines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "comment-not-empty-lines.brs"
        file = open(file_name, "r+").read()
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_multiple_tokens_and_empty_lines(self):
        bslint.load_config_file(user_filepath='empty_lines/single-empty-lines-config.json', default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "multiple-tokens-and-empty-lines.brs"
        file = open(file_name, "r+").read()
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [1,3])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_empty_lines_in_middle_custom_config(self):
        bslint.load_config_file(user_filepath="empty_lines/double-empty-lines-config.json", default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "empty-lines-in-middle.brs"
        file = open(file_name, "r+").read()
        exp_res = []
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_only_empty_lines_custom_config(self):
        bslint.load_config_file(user_filepath="empty_lines/double-empty-lines-config.json", default_filepath='test-config.json')
        file_name = self.tests_filepath_prefix + "only-empty-lines.brs"
        file = open(file_name, "r+").read()
        exp_res = [error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [2, 3]),
                   error.get_message(err_const.CONSECUTIVE_EMPTY_LINES, [2, 4])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)