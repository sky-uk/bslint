import unittest
import sys
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestCommentFormat(unittest.TestCase):

    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def testNoCommentCheck(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-comment-check-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODOComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/TODO-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NON_CONVENTIONAL_TODO, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODONoComment(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [11]),
                   self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [12]),
                   self.error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODOComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-TODO-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.NO_TODOS, [1]),
                   self.error.get(ErrConst.NO_TODOS, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODONoComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-TODO-no-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [1]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [11]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [12]),
            self.error.get(ErrConst.COMMENTS_NOT_ALLOWED, [17])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)