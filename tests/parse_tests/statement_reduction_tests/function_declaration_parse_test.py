import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestFunctionDeclarationParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_function_idopen_parenthesis_close_parenthesis(self):
        self.common.match_statement("function x()", const.FUNCTION_DECLARATION)

    def test_function_idopen_parenthesis_parameter_close_parenthesis(self):
        self.common.match_statement("function x(y as Object)", const.FUNCTION_DECLARATION)

    def test_function_idopen_parenthesis_idclose_parenthesis(self):
        self.common.match_statement("function x(y)", const.FUNCTION_DECLARATION)

    def test_function_idopen_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement("function x(y, z)", const.FUNCTION_DECLARATION)

    def test_sub_idopen_parenthesis_value_close_parenthesis(self):
        self.common.match_statement("sub x()", const.FUNCTION_DECLARATION)

    def test_sub_idopen_parenthesis_parameter_close_parenthesis(self):
        self.common.match_statement("sub x(y as String)", const.FUNCTION_DECLARATION)

    def test_sub_idopen_parenthesis_idclose_parenthesis(self):
        self.common.match_statement("sub x(y)", const.FUNCTION_DECLARATION)

    def test_sub_idopen_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement("sub x(y, z)", const.FUNCTION_DECLARATION)

    def test_anonymous_sub_idopen_parenthesis_value_close_parenthesis(self):
        self.common.match_statement("sub ()", const.ANONYMOUS_FUNCTION_DECLARATION)

    def test_anonymous_idopen_parenthesis_argument_close_parenthesis(self):
        self.common.match_statement("function (y, z)", const.ANONYMOUS_FUNCTION_DECLARATION)

    def test_invalid_function_declaraion_value(self):
        self.common.exception_runner("function 1()")

    def test_invalid_function_declaraion_missing_parenthesis(self):
        self.common.exception_runner("function x(")

    def test_invalid_function_declaraion_extra_parenthesis(self):
        self.common.exception_runner("function x(())")
