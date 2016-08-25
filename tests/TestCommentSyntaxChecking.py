import unittest
import sys
import src


class TestCommentSyntaxChecking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def setUp(self):
        self.lexer = src.Lexer()

    def testAllCommentTypes(self):
        file_name = self.filepath_prefix + "ValidCommentSingleQuoteNoTODO.txt"
        file = src.main(file_name)
        exp_res = ['Comments must be TODOs and must be initialled. Line number: 11',
                   'Comments must be TODOs and must be initialled. Line number: 12',
                   'Comments must be TODOs and must be initialled. Line number: 17']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)
