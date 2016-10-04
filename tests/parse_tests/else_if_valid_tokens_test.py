import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestElseIfValidTokens(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.IF_STATEMENT

    def testNot(self):
        current_token_type = const.NOT
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testValue(self):
        current_token_type = const.VALUE
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testInvalid(self):
        current_token_type = const.INVALID
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenParenthesis(self):
        current_token_type = const.OPEN_PARENTHESIS
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testNativeFunction(self):
        current_token_type = const.NATIVE_FUNCTION
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testComponent(self):
        current_token_type = const.COMPONENT
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testInterface(self):
        current_token_type = const.INTERFACE
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testEvent(self):
        current_token_type = const.EVENT
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testMinus(self):
        current_token_type = const.MINUS
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testPlus(self):
        current_token_type = const.PLUS
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenCurlyBracket(self):
        current_token_type = const.OPEN_CURLY_BRACKET
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testOpenSquareBracket(self):
        current_token_type = const.OPEN_SQUARE_BRACKET
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testFunction(self):
        current_token_type = const.FUNCTION
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testSub(self):
        current_token_type = const.SUB
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertTrue(result)

    def testCloseParenthesis(self):
        current_token_type = const.CLOSE_PARENTHESIS
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testAs(self):
        current_token_type = const.AS
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testFor(self):
        current_token_type = const.FOR
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)

    def testCloseSquareBracket(self):
        current_token_type = const.CLOSE_SQUARE_BRACKET
        result = Parser.is_valid_token(self.preceding_token_type, current_token_type)
        self.assertFalse(result)