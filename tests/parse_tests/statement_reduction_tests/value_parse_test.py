import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestValueParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_id_operator_id(self):
        self.common.match_statement("x / y", const.VALUE)

    def test_value_operator_value(self):
        self.common.match_statement("1 / 1", const.VALUE)

    def test_value_operator_id(self):
        self.common.match_statement("1 / y", const.VALUE)

    def test_id_operator_value(self):
        self.common.match_statement("x / 1", const.VALUE)

    def test_id_operator_function_call(self):
        self.common.match_statement("x / y()", const.VALUE)

    def test_function_call_operator_id(self):
        self.common.match_statement("x() / y", const.VALUE)

    def test_value_operator_function_call(self):
        self.common.match_statement("1 / y()", const.VALUE)

    def test_function_call_operator_value(self):
        self.common.match_statement("x() / 1", const.VALUE)

    def test_function_call_operator_function_call(self):
        self.common.match_statement("x() / y()", const.VALUE)

    def test_id_plus_id(self):
        self.common.match_statement("x + y", const.VALUE)

    def test_id_plus_plus_id(self):
        self.common.match_statement("x + +y", const.VALUE)

    def test_id_plus_minus_id(self):
        self.common.match_statement("x + -y", const.VALUE)

    def test_value_plus_value(self):
        self.common.match_statement("1 + 1", const.VALUE)

    def test_value_plus_plus_value(self):
        self.common.match_statement("1 + +1", const.VALUE)

    def test_value_minus_plus_value(self):
        self.common.match_statement("1 - +1", const.VALUE)

    def test_value_plus_id(self):
        self.common.match_statement("1 + y", const.VALUE)

    def test_value_plus_plus_id(self):
        self.common.match_statement("1 + +y", const.VALUE)

    def test_value_plus_minus_id(self):
        self.common.match_statement("1 + -y", const.VALUE)

    def test_id_plus_value(self):
        self.common.match_statement("x + 1", const.VALUE)

    def test_id_plus_plus_value(self):
        self.common.match_statement("x + +1", const.VALUE)

    def test_id_plus_minus_value(self):
        self.common.match_statement("x + -1", const.VALUE)

    def test_id_plus_function_call(self):
        self.common.match_statement("x + y()", const.VALUE)

    def test_id_plus_plus_function_call(self):
        self.common.match_statement("x + +y()", const.VALUE)

    def test_id_plus_minus_function_call(self):
        self.common.match_statement("x + -y()", const.VALUE)

    def test_function_call_plus_id(self):
        self.common.match_statement("x() + y", const.VALUE)

    def test_function_call_plus_plus_id(self):
        self.common.match_statement("x() + +y", const.VALUE)

    def test_function_call_plus_minus_id(self):
        self.common.match_statement("x() + -y", const.VALUE)

    def test_value_plus_function_call(self):
        self.common.match_statement("1 + y()", const.VALUE)

    def test_value_plus_plus_function_call(self):
        self.common.match_statement("1 + +y()", const.VALUE)

    def test_value_plus_minus_function_call(self):
        self.common.match_statement("1 + -y()", const.VALUE)

    def test_function_call_plus_value(self):
        self.common.match_statement("x() + 1", const.VALUE)

    def test_function_call_plus_plus_value(self):
        self.common.match_statement("x() + +1", const.VALUE)

    def test_function_call_plus_minus_value(self):
        self.common.match_statement("x() + -1", const.VALUE)

    def test_function_call_plus_function_call(self):
        self.common.match_statement("x() + y()", const.VALUE)

    def test_function_call_plus_plus_function_call(self):
        self.common.match_statement("x() + +y()", const.VALUE)

    def test_function_call_plus_minus_function_call(self):
        self.common.match_statement("x() + -y()", const.VALUE)

    def test_id_minus_id(self):
        self.common.match_statement("x - y", const.VALUE)

    def test_id_minus_plus_id(self):
        self.common.match_statement("x - +y", const.VALUE)

    def test_id_minus_minus_id(self):
        self.common.match_statement("x - -y", const.VALUE)

    def test_value_minus_value(self):
        self.common.match_statement("1 - 1", const.VALUE)

    def test_value_plus_minus_value(self):
        self.common.match_statement("1 + -1", const.VALUE)

    def test_value_minus_minus_value(self):
        self.common.match_statement("1 - -1", const.VALUE)

    def test_value_minus_id(self):
        self.common.match_statement("1 - y", const.VALUE)

    def test_value_minus_plus_id(self):
        self.common.match_statement("1 - +y", const.VALUE)

    def test_value_minus_minus_id(self):
        self.common.match_statement("1 - -y", const.VALUE)

    def test_id_minus_value(self):
        self.common.match_statement("x - 1", const.VALUE)

    def test_id_minus_plus_value(self):
        self.common.match_statement("x - +1", const.VALUE)

    def test_id_minus_minus_value(self):
        self.common.match_statement("x - -1", const.VALUE)

    def test_id_minus_function_call(self):
        self.common.match_statement("x - y()", const.VALUE)

    def test_id_minus_plus_function_call(self):
        self.common.match_statement("x - +y()", const.VALUE)

    def test_id_minus_minus_function_call(self):
        self.common.match_statement("x - -y()", const.VALUE)

    def test_function_call_minus_id(self):
        self.common.match_statement("x() - y", const.VALUE)

    def test_function_call_minus_plus_id(self):
        self.common.match_statement("x() - +y", const.VALUE)

    def test_function_call_minus_minus_id(self):
        self.common.match_statement("x() - -y", const.VALUE)

    def test_value_minus_function_call(self):
        self.common.match_statement("1 - y()", const.VALUE)

    def test_value_minus_plus_function_call(self):
        self.common.match_statement("1 - +y()", const.VALUE)

    def test_value_minus_minus_function_call(self):
        self.common.match_statement("1 - -y()", const.VALUE)

    def test_function_call_minus_value(self):
        self.common.match_statement("x() - 1", const.VALUE)

    def test_function_call_minus_plus_value(self):
        self.common.match_statement("x() - +1", const.VALUE)

    def test_function_call_minus_minus_value(self):
        self.common.match_statement("x() - -1", const.VALUE)

    def test_function_call_minus_function_call(self):
        self.common.match_statement("x() - y()", const.VALUE)

    def test_function_call_minus_plus_function_call(self):
        self.common.match_statement("x() - +y()", const.VALUE)

    def test_function_call_minus_minus_function_call(self):
        self.common.match_statement("x() - -y()", const.VALUE)

    def test_open_parenthesis_value_close_parenthesis(self):
        self.common.match_statement("(1)", const.VALUE)

    def test_function_call_dot_id(self):
        self.common.match_statement("func_name().id", const.VALUE)

    # Only ID Test

    def test_open_parenthesis_id_close_parenthesis(self):
        self.common.match_statement("(x)", const.ID)

    def test_invalid_value_multiple_plus(self):
        self.common.exception_runner("+ + + + + + + + + +")

    def test_invalid_value_minus(self):
        self.common.exception_runner("3-")

    def test_invalid_value_idplus_while(self):
        self.common.exception_runner("a + while")
