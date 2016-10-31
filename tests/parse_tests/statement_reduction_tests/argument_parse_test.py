import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestArgumentParse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_argument_comma_argument(self):
        self.common.match_statement("a(x, 1, y, 2)", const.FUNCTION_CALL)

    def test_value_comma_value(self):
        self.common.match_statement("a(1, 2)", const.FUNCTION_CALL)

    def test_id_comma_id(self):
        self.common.match_statement("a(x, y)", const.FUNCTION_CALL)

    def test_value_comma_argument(self):
        self.common.match_statement("a(2, 1, y)", const.FUNCTION_CALL)

    def test_id_comma_argument(self):
        self.common.match_statement("a(x, y, 2)", const.FUNCTION_CALL)

    def test_id_comma_value(self):
        self.common.match_statement("a(x, 1)", const.FUNCTION_CALL)

    def test_value_comma_id(self):
        self.common.match_statement("a(2, y)", const.FUNCTION_CALL)

    def test_function_call(self):
        self.common.match_statement("a(b())", const.FUNCTION_CALL)

    def test_invalid_argument_while(self):
        self.common.exception_runner("x(while, 1)")

    def test_invalid_argument_minus(self):
        self.common.exception_runner("x(-)")

    def test_invalid_argument_comment(self):
        self.common.exception_runner("x(')")
