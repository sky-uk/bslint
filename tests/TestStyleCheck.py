import unittest
import sys
import src


class TestStyleCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def testTODONoComment(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        exp_res = ['Comments must be TODOs and must be initialled. Line number: 11',
                   'Comments must be TODOs and must be initialled. Line number: 12',
                   'Comments must be TODOs and must be initialled. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)

    def testNoCommentCheck(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-comment-check-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)

    def testTODOComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/comment-check-TODO-check-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        exp_res = ['TODOs must be initialled. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)

    def testNoTODOComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/comment-check-no-TODO-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        exp_res = ['Comments must not be TODOs. Line number: 1',
                   'Comments must not be TODOs. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)

    def testNoTODONoComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-comment-no-TODO-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        exp_res = ['Comments are not allowed. Line number: 1',
                   'Comments are not allowed. Line number: 11',
                   'Comments are not allowed. Line number: 12',
                   'Comments are not allowed. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)