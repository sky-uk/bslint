import unittest
import src
import resources.Constants as const


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
        exp_result = [("'", const.STMT)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testOpenParenthesis(self):
        identifier = "("
        exp_result = [("(", const.STMT)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testCloseParenthesis(self):
        identifier = ")"
        exp_result = [(")", const.STMT)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testOpenSquareBracket(self):
        identifier = "["
        exp_result = [("[", const.STMT)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testCloseSquareBracket(self):
        identifier = "]"
        exp_result = [("]", const.STMT)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)
