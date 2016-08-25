import unittest

import Constants as const
import src


class TestNumericDeclaration(unittest.TestCase):
    def setUp(self):
        self.lexer = src.Lexer()

    def testInteger(self):
        identifier = "1234"
        exp_result = [('1234', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testDecimal(self):
        identifier = "123.456"
        exp_result = [('123.456', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testIntegerWithTrailingPoints(self):
        identifier = "123."
        exp_result = [('123', const.NUMERIC, 1), ('.', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testMultipleDecimalNumbers(self):
        identifier = "123.123.123"
        exp_result = [('123.123', const.NUMERIC, 1), ('.', const.OPERATOR, 1), ('123', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testMultipleDecimalPoints(self):
        identifier = "123..123"
        exp_result = [('123', const.NUMERIC, 1), ('.', const.OPERATOR, 1), ('.', const.OPERATOR, 1), ('123', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

