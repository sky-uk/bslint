import unittest
import src


class TestMiscMethods(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()
        
    def testWhiteSpace(self):
        identifier = " "
        exp_result = []
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSingleQuoteComment(self):
        identifier = "'"
        exp_result = [("'", 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)