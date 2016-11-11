import os
import unittest

import bslint.messages.handler as msg_handler
import bslint.messages.error_constants as err_const
import bslint.constants as const
from bslint.lexer.lexer import Lexer as Lexer
from bslint.utilities import config_loader
from filepaths import LEXING_TEST_FILES_PATH


class TestLexSkeletonMain(unittest.TestCase):

    def setUp(self):
        config_loader.load_config_file()

    def test_lex_whole_file(self):
        skeleton_main_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main.brs')
        chars = open(skeleton_main_file_path, "r+").read()
        result = Lexer().lex(chars)
        self.assertEqual(result[const.STATUS], const.SUCCESS)

    def test_lex_whole_file_with_multiple_errors(self):
        skeleton_main_with_errors_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'skeleton-main-with-errors.brs')
        chars = open(skeleton_main_with_errors_file_path, "r+").read()
        result = Lexer().lex(chars)
        exp_result = [msg_handler.get_error_msg(err_const.UNMATCHED_QUOTATION_MARK, ['"roSGScreen)', 2])]
        self.assertEqual(result[const.TOKENS], exp_result)
        self.assertEqual(result[const.STATUS], const.ERROR)
