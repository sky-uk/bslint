import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser
from tests.resources.common.test_methods import CommonMethods as Common


class TestIfParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_if_with_function_call_and_value_id(self):
        self.common.match_statement("if func_name(msg) = \"roVideoPlayerEvent\"", const.IF_STMT)

    def test_if_with_var_as_id(self):
        self.common.match_statement("if x = 3", const.IF_STMT)

    def test_if_with_function_call_id(self):
        self.common.match_statement("if test(param)", const.IF_STMT)

    def test_if_with_complex_function_call(self):
        self.common.match_statement("if msg.isFullResult()", const.IF_STMT)

    def test_if_with_value(self):
        self.common.match_statement("if msg.isFullResult()", const.IF_STMT)

    def test_if_with_value_equals_value(self):
        self.common.match_statement("if 3 = 3", const.IF_STMT)

    def test_if_with_value_equals_id(self):
        self.common.match_statement("if 3 = x", const.IF_STMT)

    def test_if_with_value_equals_function_call(self):
        self.common.match_statement("if 3 = test()", const.IF_STMT)

    def test_if_with_numeric_value(self):
        self.common.match_statement("if 3", const.IF_STMT)

    def test_if_with_id(self):
        self.common.match_statement("if x", const.IF_STMT)

    def test_if_with_anonymous_function(self):
        self.common.match_statement("if Function()", const.IF_STMT)

    def test_if_with_function_call_and_value_id_then(self):
        self.common.match_statement("if func_name(msg) = \"roVideoPlayerEvent\" then", const.IF_STMT)

    def test_if_with_var_as_id_then(self):
        self.common.match_statement("if x = 3 then", const.IF_STMT)

    def test_else_if_with_value_equals_id(self):
        self.common.match_statement("else if 3 = x", const.ELSE_IF_STMT)

    def test_else_if_with_numeric_value(self):
        self.common.match_statement("else if 3", const.ELSE_IF_STMT)

    def test_else_if_with_id(self):
        self.common.match_statement("else if x", const.ELSE_IF_STMT)

    def test_else_if_with_anonymous_function(self):
        self.common.match_statement("else if Function()", const.ELSE_IF_STMT)

    def test_if_with_value_equals_value_then(self):
        self.common.match_statement("else if 3 = 3 then", const.ELSE_IF_STMT)

    def test_if_with_value_equals_id_then(self):
        self.common.match_statement("else if 3 = x then", const.ELSE_IF_STMT)

    def test_if_with_numeric_value_then(self):
        self.common.match_statement("else if 3 then", const.ELSE_IF_STMT)

    def test_if_then_no_end_if_func_call(self):
        self.common.match_statement("if requiresUpdate then showRequiresUpdateScreen()", const.BLOCK_STMT)

    def test_else_if_then_no_end_if_func_call(self):
        self.common.match_statement("elseif requiresUpdate then showRequiresUpdateScreen()", const.BLOCK_STMT)

    def test_else_if_then_no_end_if_var_as(self):
        self.common.match_statement("elseif requiresUpdate then c = 3", const.BLOCK_STMT)

    def test_if_then_no_end_if_var_as(self):
        self.common.match_statement("if requiresUpdate then c = 3", const.BLOCK_STMT)

    def test_else(self):
        self.common.match_statement("else", const.ELSE_STMT)

    def test_if_with_function_declaration_fails(self):
        self.common.status_error("if function x()")

    def test_if_with_print_fails(self):
        self.common.status_error("if print x")

    def test_else_if_with_function_declaration_fails(self):
        self.common.status_error("else if +")

    def test_else_if_with_print_fails(self):
        self.common.status_error("else if =")


