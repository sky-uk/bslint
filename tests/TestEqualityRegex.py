import unittest
import src


class TestEqualityMethods(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()

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

    def testLessThan(self):
        identifier = "<"
        exp_result = [('<', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testMOD(self):
        identifier = "MOD"
        exp_result = [('MOD', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testNOT(self):
        identifier = "NOT"
        exp_result = [('NOT', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testAND(self):
        identifier = "AND"
        exp_result = [('AND', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testOR(self):
        identifier = "OR"
        exp_result = [('OR', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)