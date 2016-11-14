import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestFunctionCallParse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_id_open_parenthesis_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_CALL, "x()", )

    def test_built_in_function_call_with_value(self):
        self.common.match_statement(const.FUNCTION_CALL, "cos(3)")

    def test_built_in_function_call_with_id(self):
        self.common.match_statement(const.FUNCTION_CALL, "chr(x)")

    def test_id_open_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_CALL, "x(y, z)")

    def test_id_open_parenthesis_value_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_CALL, "x(1)")

    def test_id_open_parenthesis_id_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_CALL, "x(y)")

    def test_id_dot_function_call(self):
        self.common.match_statement(const.FUNCTION_CALL, "z.x(y)")

    def test_function_call_dot_function_call(self):
        self.common.match_statement(const.FUNCTION_CALL, "z(i).x()")

    def test_id_open_parenthesis_id_equals_value_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_CALL, "x(y = 1)")

    def test_built_in_function_call_test(self):
        self.common.match_statement(const.FUNCTION_CALL, "wait(0, x.y().t(), a)")

    def test_built_in_function_call_with_id_dot_id(self):
        self.common.match_statement(const.FUNCTION_CALL, "wait(0, x.y)")

    def test_invalid_function_call_missing_parenthesis(self):
        self.common.status_error("x(const.FUNCTION_CALL, ")

    def test_invalid_function_call_extra_parenthesis(self):
        self.common.status_error("x(())")

    def test_invalid_function_call_semi_colon(self):
        self.common.status_error("x(a; b)")
