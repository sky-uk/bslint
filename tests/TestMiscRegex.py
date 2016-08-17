import unittest
import src

class TestMiscMethods(unittest.TestCase):

    def testWhiteSpace(self):
        identifier = " "
        exp_result = []
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSingleQuoteComment(self):
        identifier = "'"
        exp_result = [("'", 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)