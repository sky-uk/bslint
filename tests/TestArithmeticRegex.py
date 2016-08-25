import unittest

import Constants as const
import src


class TestArithmeticMethods(unittest.TestCase):

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testAddEqual(self):
        identifier = "+="
        exp_result = [('+=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testSubtractEqual(self):
        identifier = "-="
        exp_result = [('-=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testMultiplyEqual(self):
        identifier = "*="
        exp_result = [('*=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testDivideEqual(self):
        identifier = "/="
        exp_result = [('/=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testAdd(self):
        identifier = "+"
        exp_result = [('+', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testSubtract(self):
        identifier = "-"
        exp_result = [('-', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testMultiply(self):
        identifier = "*"
        exp_result = [('*', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testDivide(self):
        identifier = "/"
        exp_result = [('/', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testExponent(self):
        identifier = "^"
        exp_result = [('^', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testLeftShiftAssign(self):
        identifier = "<<="
        exp_result = [('<<=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testRightShiftAssign(self):
        identifier = ">>="
        exp_result = [('>>=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testLeftShift(self):
        identifier = "<<"
        exp_result = [('<<', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testRightShift(self):
        identifier = ">>"
        exp_result = [('>>', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testDivideInteger(self):
        identifier = "\="
        exp_result = [('\=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)