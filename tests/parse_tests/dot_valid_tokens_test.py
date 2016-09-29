import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestDotValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.DOT

    def testIdentifier(self):
        current_token_type = const.ID
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


