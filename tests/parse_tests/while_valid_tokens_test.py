import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestWhileValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.WHILE

    def testIdentifier(self):
        current_token_type = const.ID
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testNot(self):
        current_token_type = const.NOT
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testWhile(self):
        current_token_type = const.WHILE
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testFor(self):
        current_token_type = const.FOR
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
