import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestEqualityOperatorRegex(unittest.TestCase):

    def testNotEquals(self):
        identifier = "<>"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testLessThanOrEqual(self):
        identifier = "<="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testLessThanOrEqualSec(self):
        identifier = "=<"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testGreaterThanOrEqual(self):
        identifier = ">="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testGreaterThanOrEqualSec(self):
        identifier = "=>"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testGreaterThan(self):
        identifier = ">"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testLessThan(self):
        identifier = "<"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.OPERATOR)
        self.assertEqual(result["token_parser_type"], const.OPERATOR)

    def testMOD(self):
        identifier = "MOD "
        exp_result = "MOD"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testNOT(self):
        identifier = "NOT "
        exp_result = "NOT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.NOT)

    def testAND(self):
        identifier = "AND "
        exp_result = "AND"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.AND)

    def testOR(self):
        identifier = "OR "
        exp_result = "OR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.OR)