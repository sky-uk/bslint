import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestForParse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_for_value_no_step(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To 3")

    def test_for_id_no_step(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y")

    def test_for_function_call_no_step(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y()")

    def test_for_value_step_value(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To 3 Step 2")

    def test_for_id_step_value(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y Step 2")

    def test_for_function_call_step_value(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y() Step 2")

    def test_for_value_step_id(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To 3 Step zz")

    def test_for_id_step_id(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y Step zz")

    def test_for_function_call_step_id(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y() Step zz")

    def test_for_value_step_function_call(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To 3 Step zz()")

    def test_for_id_step_function_call(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y Step zz()")

    def test_for_function_call_step_function_call(self):
        self.common.match_statement(const.FOR_STMT, "for x=10 To y() Step zz()")

    def test_invalid_for_statement_at_var_as(self):
        self.common.status_error("for ) To 3")

    def test_invalid_for_statement_at_to(self):
        self.common.status_error("for x=10 To ) Step 4")

    def test_invalid_for_statement_at_step(self):
        self.common.status_error("for x=1 To 3 Step )")
