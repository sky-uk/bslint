import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestCommentFormat(unittest.TestCase):

    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")

    def test_no_comment_check(self):
        bslint.load_config_file(default_filepath='test-config.json')
        file_name = self.filepath_prefix + "valid-comment-single-quote-no-TODO.txt"
        chars = open(file_name, "r+").read()
        self.assertNotEqual(chars, "")
        exp_res = []
        result = Lexer().lex(chars)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_todo_comment(self):
        bslint.load_config_file(user_filepath="comments/TODO-comment-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "valid-comment-single-quote-no-TODO.txt"
        chars = open(file_name, "r+").read()
        self.assertNotEqual(chars, "")
        exp_res = [error.get_message(err_const.NON_CONVENTIONAL_TODO, [17])]
        result = Lexer().lex(chars)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_todo_no_comment(self):
        bslint.load_config_file(user_filepath="comments/valid-comment-single-quote-no-TODO.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "valid-comment-single-quote-no-TODO.txt"
        chars = open(file_name, "r+").read()
        self.assertNotEqual(chars, "")
        exp_res = [error.get_message(err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [11]),
                   error.get_message(err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [12]),
                   error.get_message(err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [17])]
        result = Lexer().lex(chars)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_no_todo_comment(self):
        bslint.load_config_file(user_filepath="comments/no-TODO-comment-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "valid-comment-single-quote-no-TODO.txt"
        chars = open(file_name, "r+").read()
        self.assertNotEqual(chars, "")
        exp_res = [error.get_message(err_const.NO_TODOS, [1]),
                   error.get_message(err_const.NO_TODOS, [17])]
        result = Lexer().lex(chars)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_no_todo_no_comment(self):
        bslint.load_config_file(user_filepath="comments/no-TODO-no-comment-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "valid-comment-single-quote-no-TODO.txt"
        chars = open(file_name, "r+").read()
        self.assertNotEqual(chars, "")
        exp_res = [
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [1]),
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [11]),
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [12]),
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [17])]
        result = Lexer().lex(chars)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)