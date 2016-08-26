import unittest

import Constants as const
import src


class TestMiscMethods(unittest.TestCase):

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        
    def testWhiteSpace(self):
        identifier = " "
        exp_result = []
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testSingleQuoteComment(self):
        identifier = "' do stuff \n"
        exp_result = []
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testOpenParenthesis(self):
        identifier = "("
        exp_result = [("(", const.BRACKET, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testCloseParenthesis(self):
        identifier = ")"
        exp_result = [(")", const.BRACKET, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testOpenSquareBracket(self):
        identifier = "["
        exp_result = [("[", const.SQUARE_BRACKET, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)

    def testCloseSquareBracket(self):
        identifier = "]"
        exp_result = [("]", const.SQUARE_BRACKET, 1)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result["Tokens"], exp_result)
