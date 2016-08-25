import unittest

import Constants as const
import src


class TestIdentifierMethods(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()
        
    def testBasicIdentifier(self):
        identifier = "testId"
        exp_result = [('testId', const.ID, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierWithUnderscore(self):
        identifier = "test_Id"
        exp_result = [('test_Id', const.ID, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierStartingWithUnderscore(self):
        identifier = "_testId"
        exp_result = [('_testId', const.ID, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierWithNumbersNotStart(self):
        identifier = "test123ID"
        exp_result = [('test123ID', const.ID, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testOneLetterIdentifier(self):
        identifier = "t"
        exp_result = [('t', const.ID, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementWithSpace(self):
        identifier = "_testId ="
        exp_result = [('_testId', const.ID, 1), ('=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementDollar(self):
        identifier = "_testId$="
        exp_result = [('_testId', const.ID, '$', 1), ('=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierAsUnderscore(self):
        identifier = "_"
        exp_result = [('_', const.ID, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementPercentage(self):
        identifier = "_testId%"
        exp_result = [('_testId', const.ID, '%', 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementExclamation(self):
        identifier = "_testId!"
        exp_result = [('_testId', const.ID, '!', 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementHashtag(self):
        identifier = "_testId#"
        exp_result = [('_testId', const.ID, '#', 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementAmpersand(self):
        identifier = "_testId&"
        exp_result = [('_testId', const.ID, '&', 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)
