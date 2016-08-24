import unittest
import src
import resources.Constants as const


class TestSkipLine(unittest.TestCase):
    def setUp(self):
        self.lexer = src.Lexer()

    def testSkipLineSingleSpace(self):
        identifier = "'  BSLINT_skipline"
        exp_result = [("BSLINT", const.BSLINT_COMMAND)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSkipLineNoSpaces(self):
        identifier = "'BSLINT_skipline"
        exp_result = [("BSLINT", const.BSLINT_COMMAND)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    # Should be interpreted as a string
    def testSkipLineText(self):
        identifier = "' BSLINT_skipline"
        exp_result = [("BSLINT", const.BSLINT_COMMAND)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSkipLineFiveSpaces(self):
        identifier = "'     BSLINT_skipline"
        exp_result = [("BSLINT", const.BSLINT_COMMAND)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSkipLineWithText(self):
        identifier = "' randomText BSLINT_skipline \n"
        exp_result = []
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)