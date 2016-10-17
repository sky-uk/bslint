import unittest
from bslint.lexer.lexer import Lexer as Lexer


class TestEndOfMultiLineStatement(unittest.TestCase):

    def testStatementEndsWithCurlyBrace(self):
        identifier = "myVar = {\n"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertFalse(lexer.handle_style.end_of_statement)

    def testStatementWith2CurlyBraces(self):
        identifier = "myVar = {\n{\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertFalse(lexer.handle_style.end_of_statement)

    def testBasicStatementCounting(self):
        identifier = "c = 3\n x = 4"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 2)

    def testStatementCounterWithColon(self):
        identifier = "c = 3: x = 4"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 2)

    def testStatementWith2MatchingCurlyBraces(self):
        identifier = "myVar = {\n{\n}\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 1)

    def testStatementWith2MatchinCurlyBraces(self):
        identifier = "myVar = {\na: {b:\"Test String\",\n c:\"Test String\"}\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 1)

