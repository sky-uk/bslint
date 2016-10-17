import unittest
import bslint.lexer.regex_handler as regex_handler
from bslint.lexer.styling_handler import StylingHandler as StylingHandler
from bslint.lexer.lexer import Lexer as Lexer


class TestColon(unittest.TestCase):

    def testStatementEndsWithColon(self):
        identifier = ":"
        regex_match = regex_handler.find_match(identifier)
        styling_handler = StylingHandler(identifier)
        styling_handler.apply_styling(regex_match)
        styling_handler.check_end_of_statement()
        self.assertTrue(styling_handler.end_of_statement)

    def testStatementEndsWithColonNoChangeLine(self):
        identifier = "myVar = value: otherVar = otherValue"
        result = Lexer().lex(identifier)
        self.assertEqual(result["Tokens"].pop().line_number, 1)
