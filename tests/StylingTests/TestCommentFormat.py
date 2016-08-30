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
        exp_res = ['WARNING: TODOs must follow convention. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testTODONoComment(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['WARNING: Comments must be TODOs and must follow convention. Line number: 11',
                   'WARNING: Comments must be TODOs and must follow convention. Line number: 12',
                   'WARNING: Comments must be TODOs and must follow convention. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODOComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-TODO-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['WARNING: Comments must not be TODOs. Line number: 1',
                   'WARNING: Comments must not be TODOs. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoTODONoComment(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-TODO-no-comment-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['WARNING: No comments allowed. Line number: 1',
                   'WARNING: No comments allowed. Line number: 11',
                   'WARNING: No comments allowed. Line number: 12',
                   'WARNING: No comments allowed. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)