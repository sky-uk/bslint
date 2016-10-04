import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestOpenParenthesisValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.OPEN_PARENTHESIS

    def testID(self):
        current_token_type = const.ID
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseParenthesis(self):
        current_token_type = const.CLOSE_PARENTHESIS
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testAnd(self):
        current_token_type = const.AND
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testOr(self):
        current_token_type = const.COMMA
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
