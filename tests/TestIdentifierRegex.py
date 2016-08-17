import unittest
import src


class TestIdentifierMethods(unittest.TestCase):

    def testBasicIdentifier(self):
        identifier = "testId"
        exp_result = [('testId', 'ID')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testIdentifierWithUnderscore(self):
        identifier = "test_Id"
        exp_result = [('test_Id', 'ID')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testIdentifierStartingWithUnderscore(self):
        identifier = "_testId"
        exp_result = [('_testId', 'ID')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    # def testIdentifierStartingWithNumbers(self):
     #   identifier = "123testId"
      #  with self.assertRaises(NameError):
        #      src.lexer(identifier)

    def testOneLetterIdentifier(self):
        identifier = "t"
        exp_result = [('t', 'ID')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)
