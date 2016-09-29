import unittest
from bslint import constants as const
from bslint.parser import parser as parser


class TestWhileValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.WHILE

    def testIdentifier(self):
        current_token_type = const.ID
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testNot(self):
        current_token_type = const.NOT
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testWhile(self):
        current_token_type = const.WHILE
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testFor(self):
        current_token_type = const.FOR
        result = parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
