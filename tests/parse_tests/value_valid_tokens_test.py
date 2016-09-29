import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestValueValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.VALUE

    def testComma(self):
        current_token_type = const.COMMA
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseBracket(self):
        current_token_type = const.CLOSE_PARENTHESIS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testColon(self):
        current_token_type = const.COLON
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAnd(self):
        current_token_type = const.AND
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOr(self):
        current_token_type = const.COMMA
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testID(self):
        current_token_type = const.ID
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
