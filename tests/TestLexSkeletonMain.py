import sys
import unittest

import src


class TestLexSkeletonMain(unittest.TestCase):
    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testLexWholeFile(self):
        if sys.argv[0].endswith('nosetests'):
            file = src.main("./resources/SkeletonMain.brs")
        else:
            file = src.main("../resources/SkeletonMain.brs")

        result = self.lexer.lex(file)
        self.assertNotEqual(result["Status"], 'Error')

    def testLexWholeFileWithMultipleErrors(self):
        if sys.argv[0].endswith('nosetests'):
            file = src.main("./resources/SkeletonMainWithErrors.brs")
        else:
            file = src.main("../resources/SkeletonMainWithErrors.brs")
        result = self.lexer.lex(file)
        self.assertEqual(result["Tokens"], [('Syntax error at: "roSGScreen)\n', 2), ('Syntax error at: "SampleScene)\n', 6)])
