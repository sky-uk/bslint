import unittest
import sys
import src


class TestCommentFormat(unittest.TestCase):

    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
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
        exp_res = ['TODOs must be initialled. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODONoComment(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['Comments must be TODOs and must be initialled. Line number: 11',
                   'Comments must be TODOs and must be initialled. Line number: 12',
                   'Comments must be TODOs and must be initialled. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODOComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-TODO-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['Comments must not be TODOs. Line number: 1',
                   'Comments must not be TODOs. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODONoComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-TODO-no-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['Comments are not allowed. Line number: 1',
                   'Comments are not allowed. Line number: 11',
                   'Comments are not allowed. Line number: 12',
                   'Comments are not allowed. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)