import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestIfParse(unittest.TestCase):
    def _match(self, str, expected):
        parser = Parser()
        result = parser.parse(str)
        self.assertEqual("Success", result["Status"])
        index = 0
        for expect in expected:
            self.assertEqual(expect, parser.all_statements[index])
            index += 1

    def _exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_if_with_function_call_and_value_id(self):
        self._match("if func_name(msg) = \"roVideoPlayerEvent\"", [
            [const.IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE],
            [const.IF_STATEMENT]])

    def test_if_with_var_as_id(self):
        self._match("if x = 3", [[const.IF, const.VAR_AS], [const.IF_STATEMENT]])

    def test_if_with_function_call_id(self):
        self._match("if test(param)", [[const.IF, const.FUNCTION_CALL], [const.IF_STATEMENT]])

    def test_if_with_complex_function_call(self):
        self._match("if msg.isFullResult()",
                    [[const.IF, const.ID, const.DOT, const.FUNCTION_CALL],
                     [const.IF, const.FUNCTION_CALL],
                     [const.IF_STATEMENT]])

    def test_if_with_value(self):
        self._match("if msg.isFullResult()",
                    [[const.IF, const.ID, const.DOT, const.FUNCTION_CALL],
                     [const.IF, const.FUNCTION_CALL],
                     [const.IF_STATEMENT]])

    def test_if_with_value_equals_value(self):
        self._match("if 3 = 3", [[const.IF_STATEMENT]])

    def test_if_with_value_equals_id(self):
        self._match("if 3 = x", [[const.IF_STATEMENT]])

    def test_if_with_numeric_value(self):
        self._match("if 3", [[const.IF_STATEMENT]])

    def test_if_with_id(self):
        self._match("if x", [[const.IF_STATEMENT]])

    def test_if_with_anonymous_function(self):
        self._match("if Function()", [[const.IF, const.ANONYMOUS_FUNCTION_DECLARATION], [const.IF_STATEMENT]])

    def test_if_with_function_call_and_value_id_then(self):
        self._match("if func_name(msg) = \"roVideoPlayerEvent\" then",
                    [[const.IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE, const.THEN], [const.IF_STATEMENT]])

    def test_if_with_var_as_id_then(self):
        self._match("if x = 3 then", [[const.IF, const.VAR_AS, const.THEN], [const.IF_STATEMENT]])

    def test_else_if_with_value_equals_id(self):
        self._match("else if 3 = x", [[const.ELSE_IF_STATEMENT]])

    def test_else_if_with_numeric_value(self):
        self._match("else if 3", [[const.ELSE_IF_STATEMENT]])

    def test_else_if_with_id(self):
        self._match("else if x", [[const.ELSE_IF_STATEMENT]])

    def test_else_if_with_anonymous_function(self):
        self._match("else if Function()", [[const.ELSE_IF, const.ANONYMOUS_FUNCTION_DECLARATION], [const.ELSE_IF_STATEMENT]])

    def test_if_with_value_equals_value_then(self):
        self._match("else if 3 = 3 then", [[const.ELSE_IF_STATEMENT]])

    def test_if_with_value_equals_id_then(self):
        self._match("else if 3 = x then", [[const.ELSE_IF_STATEMENT]])

    def test_if_with_numeric_value_then(self):
        self._match("else if 3 then", [[const.ELSE_IF_STATEMENT]])

    def test_else(self):
        self._match("else", [[const.ELSE_STATEMENT]])

    def test_if_with_function_declaration_fails(self):
        self._exception_runner("if function x()")

    def test_if_with_print_fails(self):
        self._exception_runner("if print x")

    def test_else_if_with_function_declaration_fails(self):
        self._exception_runner("else if +")

    def test_else_if_with_print_fails(self):
        self._exception_runner("else if =")


