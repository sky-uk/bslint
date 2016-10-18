import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer


class TestMiscRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    def test_white_space(self):
        identifier = " "
        exp_result = []
        result = Lexer().lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def test_single_quote_comment(self):
        identifier = "' do stuff \n"
        exp_result = []
        result = Lexer().lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def test_open_parenthesis(self):
        identifier = "("
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.BRACKET)
        self.assertEqual(result["token_parser_type"], const.OPEN_PARENTHESIS)

    def test_close_parenthesis(self):
        identifier = ")"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.BRACKET)
        self.assertEqual(result["token_parser_type"], const.CLOSE_PARENTHESIS)

    def test_open_square_bracket(self):
        identifier = "["
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.SQUARE_BRACKET)
        self.assertEqual(result["token_parser_type"], const.OPEN_SQUARE_BRACKET)

    def test_close_square_bracket(self):
        identifier = "]"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.SQUARE_BRACKET)
        self.assertEqual(result["token_parser_type"], const.CLOSE_SQUARE_BRACKET)

    def test_open_curly_bracket(self):
        identifier = "{"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPEN_CURLY_BRACKET)
        self.assertEqual(result["token_parser_type"], const.OPEN_CURLY_BRACKET)

    def test_close_curly_bracket(self):
        identifier = "}"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.CLOSE_CURLY_BRACKET)
        self.assertEqual(result["token_parser_type"], const.CLOSE_CURLY_BRACKET)

    def test_semi_colon(self):
        identifier = ";"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.SEMI_COLON)
        self.assertEqual(result["token_parser_type"], const.SEMI_COLON)

    def test_at_symbol(self):
        identifier = "@"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.AT_SYMBOL)
        self.assertEqual(result["token_parser_type"], const.AT_SYMBOL)

    def test_hash_symbol(self):
        identifier = "#"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.HASH_SYMBOL)
        self.assertEqual(result["token_parser_type"], const.HASH_SYMBOL)

    def test_space_new_line(self):
        identifier = " \n"
        exp_res = ' '
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), exp_res)
        self.assertEqual(len(result["match"].group()), 1)
        self.assertEqual(result["token_lexer_type"], None)
        self.assertEqual(result["token_parser_type"], None)

    def testColon(self):
        identifier = ":"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.COLON)
        self.assertEqual(result["token_parser_type"], const.COLON)
