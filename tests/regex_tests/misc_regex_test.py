import unittest
import bslint.constants as const
from bslint.lexer import Lexer as Lexer
import bslint.utilities.regex_handler as regex_handler


class TestMiscRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    def testWhiteSpace(self):
        identifier = " "
        exp_result = []
        result = Lexer(identifier).lex()
        self.assertEqual(result[self.TOKENS], exp_result)

    def testSingleQuoteComment(self):
        identifier = "' do stuff \n"
        exp_result = []
        result = Lexer(identifier).lex()
        self.assertEqual(result[self.TOKENS], exp_result)

    def testOpenParenthesis(self):
        identifier = "("
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.BRACKET)
        self.assertEqual(result["token_parser_type"], const.OPEN_PARENTHESIS)

    def testCloseParenthesis(self):
        identifier = ")"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.BRACKET)
        self.assertEqual(result["token_parser_type"], const.CLOSE_PARENTHESIS)

    def testOpenSquareBracket(self):
        identifier = "["
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.SQUARE_BRACKET)
        self.assertEqual(result["token_parser_type"], const.OPEN_SQUARE_BRACKET)

    def testCloseSquareBracket(self):
        identifier = "]"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.SQUARE_BRACKET)
        self.assertEqual(result["token_parser_type"], const.CLOSE_SQUARE_BRACKET)

    def testOpenCurlyBracket(self):
        identifier = "{"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.CURLY_BRACKET)
        self.assertEqual(result["token_parser_type"], const.OPEN_CURLY_BRACKET)

    def testCloseCurlyBracket(self):
        identifier = "}"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.CURLY_BRACKET)
        self.assertEqual(result["token_parser_type"], const.CLOSE_CURLY_BRACKET)

    def testSemiColon(self):
        identifier = ";"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.SEMI_COLON)
        self.assertEqual(result["token_parser_type"], const.SEMI_COLON)

    def testAtSymbol(self):
        identifier = "@"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.AT_SYMBOL)
        self.assertEqual(result["token_parser_type"], const.AT_SYMBOL)

    def testHashSymbol(self):
        identifier = "#"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.HASH_SYMBOL)
        self.assertEqual(result["token_parser_type"], const.HASH_SYMBOL)
