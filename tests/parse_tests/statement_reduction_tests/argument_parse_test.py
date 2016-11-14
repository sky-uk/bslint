import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestArgumentParse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_argument_comma_argument(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(x, 1, y, 2)")

    def test_value_comma_value(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(1, 2)")

    def test_id_comma_id(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(x, y)")

    def test_value_comma_argument(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(2, 1, y)")

    def test_id_comma_argument(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(x, y, 2)")

    def test_id_comma_value(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(x, 1)")

    def test_value_comma_id(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(2, y)")

    def test_function_call(self):
        self.common.match_statement(const.FUNCTION_CALL, "a(b())")

    def test_invalid_argument_while(self):
        self.common.status_error("x(while, 1)")

    def test_invalid_argument_minus(self):
        self.common.status_error("x(-)")

    def test_invalid_argument_comment(self):
        self.common.status_error("x(')")
