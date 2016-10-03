import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestCloseSquareBracketValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.CLOSE_SQUARE_BRACKET

    def testCloseParenthesis(self):
        current_token_type = const.CLOSE_PARENTHESIS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseSquareBracket(self):
        current_token_type = const.CLOSE_SQUARE_BRACKET
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testDot(self):
        current_token_type = const.DOT
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testComma(self):
        current_token_type = const.COMMA
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAs(self):
        current_token_type = const.AS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testOpenParenthesis(self):
        current_token_type = const.OPEN_PARENTHESIS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testOpenSquareBracket(self):
        current_token_type = const.OPEN_SQUARE_BRACKET
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
