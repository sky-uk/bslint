import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestEqualityOperatorRegex(unittest.TestCase):

    def test_not_equals(self):
        identifier = "<>"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_less_than_or_equal(self):
        identifier = "<="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_less_than_or_equal_sec(self):
        identifier = "=<"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_greater_than_or_equal(self):
        identifier = ">="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_greater_than_or_equal_sec(self):
        identifier = "=>"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_greater_than(self):
        identifier = ">"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_less_than(self):
        identifier = "<"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def test_mod(self):
        identifier = "MOD "
        exp_result = "MOD"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_not(self):
        identifier = "NOT "
        exp_result = "NOT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.NOT)

    def test_and(self):
        identifier = "AND "
        exp_result = "AND"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.AND)

    def test_or(self):
        identifier = "OR "
        exp_result = "OR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.OR)