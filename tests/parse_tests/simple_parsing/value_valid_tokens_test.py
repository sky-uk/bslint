import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestValueValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.VALUE

    def testComma(self):
        current_token_type = const.COMMA
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseBracket(self):
        current_token_type = const.CLOSE_PARENTHESIS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testColon(self):
        current_token_type = const.COLON
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAnd(self):
        current_token_type = const.AND
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOr(self):
        current_token_type = const.COMMA
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testID(self):
        current_token_type = const.ID
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
