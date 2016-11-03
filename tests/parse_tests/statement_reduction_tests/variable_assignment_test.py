import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestVariableAssignment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_value(self):
        self.common.match_statement("jack = 3", const.VAR_AS)

    def test_value_with_dot(self):
        self.common.match_statement("m.isRunning = false", const.VAR_AS)

    def test_identifier(self):
        self.common.match_statement("x = y", const.VAR_AS)

    def test_function_call(self):
        self.common.match_statement("x = y()", const.VAR_AS)

    def test_empty_enumerable_object(self):
        self.common.match_statement("x = []", const.VAR_AS)

    def test_enumerable_object(self):
        self.common.match_statement("x = {x:3}", const.VAR_AS)

    def test_variable_assignment_with_plus_value(self):
        self.common.match_statement("x = +3", const.VAR_AS)

    def test_variable_assignment_with_minus_value(self):
        self.common.match_statement("x = -3", const.VAR_AS)

    def test_variable_assignment_with_plus_id(self):
        self.common.match_statement("x = +y", const.VAR_AS)

    def test_variable_assignment_with_minus_id(self):
        self.common.match_statement("x = -y", const.VAR_AS)

    def test_variable_assignment_with_plus_function_call(self):
        self.common.match_statement("x = +y()", const.VAR_AS)

    def test_variable_assignment_with_minus_function_call(self):
        self.common.match_statement("x = -y()", const.VAR_AS)

    def test_open_parenthesis_variable_assignment_close_parenthesis(self):
        self.common.match_statement("(x = 1)", const.VAR_AS)

    def test_variable_declaration_with_reduction(self):
        self.common.match_statement('x = 3 + 2', const.VAR_AS)

    def test_variable_declaration_with_multiple_reduction(self):
        self.common.match_statement('x = 3 + 2 - 5', const.VAR_AS)

    def test_variable_declaration_with_reduction_and_parenthesis(self):
        self.common.match_statement('x = (3 + 2)', const.VAR_AS)

    def test_assignment_to_array_key(self):
        self.common.match_statement('x[y] = (3 + 2)', const.VAR_AS)

    def test_invalid_variable_assignment_while(self):
        self.common.status_error("jack = while")

    def test_invalid_variable_assignment_extra_equals(self):
        self.common.status_error("jack == 3")

    def test_invalid_variable_assignment_incorrect_order(self):
        self.common.status_error("3 = jack")
