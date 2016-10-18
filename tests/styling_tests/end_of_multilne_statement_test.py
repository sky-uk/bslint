import unittest
from bslint.lexer.lexer import Lexer as Lexer


class TestEndOfMultiLineStatement(unittest.TestCase):

    def test__statement__ends__with__curly__brace(self):
        identifier = "myVar = {\n"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertFalse(lexer.handle_style.end_of_statement)

    def test_statement_with_2curly_braces(self):
        identifier = "myVar = {\n{\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertFalse(lexer.handle_style.end_of_statement)

    def test_basic_statement_counting(self):
        identifier = "c = 3\n x = 4"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 2)

    def test_statement_counter_with_colon(self):
        identifier = "c = 3: x = 4"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 2)

    def test_statement_with_2matching_curly_braces(self):
        identifier = "myVar = {\n{\n}\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 1)

    def test_statement_with_2matchin_curly_braces(self):
        identifier = "myVar = {\na: {b:\"Test String\",\n c:\"Test String\"}\n}"
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(lexer.statements_counter, 1)

