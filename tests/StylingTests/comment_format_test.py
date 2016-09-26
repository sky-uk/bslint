import os
import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
import bslint.utilities.commands as commands
import bslint.lexer as lexer

class TestCommentFormat(unittest.TestCase):

    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/StylingTestFiles/")

    def testNoCommentCheck(self):
        bslint.load_config_file(default_filepath='test-config.json')
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODOComment(self):
        bslint.load_config_file(user_filepath="Comments/TODO-comment-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [error.get_message(err_const.NON_CONVENTIONAL_TODO, [17])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODONoComment(self):
        bslint.load_config_file(user_filepath="Comments/ValidCommentSingleQuoteNoTODO.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [error.get_message(err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [11]),
                   error.get_message(err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [12]),
                   error.get_message(err_const.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [17])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODOComment(self):
        bslint.load_config_file(user_filepath="Comments/no-TODO-comment-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [error.get_message(err_const.NO_TODOS, [1]),
                   error.get_message(err_const.NO_TODOS, [17])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODONoComment(self):
        bslint.load_config_file(user_filepath="Comments/no-TODO-no-comment-config.json", default_filepath='test-config.json')
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [1]),
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [11]),
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [12]),
            error.get_message(err_const.COMMENTS_NOT_ALLOWED, [17])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)