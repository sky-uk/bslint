import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer
from bslint.lexer.token import Token as Token
from tests.resources.common.test_methods import CommonMethods as Common


class TestIdentifierRegex(unittest.TestCase):
    TYPE_GROUP = 'type'
    VALUE_GROUP = 'value'

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_basic_identifier(self):
        self.common.match_regex("testId", 0, const.ID, const.ID)

    def test_identifier_with_underscore(self):
        self.common.match_regex("test_Id", self.VALUE_GROUP, const.ID, const.ID)

    def test_identifier_starting_with_underscore(self):
        self.common.match_regex("_testId", self.VALUE_GROUP, const.ID, const.ID)

    def test_identifier_with_numbers_not_start(self):
        self.common.match_regex("test123ID", self.VALUE_GROUP, const.ID, const.ID)

    def test_one_letter_identifier(self):
        self.common.match_regex("t", self.VALUE_GROUP, const.ID, const.ID)

    def test_identifier_as_underscore(self):
        self.common.match_regex("_", 0, const.ID, const.ID)

    def test_identifier_in_statement_with_space(self):
        identifier = "_testId ="
        expected = [Token('_testId', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result["Tokens"])

    def test_identifier_in_statement_dollar(self):
        identifier = "_testId$="
        expected = [Token('_testId', const.ID, const.ID, 1, '$'), Token('=', const.OPERATOR, const.EQUALS, 1, None)]
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result['Tokens'])

    def test_identifier_in_statement_percentage(self):
        identifier = "_testId%"
        expected_result = "_testId"
        expected_type = "%"
        result = regex_handler.find_match(identifier)
        self.assertEqual(expected_result, result["match"].group(self.VALUE_GROUP))
        self.assertEqual(expected_type, result["match"].group(self.TYPE_GROUP))
        self.assertEqual(const.ID, result["token_lexer_type"])
        self.assertEqual(const.ID, result["token_parser_type"])

    def test_identifier_in_statement_exclamation(self):
        identifier = "_testId!"
        expected_result = "_testId"
        expected_type = "!"
        result = regex_handler.find_match(identifier)
        self.assertEqual(expected_result, result["match"].group(self.VALUE_GROUP))
        self.assertEqual(expected_type, result["match"].group(self.TYPE_GROUP))
        self.assertEqual(const.ID, result["token_lexer_type"])
        self.assertEqual(const.ID, result["token_parser_type"])

    def test_identifier_in_statement_hashtag(self):
        identifier = "_testId#"
        expected_result = "_testId"
        expected_type = "#"
        result = regex_handler.find_match(identifier)
        self.assertEqual(expected_result, result["match"].group(self.VALUE_GROUP))
        self.assertEqual(expected_type, result["match"].group(self.TYPE_GROUP))
        self.assertEqual(const.ID, result["token_lexer_type"])

    def test_identifier_in_statement_ampersand(self):
        identifier = "_testId&"
        expected_result = "_testId"
        expected_type = "&"
        result = regex_handler.find_match(identifier)
        self.assertEqual(expected_result, result["match"].group(self.VALUE_GROUP))
        self.assertEqual(expected_type, result["match"].group(self.TYPE_GROUP))
        self.assertEqual(const.ID, result["token_lexer_type"])
        self.assertEqual(const.ID, result["token_parser_type"])

    def test_random(self):
        identifier = 'print "[";_logLevel;"]   ";isoDateTime;"   ";message'
        expected = [Token('print', const.PRINT_KEYWORD, const.PRINT_KEYWORD, 1, None),
                    Token('[', const.STRING, const.VALUE, 1, None),
                    Token(';', const.SEMI_COLON, const.SEMI_COLON, 1, None),
                    Token('_logLevel', const.ID, const.ID, 1, None),
                    Token(';', const.SEMI_COLON, const.SEMI_COLON, 1, None),
                    Token(']   ', const.STRING, const.VALUE, 1, None),
                    Token(';', const.SEMI_COLON, const.SEMI_COLON, 1, None),
                    Token('isoDateTime', const.ID, const.ID, 1, None),
                    Token(';', const.SEMI_COLON, const.SEMI_COLON, 1, None),
                    Token('   ', const.STRING, const.VALUE, 1, None),
                    Token(';', const.SEMI_COLON, const.SEMI_COLON, 1, None),
                    Token('message', const.ID, const.ID, 1, None)]
        result = Lexer().lex(identifier)
        self.assertEqual(expected, result['Tokens'])
