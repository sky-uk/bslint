import unittest
import bslint.constants as const
import bslint


class TestMiscRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    def setUp(self):
        config = bslint.load_config_file(default='test-config.json')
        self.lexer = bslint.Lexer(config)
        self.regex_handler = bslint.RegexHandler()
        
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
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.BRACKET)

    def testCloseParenthesis(self):
        identifier = ")"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.BRACKET)

    def testOpenSquareBracket(self):
        identifier = "["
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.SQUARE_BRACKET)

    def testCloseSquareBracket(self):
        identifier = "]"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.SQUARE_BRACKET)
