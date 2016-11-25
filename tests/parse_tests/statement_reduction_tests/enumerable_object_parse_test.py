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

    def test_enumerable_object_with_built_in_func_as_key_and_id(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{type:x, b:2}")

    def test_enumerable_object_with_built_in_func_as_key_and_value(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{Chr:1, b:2}")

    def test_enumerable_object_with_built_in_func_as_key_and_func_call(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{len:x(), b:2}")

    def test_enumerable_object_with_built_in_func_as_key_and_enumerable_object(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{wait:{a:3}, b:2}")

    def test_enumerable_object_with_built_in_func_as_key_and_anon_func(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{wait:function () \n c=3 \n end function,\n b:2}")

    def test_enumerable_object_with_keyword_as_key_and_id(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{left:x, b:2}")

    def test_enumerable_object_with_keyword_as_key_and_value(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{left:1, b:2}")

    def test_enumerable_object_with_keyword_as_key_and_function_call(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{instr:x(), b:2}")

    def test_enumerable_object_with_keyword_as_key_and_enumerable_object(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{sleep:{p:23}, b:2}")

    def test_enumerable_object_with_keyword_as_key_and_anon_func(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{str:function () \n c=3 \n end function,\n b:2}")

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

    def test_open_enumerable_object_value_colon_enumerable_object(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\"help\":{c:3}}")

    def test_list_of_enumerable_objects(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "[{a:3, b:4},\n{a:3, b:4}]")

    def test_list_without_commas(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "[{a:3, b:4}\n{a:3, b:4}\n4]")

    def test_object_of_enumerable_objects(self):
        self.common.status_error("{{a:3, b:4},\n{a:3, b:4}}")

    def test_keyword_as_object_key(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\nnext: 3\n}")

    def test_keyword_as_object_key_with_object_as_value(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{\nnext: {data: \"NEXT_DATA\"}\n}")

    def test_keyword_as_function_call(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{next: func_name()}")

    def test_keyword_as_id(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{next: id}")

    def test_keyword_as_key_with_anonymous_function_as_val(self):
        self.common.match_statement(const.ENUMERABLE_OBJECT, "{next:function () \n c=3\nend function}")

    def test_invalid_associative_array_var_as(self):
        self.common.status_error("{x = 3}")

    def test_invalid_array_var_as(self):
        self.common.status_error("[y = 2]")

    def test_invalid_mismatched_array_braces(self):
        self.common.status_error("[}")
