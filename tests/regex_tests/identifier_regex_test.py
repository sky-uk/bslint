import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer
from bslint.lexer.token import Token as Token


class TestIdentifierRegex(unittest.TestCase):

    TYPE_GROUP = 'type'
    VALUE_GROUP = 'value'

    def _match(self, identifier, match_group):
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(match_group), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def test_basic_identifier(self):
        self._match("testId", 0)

    def test_identifier_with_underscore(self):
        self._match("test_Id", self.VALUE_GROUP)

    def test_identifier_starting_with_underscore(self):
        self._match("_testId", self.VALUE_GROUP)

    def test_identifier_with_numbers_not_start(self):
        self._match("test123ID", self.VALUE_GROUP)

    def test_one_letter_identifier(self):
        self._match("t", self.VALUE_GROUP)

    def test_identifier_as_underscore(self):
        self._match("_", 0)

    def test_identifier_in_statement_with_space(self):
        identifier = "_testId ="
        exp_result = [Token('_testId', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1)]
        result = Lexer().lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def test_identifier_in_statement_dollar(self):
        identifier = "_testId$="
        exp_result = [Token('_testId', const.ID, const.ID, 1, '$'), Token('=', const.OPERATOR, const.EQUALS, 1, None)]
        result = Lexer().lex(identifier)
        self.assertEqual(result['Tokens'], exp_result)

    def test_identifier_in_statement_percentage(self):
        identifier = "_testId%"
        exp_result = "_testId"
        exp_type = "%"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def test_identifier_in_statement_exclamation(self):
        identifier = "_testId!"
        exp_result = "_testId"
        exp_type = "!"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def test_identifier_in_statement_hashtag(self):
        identifier = "_testId#"
        exp_result = "_testId"
        exp_type = "#"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)

    def test_identifier_in_statement_ampersand(self):
        identifier = "_testId&"
        exp_result = "_testId"
        exp_type = "&"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)
