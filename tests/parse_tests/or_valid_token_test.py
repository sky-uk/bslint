import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestOrValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.OR

    def testIdentifier(self):
        current_token_type = const.ID
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenParenthesis(self):
        current_token_type = const.OPEN_PARENTHESIS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testNot(self):
        current_token_type = const.NOT
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testPlus(self):
        current_token_type = const.PLUS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testMinus(self):
        current_token_type = const.MINUS
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAnd(self):
        current_token_type = const.AND
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testWhile(self):
        current_token_type = const.WHILE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
