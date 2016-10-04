import unittest
import bslint
import bslint.error_messages_builder.error_message_handler as err
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import os
from bslint.lexer import Lexer as Lexer


class TestLexSkeletonMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/lexing_test_files/")

    def testLexWholeFile(self):
        file = bslint.get_string_to_parse(self.filepath_prefix + "skeleton-main.brs")
        result = Lexer().lex(file)
        self.assertEqual(result["Status"], 'Success')

    def testLexWholeFileWithMultipleErrors(self):
        file = bslint.get_string_to_parse(self.filepath_prefix + "skeleton-main-with-errors.brs")
        result = Lexer().lex(file)
        exp_result = [err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"roSGScreen', 2]),
                      err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"SampleScene', 6])]
        self.assertEqual(result["Tokens"], exp_result)
        self.assertEqual(result["Status"], 'Error')
