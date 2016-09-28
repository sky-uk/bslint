import unittest


class TestParseRightHandSideOfEquals(unittest.TestCase):

    def testRightSideOfAssignment(self):
        token = "="
        lookahead = '"string value"'
        result = parser_equal_operator(token, lookahead)
        self.assertTrue(result)

    def testRightSideOfAssignmentWithNumber(self):
        token = "="
        lookahead = 123
        result = parser_equal_operator(token, lookahead)
        self.assertTrue(result)

    def testRightSideOfAssignmentWithDecimal(self):
        token = "="
        lookahead = 123.45
        result = parser_equal_operator(token, lookahead)
        self.assertTrue(result)

    def testRightSideOfAssignmentWithBoolean(self):
        token = "="
        lookahead = True
        result = parser_equal_operator(token, lookahead)
        self.assertTrue(result)

    def testRightSideOfAssignmentWithIdentifier(self):
        token = "="
        lookahead = "other_variable"
        result = parser_equal_operator(token, lookahead)
        self.assertTrue(result)

    def testRightHandSideOfEqualWithFunctionKeyword(self):
        token = "="
        lookahead = "function"
        result = parser_equal_operator(token, lookahead)
        self.assertTrue(result)

    def testIncorrectRightHandSideOfEqualWithOperator(self):
        token = "="
        lookahead = "/"
        result = parser_equal_operator(token, lookahead)
        self.assertFalse(result)

    def testIncorrectRightHandSideOfEqualWithWhileKeyword(self):
        token = "="
        lookahead = "while"
        result = parser_equal_operator(token, lookahead)
        self.assertFalse(result)

    def testIncorrectRightHandSideOfEqualWithForKeyword(self):
        token = "="
        lookahead = "for"
        result = parser_equal_operator(token, lookahead)
        self.assertFalse(result)



