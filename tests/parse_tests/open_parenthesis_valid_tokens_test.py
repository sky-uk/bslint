import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestOpenParenthesisValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.OPEN_PARENTHESIS

    def testID(self):
        current_token_type = const.ID
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseParenthesis(self):
        current_token_type = const.CLOSE_PARENTHESIS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testAnd(self):
        current_token_type = const.AND
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testOr(self):
        current_token_type = const.COMMA
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
