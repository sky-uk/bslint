import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestOpenCurlyBracketValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.OPEN_CURLY_BRACKET

    def testID(self):
        current_token_type = const.ID
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseCurlyBracket(self):
        current_token_type = const.CLOSE_CURLY_BRACKET
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAs(self):
        current_token_type = const.AS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testOpenCurlyBracket(self):
        current_token_type = const.OPEN_CURLY_BRACKET
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testFor(self):
        current_token_type = const.FOR
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
