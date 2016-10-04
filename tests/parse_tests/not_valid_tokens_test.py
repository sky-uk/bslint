import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestNotValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.NOT

    def testIdentifier(self):
        current_token_type = const.ID
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testBracket(self):
        current_token_type = const.BRACKET
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
