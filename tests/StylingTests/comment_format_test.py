import os
import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as ErrConst
import bslint.error_messages_builder.error_message_handler as Err
import bslint.utilities.commands as commands

class TestCommentFormat(unittest.TestCase):

    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/StylingTestFiles/")

    def testNoCommentCheck(self):
        config = bslint.load_config_file(default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODOComment(self):
        config = bslint.load_config_file(user="Comments/TODO-comment-config.json", default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NON_CONVENTIONAL_TODO, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODONoComment(self):
        config = bslint.load_config_file(user="Comments/ValidCommentSingleQuoteNoTODO.json", default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [11]),
                   self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [12]),
                   self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODOComment(self):
        config = bslint.load_config_file(user="Comments/no-TODO-comment-config.json", default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NO_TODOS, [1]),
                   self.error.get(ErrConst.NO_TODOS, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODONoComment(self):
        config = bslint.load_config_file(user="Comments/no-TODO-no-comment-config.json", default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [1]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [11]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [12]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)