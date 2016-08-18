import unittest
import src


class TestIdentifierMethods(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()
        
    def testBasicIdentifier(self):
        identifier = "testId"
        exp_result = [('testId', 'ID')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testIdentifierWithUnderscore(self):
        identifier = "test_Id"
        exp_result = [('test_Id', 'ID')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testIdentifierStartingWithUnderscore(self):
        identifier = "_testId"
        exp_result = [('_testId', 'ID')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testIdentifierWithNumbersNotStart(self):
        identifier = "test123ID"
        exp_result = [('test123ID', 'ID')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testOneLetterIdentifier(self):
        identifier = "t"
        exp_result = [('t', 'ID')]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testIdentifierInStatementWithSpace(self):
        identifier = "_testId ="
        exp_result = ('_testId', 'ID')
        result = self.lexer.lex(identifier)
        self.assertEqual(result[0], exp_result)

    def testIdentifierInStatement(self):
        identifier = "_testId$="
        exp_result = ('_testId', 'ID', '$')
        result = self.lexer.lex(identifier)
        self.assertEqual(result[0], exp_result)

    def testIdentifierAsUnderscore(self):
        identifier = "_"
        exp_result = ('_', 'ID')
        result = self.lexer.lex(identifier)
        self.assertEqual(result[0], exp_result)
