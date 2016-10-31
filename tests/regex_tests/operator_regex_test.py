import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestOperatorRegex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_add_equal(self):
        self.common.match_regex("+=", None, const.OPERATOR, const.OPERATOR)

    def test_subtract_equal(self):
        self.common.match_regex("-=", None, const.OPERATOR, const.OPERATOR)

    def test_multiply_equal(self):
        self.common.match_regex("*=", None, const.OPERATOR, const.OPERATOR)

    def test_divide_equal(self):
        self.common.match_regex("/=", None, const.OPERATOR, const.OPERATOR)

    def test_add(self):
        self.common.match_regex("+", None, const.OPERATOR, const.PLUS)

    def test_subtract(self):
        self.common.match_regex("-", None, const.OPERATOR, const.MINUS)

    def test_multiply(self):
        self.common.match_regex("*", None, const.OPERATOR, const.OPERATOR)

    def test_divide(self):
        self.common.match_regex("/", None, const.OPERATOR, const.OPERATOR)

    def test_divide_integer(self):
        self.common.match_regex("\\", None, const.OPERATOR, const.OPERATOR)

    def test_bitwise_and(self):
        self.common.match_regex("&", None, const.OPERATOR, const.OPERATOR)

    def test_exponent(self):
        self.common.match_regex("^", None, const.OPERATOR, const.OPERATOR)

    def test_left_shift_assign(self):
        self.common.match_regex("<<=", None, const.OPERATOR, const.OPERATOR)

    def test_right_shift_assign(self):
        self.common.match_regex(">>=", None, const.OPERATOR, const.OPERATOR)

    def test_left_shift(self):
        self.common.match_regex("<<", None, const.OPERATOR, const.OPERATOR)

    def test_right_shift(self):
        self.common.match_regex(">>", None, const.OPERATOR, const.OPERATOR)

    def test_divide_integer_assign(self):
        self.common.match_regex("\=", None, const.OPERATOR, const.OPERATOR)