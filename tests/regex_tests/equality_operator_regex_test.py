import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestEqualityOperatorRegex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_not_equals(self):
        self.common.match_regex("<>", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_less_than_or_equal(self):
        self.common.match_regex("<=", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_less_than_or_equal_sec(self):
        self.common.match_regex("=<", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_greater_than_or_equal(self):
        self.common.match_regex(">=", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_greater_than_or_equal_sec(self):
        self.common.match_regex("=>", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_greater_than(self):
        self.common.match_regex(">", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_less_than(self):
        self.common.match_regex("<", 0, const.OPERATOR, const.COMPARISON_OPERATOR)

    def test_mod(self):
        self.common.match_regex("MOD", 1, const.KEYWORD, const.KEYWORD)

    def test_not(self):
        self.common.match_regex("NOT", 1, const.KEYWORD, const.NOT)

    def test_and(self):
        self.common.match_regex("AND", 1, const.KEYWORD, const.AND)

    def test_or(self):
        self.common.match_regex("OR", 1, const.KEYWORD, const.OR)