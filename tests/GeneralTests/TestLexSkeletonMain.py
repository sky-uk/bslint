import sys
import unittest

import src


class TestLexSkeletonMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testLexWholeFile(self):
        file = src.main(self.filepath_prefix + "SkeletonMain.brs")
        result = self.lexer.lex(file)
        self.assertEqual(result["Status"], 'Success')

    def testLexWholeFileWithMultipleErrors(self):
        file = src.main(self.filepath_prefix + "SkeletonMainWithErrors.brs")
        result = self.lexer.lex(file)
        self.assertEqual(result["Tokens"], [('Syntax error at: "roSGScreen)\n', 2), ('Syntax error at: "SampleScene)\n', 6)])
        self.assertEqual(result["Status"], 'Error')
