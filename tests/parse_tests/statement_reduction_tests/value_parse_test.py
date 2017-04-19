import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestValueParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_id_operator_id(self):
        self.common.match_statement(const.VALUE, "x / y")

    def test_value_operator_value(self):
        self.common.match_statement(const.VALUE, "1 / 1")

    def test_value_operator_id(self):
        self.common.match_statement(const.VALUE, "1 / y")

    def test_id_operator_value(self):
        self.common.match_statement(const.VALUE, "x / 1")

    def test_id_operator_function_call(self):
        self.common.match_statement(const.VALUE, "x / y()")

    def test_function_call_operator_id(self):
        self.common.match_statement(const.VALUE, "x() / y")

    def test_value_operator_function_call(self):
        self.common.match_statement(const.VALUE, "1 / y()")

    def test_function_call_operator_value(self):
        self.common.match_statement(const.VALUE, "x() / 1")

    def test_function_call_operator_function_call(self):
        self.common.match_statement(const.VALUE, "x() / y()")

    def test_id_plus_id(self):
        self.common.match_statement(const.VALUE, "x + y")

    def test_id_plus_plus_id(self):
        self.common.match_statement(const.VALUE, "x + +y")

    def test_id_plus_minus_id(self):
        self.common.match_statement(const.VALUE, "x + -y")

    def test_value_plus_value(self):
        self.common.match_statement(const.VALUE, "1 + 1")

    def test_value_plus_plus_value(self):
        self.common.match_statement(const.VALUE, "1 + +1")

    def test_value_minus_plus_value(self):
        self.common.match_statement(const.VALUE, "1 - +1")

    def test_value_plus_id(self):
        self.common.match_statement(const.VALUE, "1 + y")

    def test_value_plus_plus_id(self):
        self.common.match_statement(const.VALUE, "1 + +y")

    def test_value_plus_minus_id(self):
        self.common.match_statement(const.VALUE, "1 + -y")

    def test_id_plus_value(self):
        self.common.match_statement(const.VALUE, "x + 1")

    def test_id_plus_plus_value(self):
        self.common.match_statement(const.VALUE, "x + +1")

    def test_id_plus_minus_value(self):
        self.common.match_statement(const.VALUE, "x + -1")

    def test_id_plus_function_call(self):
        self.common.match_statement(const.VALUE, "x + y()")

    def test_id_plus_plus_function_call(self):
        self.common.match_statement(const.VALUE, "x + +y()")

    def test_id_plus_minus_function_call(self):
        self.common.match_statement(const.VALUE, "x + -y()")

    def test_function_call_plus_id(self):
        self.common.match_statement(const.VALUE, "x() + y")

    def test_function_call_plus_plus_id(self):
        self.common.match_statement(const.VALUE, "x() + +y")

    def test_function_call_plus_minus_id(self):
        self.common.match_statement(const.VALUE, "x() + -y")

    def test_value_plus_function_call(self):
        self.common.match_statement(const.VALUE, "1 + y()")

    def test_value_plus_plus_function_call(self):
        self.common.match_statement(const.VALUE, "1 + +y()")

    def test_value_plus_minus_function_call(self):
        self.common.match_statement(const.VALUE, "1 + -y()")

    def test_function_call_plus_value(self):
        self.common.match_statement(const.VALUE, "x() + 1")

    def test_function_call_plus_plus_value(self):
        self.common.match_statement(const.VALUE, "x() + +1")

    def test_function_call_plus_minus_value(self):
        self.common.match_statement(const.VALUE, "x() + -1")

    def test_function_call_plus_function_call(self):
        self.common.match_statement(const.VALUE, "x() + y()")

    def test_function_call_plus_plus_function_call(self):
        self.common.match_statement(const.VALUE, "x() + +y()")

    def test_function_call_plus_minus_function_call(self):
        self.common.match_statement(const.VALUE, "x() + -y()")

    def test_id_minus_id(self):
        self.common.match_statement(const.VALUE, "x - y")

    def test_id_minus_plus_id(self):
        self.common.match_statement(const.VALUE, "x - +y")

    def test_id_minus_minus_id(self):
        self.common.match_statement(const.VALUE, "x - -y")

    def test_value_minus_value(self):
        self.common.match_statement(const.VALUE, "1 - 1")

    def test_value_plus_minus_value(self):
        self.common.match_statement(const.VALUE, "1 + -1")

    def test_value_minus_minus_value(self):
        self.common.match_statement(const.VALUE, "1 - -1")

    def test_value_minus_id(self):
        self.common.match_statement(const.VALUE, "1 - y")

    def test_value_minus_plus_id(self):
        self.common.match_statement(const.VALUE, "1 - +y")

    def test_value_minus_minus_id(self):
        self.common.match_statement(const.VALUE, "1 - -y")

    def test_id_minus_value(self):
        self.common.match_statement(const.VALUE, "x - 1")

    def test_id_minus_plus_value(self):
        self.common.match_statement(const.VALUE, "x - +1")

    def test_id_minus_minus_value(self):
        self.common.match_statement(const.VALUE, "x - -1")

    def test_id_minus_function_call(self):
        self.common.match_statement(const.VALUE, "x - y()")

    def test_id_minus_plus_function_call(self):
        self.common.match_statement(const.VALUE, "x - +y()")

    def test_id_minus_minus_function_call(self):
        self.common.match_statement(const.VALUE, "x - -y()")

    def test_function_call_minus_id(self):
        self.common.match_statement(const.VALUE, "x() - y")

    def test_function_call_minus_plus_id(self):
        self.common.match_statement(const.VALUE, "x() - +y")

    def test_function_call_minus_minus_id(self):
        self.common.match_statement(const.VALUE, "x() - -y")

    def test_value_minus_function_call(self):
        self.common.match_statement(const.VALUE, "1 - y()")

    def test_value_minus_plus_function_call(self):
        self.common.match_statement(const.VALUE, "1 - +y()")

    def test_value_minus_minus_function_call(self):
        self.common.match_statement(const.VALUE, "1 - -y()")

    def test_function_call_minus_value(self):
        self.common.match_statement(const.VALUE, "x() - 1")

    def test_function_call_minus_plus_value(self):
        self.common.match_statement(const.VALUE, "x() - +1")

    def test_function_call_minus_minus_value(self):
        self.common.match_statement(const.VALUE, "x() - -1")

    def test_function_call_minus_function_call(self):
        self.common.match_statement(const.VALUE, "x() - y()")

    def test_function_call_minus_plus_function_call(self):
        self.common.match_statement(const.VALUE, "x() - +y()")

    def test_function_call_minus_minus_function_call(self):
        self.common.match_statement(const.VALUE, "x() - -y()")

    def test_open_parenthesis_value_close_parenthesis(self):
        self.common.match_statement(const.ID, "(1)")

    def test_open_parenthesis_plus_id_close_parenthesis(self):
        self.common.match_statement(const.ID, "(+y)")

    def test_open_parenthesis_minus_id_close_parenthesis(self):
        self.common.match_statement(const.ID, "(-y)")

    def test_open_parenthesis_plus_value_close_parenthesis(self):
        self.common.match_statement(const.ID, "(+1)")

    def test_open_parenthesis_minus_value_close_parenthesis(self):
        self.common.match_statement(const.ID, "(-1)")

    # Only ID Test

    def test_open_parenthesis_id_close_parenthesis(self):
        self.common.match_statement(const.ID, "(x)")

    def test_function_call_dot_id(self):
        self.common.match_statement(const.ID, "func_name().id")

    def test_invalid_value_multiple_plus(self):
        self.common.status_error("+ + + + + + + + + +")

    def test_invalid_value_minus(self):
        self.common.status_error("3-")

    def test_invalid_value_idplus_while(self):
        self.common.status_error("a + while")
