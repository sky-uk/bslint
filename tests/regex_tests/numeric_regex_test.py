import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer
from bslint.lexer.token import Token as Token


class TestNumericRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    def testInteger(self):
        identifier = "1234"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.NUMERIC)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testDecimal(self):
        identifier = "123.456"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.NUMERIC)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testIntegerWithTrailingPoints(self):
        identifier = "123."
        exp_result = [Token('123', const.NUMERIC, const.VALUE, 1), Token('.', const.SPECIAL_OPERATOR, const.DOT, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalNumbers(self):
        identifier = "123.123.123"
        exp_result = [Token('123.123', const.NUMERIC, const.VALUE, 1), Token('.', const.SPECIAL_OPERATOR, const.DOT, 1),
                      Token('123', const.NUMERIC, const.VALUE, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalPoints(self):
        identifier = "123..123"
        exp_result = [Token('123', const.NUMERIC, const.VALUE, 1), Token('.', const.SPECIAL_OPERATOR, const.DOT, 1),
                      Token('.', const.SPECIAL_OPERATOR, const.DOT, 1),
                      Token('123', const.NUMERIC, const.VALUE, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)
