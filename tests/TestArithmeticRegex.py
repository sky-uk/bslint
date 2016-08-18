import unittest
import src

class TestArithmeticMethods(unittest.TestCase):

    def testAddEqual(self):
        identifier = "+="
        exp_result = [('+=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSubtractEqual(self):
        identifier = "-="
        exp_result = [('-=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testMultiplyEqual(self):
        identifier = "*="
        exp_result = [('*=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testDivideEqual(self):
        identifier = "/="
        exp_result = [('/=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testAdd(self):
        identifier = "+"
        exp_result = [('+', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSubtract(self):
        identifier = "-"
        exp_result = [('-', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testMultiply(self):
        identifier = "*"
        exp_result = [('*', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testDivide(self):
        identifier = "/"
        exp_result = [('/', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testExponent(self):
        identifier = "^"
        exp_result = [('^', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testLeftShiftAssign(self):
        identifier = "<<="
        exp_result = [('<<=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testRightShiftAssign(self):
        identifier = ">>="
        exp_result = [('>>=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testLeftShift(self):
        identifier = "<<"
        exp_result = [('<<', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testRightShift(self):
        identifier = ">>"
        exp_result = [('>>', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testDivideInteger(self):
        identifier = "\="
        exp_result = [('\=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)