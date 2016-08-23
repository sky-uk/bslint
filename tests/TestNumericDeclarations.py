import unittest
import src
import resources.Constants as const


class TestNumericDeclaration(unittest.TestCase):
    def setUp(self):
        self.lexer = src.Lexer()

    def testInteger(self):
        identifier = "1234"
        exp_result = [('1234', const.NUMERIC)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testDecimal(self):
        identifier = "123.456"
        exp_result = [('123.456', const.NUMERIC)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testIntegerWithTrailingPoints(self):
        identifier = "123."
        exp_result = [('123', const.NUMERIC), ('.', const.OPERATOR)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testMultipleDecimalNumbers(self):
        identifier = "123.123.123"
        exp_result = [('123.123', const.NUMERIC), ('.', const.OPERATOR), ('123', const.NUMERIC)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testMultipleDecimalPoints(self):
        identifier = "123..123"
        exp_result = [('123', const.NUMERIC), ('.', const.OPERATOR), ('.', const.OPERATOR), ('123', const.NUMERIC)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

