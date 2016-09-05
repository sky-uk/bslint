import sys
import unittest
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestLexSkeletonMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
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
        exp_result = [self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK, ['"roSGScreen', 2]),
                      self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK, ['"SampleScene', 6])]
        self.assertEqual(result["Tokens"], exp_result)
        self.assertEqual(result["Status"], 'Error')
