import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestOperatorRegex(unittest.TestCase):

    def _match(self, identifier, lexer_type, parser_type):
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], lexer_type)
        self.assertEqual(result["token_parser_type"], parser_type)

    def test_add_equal(self):
        self._match("+=", const.OPERATOR, const.OPERATOR)

    def test_subtract_equal(self):
        self._match("-=", const.OPERATOR, const.OPERATOR)

    def test_multiply_equal(self):
        self._match("*=", const.OPERATOR, const.OPERATOR)

    def test_divide_equal(self):
        self._match("/=", const.OPERATOR, const.OPERATOR)

    def test_add(self):
        self._match("+", const.OPERATOR, const.PLUS)

    def test_subtract(self):
        self._match("-", const.OPERATOR, const.MINUS)

    def test_multiply(self):
        self._match("*", const.OPERATOR, const.OPERATOR)

    def test_divide(self):
        self._match("/", const.OPERATOR, const.OPERATOR)

    def test_divide_integer(self):
        self._match("\\", const.OPERATOR, const.OPERATOR)

    def test_bitwise_and(self):
        self._match("&", const.OPERATOR, const.OPERATOR)

    def test_exponent(self):
        self._match("^", const.OPERATOR, const.OPERATOR)

    def test_left_shift_assign(self):
        self._match("<<=", const.OPERATOR, const.OPERATOR)

    def test_right_shift_assign(self):
        self._match(">>=", const.OPERATOR, const.OPERATOR)

    def test_left_shift(self):
        self._match("<<", const.OPERATOR, const.OPERATOR)

    def test_right_shift(self):
        self._match(">>", const.OPERATOR, const.OPERATOR)

    def test_divide_integer_assign(self):
        self._match("\=", const.OPERATOR, const.OPERATOR)