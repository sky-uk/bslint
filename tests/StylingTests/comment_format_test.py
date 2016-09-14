import unittest
import src
import src.commands as commands
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os


class TestCommentFormat(unittest.TestCase):

    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../StylingTestFiles/")

    def testNoCommentCheck(self):
        config = src.load_config_file(default='test-config.json')
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODOComment(self):
        config = src.load_config_file(user="Comments/TODO-comment-config.json", default='test-config.json')
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NON_CONVENTIONAL_TODO, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODONoComment(self):
        config = src.load_config_file()
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [11]),
                   self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [12]),
                   self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODOComment(self):
        config = src.load_config_file(user="Comments/no-TODO-comment-config.json", default='test-config.json')
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NO_TODOS, [1]),
                   self.error.get(ErrConst.NO_TODOS, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODONoComment(self):
        config = src.load_config_file(user="Comments/no-TODO-no-comment-config.json", default='test-config.json')
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [1]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [11]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [12]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)