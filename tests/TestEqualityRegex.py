import unittest
import src

class TestEqualityMethods(unittest.TestCase):

    def testEquals(self):
        identifier = "=="
        exp_result = [('==', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testNotEquals(self):
        identifier = "<>"
        exp_result = [('<>', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testNotEquals(self):
        identifier = "<="
        exp_result = [('<=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testNotEquals(self):
        identifier = ">="
        exp_result = [('>=', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)