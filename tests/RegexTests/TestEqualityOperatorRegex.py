import unittest

import Constants as const
import src


class TestEqualityOperatorRegex(unittest.TestCase):

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testNotEquals(self):
        identifier = "<>"
        exp_result = ('<>', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testLessThanOrEqual(self):
        identifier = "<="
        exp_result = ('<=', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testLessThanOrEqualSec(self):
        identifier = "=<"
        exp_result = ('=<', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testGreaterThanOrEqual(self):
        identifier = ">="
        exp_result = ('>=', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testGreaterThanOrEqualSec(self):
        identifier = "=>"
        exp_result = ('=>', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testGreaterThan(self):
        identifier = ">"
        exp_result = ('>', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testLessThan(self):
        identifier = "<"
        exp_result = ('<', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testLessThan(self):
        identifier = "<"
        exp_result = ('<', const.OPERATOR, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testMOD(self):
        identifier = "MOD"
        exp_result = ('MOD', const.KEYWORD, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testNOT(self):
        identifier = "NOT"
        exp_result = ('NOT', const.KEYWORD, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testAND(self):
        identifier = "AND"
        exp_result = ('AND', const.KEYWORD, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)

    def testOR(self):
        identifier = "OR"
        exp_result = ('OR', const.KEYWORD, 1)
        match, token_type = self.lexer.regex_handler(identifier)
        result = self.lexer.build_token(match, token_type)
        self.assertEqual(result, exp_result)