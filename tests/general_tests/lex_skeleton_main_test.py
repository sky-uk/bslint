import os
import unittest

import bslint.error_messages.handler as err
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import LEXING_TEST_FILES_PATH
from bslint.utilities import config_loader


class TestLexSkeletonMain(unittest.TestCase):

    def setUp(self):
        config_loader.load_config_file()

    def test_lex_whole_file(self):
        skeleton_main_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main.brs')
        chars = open(skeleton_main_file_path, "r+").read()
        result = Lexer().lex(chars)
        self.assertEqual(result["Status"], 'Success')

    def test_lex_whole_file_with_multiple_errors(self):
        skeleton_main_with_errors_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main-with-errors.brs')
        chars = open(skeleton_main_with_errors_file_path, "r+").read()
        result = Lexer().lex(chars)
        exp_result = [err.get_message(err_const.UNMATCHED_QUOTATION_MARK, ['"roSGScreen)', 2])]
        self.assertEqual(result["Tokens"], exp_result)
        self.assertEqual(result["Status"], 'Error')
