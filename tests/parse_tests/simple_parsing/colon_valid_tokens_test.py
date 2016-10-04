import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestColonValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.COLON

    def testID(self):
        current_token_type = const.ID
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testNot(self):
        current_token_type = const.NOT
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testMinus(self):
        current_token_type = const.MINUS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testPlus(self):
        current_token_type = const.PLUS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenParenthesis(self):
        current_token_type = const.OPEN_PARENTHESIS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenSquareBracket(self):
        current_token_type = const.OPEN_SQUARE_BRACKET
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenCurlyBracket(self):
        current_token_type = const.OPEN_CURLY_BRACKET
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAs(self):
        current_token_type = const.AS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testFor(self):
        current_token_type = const.FOR
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testCloseSquareBracket(self):
        current_token_type = const.CLOSE_SQUARE_BRACKET
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)