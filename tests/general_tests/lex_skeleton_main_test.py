import os
import unittest

import bslint.error_messages.handler as err
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestLexSkeletonMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/lexing_test_files/")

    def test_lex_whole_file(self):
        chars = open(self.filepath_prefix + "skeleton-main.brs", "r+").read()
        result = Lexer().lex(chars)
        self.assertEqual(result["Status"], 'Success')

    def test_lex_whole_file_with_multiple_errors(self):
        chars = open(self.filepath_prefix + "skeleton-main-with-errors.brs", "r+").read()
        result = Lexer().lex(chars)
        exp_result = [err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"roSGScreen', 2]),
                      err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"SampleScene', 6])]
        self.assertEqual(result["Tokens"], exp_result)
        self.assertEqual(result["Status"], 'Error')
