import unittest
import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestArgumentParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_open_enumerable_object_no_commas(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{a:1\n b:2}")

    def test_open_enumerable_object_no_commas_all_new_lines(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\na:1\n b:2\n}")

    def test_open_enumerable_object_no_commas_start_new_lines(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\na:1\n b:2}")

    def test_open_enumerable_object_commas(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{a:1,\n b:2}")

    def test_open_enumerable_object_commas_all_new_lines(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\na:1,\n b:2\n}")

    def test_open_enumerable_object_commas_start_new_lines(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\na:1,\n b:2}")

    def test_open_enumerable_object_mix_commas_all_new_lines(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\na:1\n b:2,\nc:3}")

    def test_open_curly_bracket_close_curly_bracket(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{}")

    def test_open_enumerable_object_single_values(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{a:1}")

    def test_open_enumerable_object_two_values(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{a:1, b:2}")

    def test_open_enumerable_object_value_function_call(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{a: m.id(), b: m.id()}")

    def test_open_square_bracket_close_square_bracket(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "[]")

    def test_open_square_bracket_value_close_square_bracket(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "[5]")

    def test_open_square_bracket_value_comma_id_close_square_bracket(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "[5, x]")

    def test_open_square_bracket_function_call_close_square_bracket(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "[x()]")

    def test_id_anonymous_function_block(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{x:function () \n c=3\nend function}")

    def test_value_anonymous_function_block(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{3:function () \n c=3\nend function}")

    def test_open_enumerable_object_value_colon_value(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\"help\":1}")

    def test_invalid_associative_array_var_as(self):
        self.common.status_error("{x = 3}")

    def test_invalid_array_var_as(self):
        self.common.status_error("[y = 2]")

    def test_invalid_mismatched_array_braces(self):
        self.common.status_error("[}")
