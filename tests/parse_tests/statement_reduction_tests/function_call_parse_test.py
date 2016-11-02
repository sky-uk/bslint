import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestFunctionCallParse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_id_open_parenthesis_close_parenthesis(self):
        self.common.match_statement("x()", const.FUNCTION_CALL)

    def test_built_in_function_call_with_value(self):
        self.common.match_statement("cos(3)", const.FUNCTION_CALL)

    def test_built_in_function_call_with_id(self):
        self.common.match_statement("chr(x)", const.FUNCTION_CALL)

    def test_id_open_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement("x(y, z)", const.FUNCTION_CALL)

    def test_id_open_parenthesis_value_close_parenthesis(self):
        self.common.match_statement("x(1)", const.FUNCTION_CALL)

    def test_id_open_parenthesis_id_close_parenthesis(self):
        self.common.match_statement("x(y)", const.FUNCTION_CALL)

    def test_id_dot_function_call(self):
        self.common.match_statement("z.x(y)", const.FUNCTION_CALL)

    def test_function_call_dot_function_call(self):
        self.common.match_statement("z(i).x()", const.FUNCTION_CALL)

    def test_id_open_parenthesis_id_equals_value_close_parenthesis(self):
        self.common.match_statement("x(y = 1)", const.FUNCTION_CALL)

    def test_built_in_function_call_test(self):
        self.common.match_statement("wait(0, x.y())", const.FUNCTION_CALL)

    def test_built_in_function_call_with_id_dot_id(self):
        self.common.match_statement("wait(0, x.y)", const.FUNCTION_CALL)

    def test_invalid_function_call_missing_parenthesis(self):
        self.common.status_error("x(")

    def test_invalid_function_call_extra_parenthesis(self):
        self.common.status_error("x(())")
