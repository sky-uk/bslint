import unittest
import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestArgumentParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_open_curly_bracket_close_curly_bracket(self):
        self.common.match_statement("{}", const.ENUMERABLE_OBJECT)

    def test_open_enumerable_object_single_values(self):
        self.common.match_statement("{a:1}", const.ENUMERABLE_OBJECT)

    def test_open_enumerable_object_two_values(self):
        self.common.match_statement("{a:1, b:2}", const.ENUMERABLE_OBJECT)

    def test_open_enumerable_object_value_function_call(self):
        self.common.match_statement("{a: m.id(), b: m.id()}", const.ENUMERABLE_OBJECT)

    def test_open_square_bracket_close_square_bracket(self):
        self.common.match_statement("[]", const.ENUMERABLE_OBJECT)

    def test_open_square_bracket_value_close_square_bracket(self):
        self.common.match_statement("[5]", const.ENUMERABLE_OBJECT)

    def test_open_square_bracket_value_comma_id_close_square_bracket(self):
        self.common.match_statement("[5, x]", const.ENUMERABLE_OBJECT)

    def test_invalid_associative_array_var_as(self):
        self.common.status_error("{x = 3}")

    def test_invalid_array_var_as(self):
        self.common.status_error("[y = 2]")

    def test_invalid_mismatched_array_braces(self):
        self.common.status_error("[}")
