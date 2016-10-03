import unittest
import bslint.constants as const
from bslint.lexer import Lexer as Lexer
import bslint.utilities.regex_handler as regex_handler


class TestNumericRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    def testInteger(self):
        identifier = "1234"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.NUMERIC)

    def testDecimal(self):
        identifier = "123.456"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.NUMERIC)

    def testIntegerWithTrailingPoints(self):
        identifier = "123."
        exp_result = [('123', const.NUMERIC, 1), ('.', const.SPECIAL_OPERATOR, 1)]
        result = Lexer(identifier).lex()
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalNumbers(self):
        identifier = "123.123.123"
        exp_result = [('123.123', const.NUMERIC, 1), ('.', const.SPECIAL_OPERATOR, 1), ('123', const.NUMERIC, 1)]
        result = Lexer(identifier).lex()
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalPoints(self):
        identifier = "123..123"
        exp_result = [('123', const.NUMERIC, 1), ('.', const.SPECIAL_OPERATOR, 1), ('.', const.SPECIAL_OPERATOR, 1),
                      ('123', const.NUMERIC, 1)]
        result = Lexer(identifier).lex()
        self.assertEqual(result[self.TOKENS], exp_result)
