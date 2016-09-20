import unittest
import bslint.constants as const
import bslint.lexer as lexer
import bslint.utilities.regex_handler as regex_handler


class TestMiscRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    def testWhiteSpace(self):
        identifier = " "
        exp_result = []
        result = lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testSingleQuoteComment(self):
        identifier = "' do stuff \n"
        exp_result = []
        result = lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testOpenParenthesis(self):
        identifier = "("
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.BRACKET)

    def testCloseParenthesis(self):
        identifier = ")"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.BRACKET)

    def testOpenSquareBracket(self):
        identifier = "["
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.SQUARE_BRACKET)

    def testCloseSquareBracket(self):
        identifier = "]"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.SQUARE_BRACKET)
