import unittest

import Constants as const
import src


class TestMiscRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        
    def testWhiteSpace(self):
        identifier = " "
        exp_result = []
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testSingleQuoteComment(self):
        identifier = "' do stuff \n"
        exp_result = []
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testOpenParenthesis(self):
        identifier = "("
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.BRACKET)

    def testCloseParenthesis(self):
        identifier = ")"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.BRACKET)

    def testOpenSquareBracket(self):
        identifier = "["
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.SQUARE_BRACKET)

    def testCloseSquareBracket(self):
        identifier = "]"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.SQUARE_BRACKET)
