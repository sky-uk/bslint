import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestEqualityOperatorRegex(unittest.TestCase):

    def _match(self, identifier, match_group, lexer_type, parser_type):
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(match_group), identifier)
        self.assertEqual(result["token_lexer_type"], lexer_type)
        self.assertEqual(result["token_parser_type"], parser_type)

    def test_not_equals(self):
        self._match("<>", 0, const.OPERATOR, const.OPERATOR)

    def test_less_than_or_equal(self):
        self._match("<=", 0, const.OPERATOR, const.OPERATOR)

    def test_less_than_or_equal_sec(self):
        self._match("=<", 0, const.OPERATOR, const.OPERATOR)

    def test_greater_than_or_equal(self):
        self._match(">=", 0, const.OPERATOR, const.OPERATOR)

    def test_greater_than_or_equal_sec(self):
        self._match("=>", 0, const.OPERATOR, const.OPERATOR)

    def test_greater_than(self):
        self._match(">", 0, const.OPERATOR, const.OPERATOR)

    def test_less_than(self):
        self._match("<", 0, const.OPERATOR, const.OPERATOR)

    def test_mod(self):
        self._match("MOD", 1, const.KEYWORD, const.KEYWORD)

    def test_not(self):
        self._match("NOT", 1, const.KEYWORD, const.NOT)

    def test_and(self):
        self._match("AND", 1, const.KEYWORD, const.AND)

    def test_or(self):
        self._match("OR", 1, const.KEYWORD, const.OR)