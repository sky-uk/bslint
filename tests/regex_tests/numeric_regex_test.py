import unittest

import bslint.constants as const
from bslint.lexer.lexer import Lexer as Lexer
from bslint.lexer.token import Token as Token
from tests.resources.common.test_methods import CommonMethods as Common


class TestNumericRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_integer(self):
        self.common.match_regex("1234", None, const.NUMERIC, const.VALUE)

    def test_decimal(self):
        self.common.match_regex("123.456", None, const.NUMERIC, const.VALUE)

    def test_integer_with_trailing_points(self):
        identifier = "123."
        expected = [Token('123', const.NUMERIC, const.VALUE, 1), Token('.', const.SPECIAL_OPERATOR, const.DOT, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result[self.TOKENS])

    def test_multiple_decimal_numbers(self):
        identifier = "123.123.123"
        expected = [Token('123.123', const.NUMERIC, const.VALUE, 1), Token('.', const.SPECIAL_OPERATOR, const.DOT, 1),
                    Token('123', const.NUMERIC, const.VALUE, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result[self.TOKENS])

    def test_multiple_decimal_points(self):
        identifier = "123..123"
        expected = [Token('123', const.NUMERIC, const.VALUE, 1), Token('.', const.SPECIAL_OPERATOR, const.DOT, 1),
                    Token('.', const.SPECIAL_OPERATOR, const.DOT, 1),
                    Token('123', const.NUMERIC, const.VALUE, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result[self.TOKENS])
