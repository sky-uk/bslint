import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestForEachParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_for_each_id_in_id(self):
        self.common.match_statement(const.FOR_EACH_STMT, "For Each n In aa")

    def test_for_each_id_in_func_call(self):
        self.common.match_statement(const.FOR_EACH_STMT, "For Each n In aa()")

    def test_for_each_id_in_value(self):
        self.common.match_statement(const.FOR_EACH_STMT, "For Each char In \"abc\"")

    def test_for_each_value_in_id(self):
        self.common.status_error("For Each 1 in num")

    def test_for_each_function_call_in_id(self):
        self.common.status_error("For Each x() in num")
