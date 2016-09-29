import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestNotValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.NOT

    def testIdentifier(self):
        current_token_type = const.ID
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testBracket(self):
        current_token_type = const.BRACKET
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
