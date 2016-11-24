import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestVariableAssignment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_value(self):
        self.common.match_statement(const.VAR_AS, "x = 3")

    def test_value_with_dot(self):
        self.common.match_statement(const.VAR_AS, "m.isRunning = false")

    def test_identifier(self):
        self.common.match_statement(const.VAR_AS, "x = y")

    def test_function_call(self):
        self.common.match_statement(const.VAR_AS, "x = y()")

    def test_empty_enumerable_object(self):
        self.common.match_statement(const.VAR_AS, "x = []")

    def test_enumerable_object(self):
        self.common.match_statement(const.VAR_AS, "x = {x:3}")

    def test_variable_assignment_with_plus_value(self):
        self.common.match_statement(const.VAR_AS, "x = +3")

    def test_variable_assignment_with_minus_value(self):
        self.common.match_statement(const.VAR_AS, "x = -3")

    def test_variable_assignment_with_plus_id(self):
        self.common.match_statement(const.VAR_AS, "x = +y")

    def test_variable_assignment_with_minus_id(self):
        self.common.match_statement(const.VAR_AS, "x = -y")

    def test_variable_assignment_with_plus_function_call(self):
        self.common.match_statement(const.VAR_AS, "x = +y()")

    def test_variable_assignment_with_minus_function_call(self):
        self.common.match_statement(const.VAR_AS, "x = -y()")

    def test_open_parenthesis_variable_assignment_close_parenthesis(self):
        self.common.match_statement(const.VAR_AS, "(x = 1)")

    def test_variable_declaration_with_reduction(self):
        self.common.match_statement(const.VAR_AS, 'x = 3 + 2')

    def test_variable_declaration_with_multiple_reduction(self):
        self.common.match_statement(const.VAR_AS, 'x = 3 + 2 - 5')

    def test_variable_declaration_with_reduction_and_parenthesis(self):
        self.common.match_statement(const.VAR_AS, 'x = (3 + 2)')

    def test_assignment_to_array_key(self):
        self.common.match_statement(const.VAR_AS, 'x[y] = (3 + 2)')

    def test_sub_id_open_parenthesis_var_as_as_type_close_parenthesis(self):
        self.common.match_statement(const.VAR_AS, "c = x(y=3, a, b[3,5])")

    def test_id_equals_id_with_parenthesis(self):
        self.common.match_statement(const.VAR_AS, "x = (y)")

    def test_id_equals_value_with_parenthesis(self):
        self.common.match_statement(const.VAR_AS, "x = (6)")

    def test_invalid_variable_assignment_while(self):
        self.common.status_error("x = while")

    def test_invalid_variable_assignment_extra_equals(self):
        self.common.status_error("x == 3")

    def test_invalid_variable_assignment_incorrect_order(self):
        self.common.status_error("3 = x")
