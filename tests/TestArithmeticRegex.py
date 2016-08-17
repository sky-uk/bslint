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
