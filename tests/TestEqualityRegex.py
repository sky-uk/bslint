import unittest
import src


class TestEqualityMethods(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()
        
    def testEquals(self):
        identifier = "=="
        exp_result = [('==', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testNotEquals(self):
        identifier = "<>"
        exp_result = [('<>', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testLessThanOrEqual(self):
        identifier = "<="
        exp_result = [('<=', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testLessThanOrEqualSec(self):
        identifier = "=<"
        exp_result = [('=<', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGreaterThanOrEqual(self):
        identifier = ">="
        exp_result = [('>=', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGreaterThanOrEqualSec(self):
        identifier = "=>"
        exp_result = [('=>', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGreaterThan(self):
        identifier = ">"
        exp_result = [('>', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testLessThan(self):
        identifier = "<"
        exp_result = [('<', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)
