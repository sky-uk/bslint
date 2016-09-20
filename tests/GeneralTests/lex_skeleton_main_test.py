import unittest
import bslint
import bslint.error_messages_builder.error_message_handler as Err
import bslint.error_messages_builder.error_builder.error_messages_constants as ErrConst
import os



class TestLexSkeletonMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/LexingTestFiles/")

    def setUp(self):
        self.lexer = bslint.Lexer()

    def testLexWholeFile(self):
        file = bslint.get_string_to_parse(self.filepath_prefix + "SkeletonMain.brs")
        result = self.lexer.lex(file)
        self.assertEqual(result["Status"], 'Success')

    def testLexWholeFileWithMultipleErrors(self):
        file = bslint.get_string_to_parse(self.filepath_prefix + "SkeletonMainWithErrors.brs")
        result = self.lexer.lex(file)
        exp_result = [self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK, ['"roSGScreen', 2]),
                      self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK, ['"SampleScene', 6])]
        self.assertEqual(result["Tokens"], exp_result)
        self.assertEqual(result["Status"], 'Error')
