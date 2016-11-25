import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer
from tests.resources.common.test_methods import CommonMethods as Common


class TestMiscRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_open_parenthesis(self):
        self.common.match_regex("(", None, const.OPEN_PARENTHESIS, const.OPEN_PARENTHESIS)

    def test_close_parenthesis(self):
        self.common.match_regex(")", None, const.CLOSE_PARENTHESIS, const.CLOSE_PARENTHESIS)

    def test_open_square_bracket(self):
        self.common.match_regex("[", None, const.OPEN_SQUARE_BRACKET, const.OPEN_SQUARE_BRACKET)

    def test_close_square_bracket(self):
        self.common.match_regex("]", None, const.CLOSE_SQUARE_BRACKET, const.CLOSE_SQUARE_BRACKET)

    def test_open_curly_bracket(self):
        self.common.match_regex("{", None, const.OPEN_CURLY_BRACKET, const.OPEN_CURLY_BRACKET)

    def test_close_curly_bracket(self):
        self.common.match_regex("}", None, const.CLOSE_CURLY_BRACKET, const.CLOSE_CURLY_BRACKET)

    def test_semi_colon(self):
        self.common.match_regex(";", None, const.SEMI_COLON, const.SEMI_COLON)

    def test_at_symbol(self):
        self.common.match_regex("@", None, const.AT_SYMBOL, const.AT_SYMBOL)

    def test_hash_symbol(self):
        self.common.match_regex("#", None, const.HASH_SYMBOL, const.HASH_SYMBOL)

    def test_colon(self):
        self.common.match_regex(":", None, const.COLON, const.COLON)

    def test_space_new_line(self):
        identifier = " \n"
        expected = ' '
        result = regex_handler.find_match(identifier)
        self.assertEqual(expected, result["match"].group())
        self.assertEqual(1, len(result["match"].group()))
        self.assertEqual(None, result["token_lexer_type"])
        self.assertEqual(None, result["token_parser_type"])

    def test_white_space(self):
        identifier = " "
        expected_result = []
        result = Lexer().lex(identifier)
        self.assertEqual(expected_result, result[self.TOKENS])

    def test_single_quote_comment(self):
        identifier = "' do stuff \n"
        expected = []
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result[self.TOKENS])
