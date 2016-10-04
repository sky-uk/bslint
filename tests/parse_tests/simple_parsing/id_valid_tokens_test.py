import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestIDValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.ID

    def testDot(self):
        current_token_type = const.DOT
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOperator(self):
        current_token_type = const.OPERATOR
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testBracket(self):
        current_token_type = const.BRACKET
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testColon(self):
        current_token_type = const.COLON
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAs(self):
        current_token_type = const.AS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testId(self):
        current_token_type = const.EQUALS
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testAnd(self):
        current_token_type = const.AND
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOr(self):
        current_token_type = const.OR
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testComma(self):
        current_token_type = const.COMMA
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testID(self):
        current_token_type = const.ID
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testWhile(self):
        current_token_type = const.WHILE
        result = Parser().check_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)
