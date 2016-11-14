import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestFunctionDeclarationParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_function_id_open_parenthesis_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "function x()")

    def test_function_declaration_as_void(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "function x() as Void")

    def test_function_declaration_as_boolean(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "function x() as Boolean")

    def test_function_id_open_parenthesis_parameter_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "function x(y as Object)")

    def test_function_id_open_parenthesis_idclose_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "function x(y)")

    def test_function_id_open_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "function x(y, z)")

    def test_sub_id_open_parenthesis_value_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "sub x()")

    def test_sub_id_open_parenthesis_parameter_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "sub x(y as String)")

    def test_sub_id_open_parenthesis_idclose_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "sub x(y)")

    def test_sub_id_open_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement(const.FUNCTION_DECLARATION, "sub x(y, z)")

    def test_sub_id_open_parenthesis_var_as_close_parenthesis(self):
        self.common.match_statement("sub x(y=3)", const.FUNCTION_DECLARATION)

    def test_sub_id_open_parenthesis_var_as_as_type_close_parenthesis(self):
        self.common.match_statement("sub x(y=3 as Integer)", const.FUNCTION_DECLARATION)

    def test_anonymous_sub_id_open_parenthesis_value_close_parenthesis(self):
        self.common.match_statement(const.ANONYMOUS_FUNCTION_DECLARATION, "sub ()")

    def test_anonymous_id_open_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement(const.ANONYMOUS_FUNCTION_DECLARATION, "function (y, z)")

    def test_invalid_function_declaraion_value(self):
        self.common.status_error("function 1()")

    def test_invalid_function_declaraion_missing_parenthesis(self):
        self.common.status_error("function x(")

    def test_invalid_function_declaraion_extra_parenthesis(self):
        self.common.status_error("function x(())")
