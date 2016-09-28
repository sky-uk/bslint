import unittest


class TestParseIdentifier(unittest.TestCase):

    def testIdentifier(self):
        token = "name"
        lookahead = None
        result = parser_identifier(token, lookahead)
        self.assertTrue(result)

    def testIdentifierWithType(self):
        token = "name$"
        lookahead = None
        result = parser_identifier(token, lookahead)
        self.assertTrue(result)

    def testAssignment(self):
        token = "name"
        lookahead = "="
        result = parser_identifier(token, lookahead)
        self.assertTrue(result)

    def testFunctionCall(self):
        token = "name"
        lookahead = "("
        result = parser_identifier(token, lookahead)
        self.assertTrue(result)

    def testIncorrectLookahead(self):
        token = "name"
        lookahead = "function"
        result = parser_identifier(token, lookahead)
        self.assertFalse(result)

    def testIncorrectLookaheadForKeyword(self):
        token = "name"
        lookahead = "for"
        result = parser_identifier(token, lookahead)
        self.assertFalse(result)

    def testIncorrectLookaheadWhileKeyword(self):
        token = "name"
        lookahead = "while"
        result = parser_identifier(token, lookahead)
        self.assertFalse(result)

    def testIncorrectLookaheadIfKeyword(self):
        token = "name"
        lookahead = "if"
        result = parser_identifier(token, lookahead)
        self.assertFalse(result)