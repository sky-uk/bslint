import os
import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer
from bslint.lexer.token import Token as Token
import bslint.utilities.custom_exceptions as custom_exception
from filepaths import LEXING_TEST_FILES_PATH
from filepaths import STYLING_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestStringRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_string(self):
        self.common.match_regex('"test123ID"', None, const.STRING, const.VALUE)

    def test_unclosed_quotes(self):
        with self.assertRaises(custom_exception.UnexpectedTokenException):
            self.common.match_regex('"test123ID\n', None, const.STRING, const.VALUE)

    def test_variable_assignment_string(self):
        exp_result = [Token('myString', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1),
                      Token('words', const.STRING, const.VALUE, 1)]
        string_file_path = os.path.join(LEXING_TEST_FILES_PATH, 'basic-string-assignment.brs')
        string_file = open(string_file_path, "r+").read()
        result = Lexer().lex(string_file)
        self.assertEqual(result[self.TOKENS], exp_result)

    def test_double_quote_string(self):
        test_string = '""""'
        exp_result = '""'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(), exp_result)
        self.assertEqual(result["token_lexer_type"], const.STRING)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def test_multiline_assignment(self):
        exp_result = [Token('myString', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1),
                      Token("words", const.STRING, const.VALUE, 1),
                      Token('test_String', const.ID, const.ID, 2), Token('=', const.OPERATOR, const.EQUALS, 2),
                      Token("this is words", const.STRING, const.VALUE, 2)]
        multi_line_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'multiline-assignment.txt')
        multi_line_file = open(multi_line_file_path, "r+").read()
        result = Lexer().lex(multi_line_file)
        self.assertEqual(result[self.TOKENS], exp_result)
