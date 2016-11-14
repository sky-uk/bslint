import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestReturnParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_return(self):
        self.common.match_statement(const.RETURN_STMT, "return")

    def test_return_value(self):
        self.common.match_statement(const.RETURN_STMT, "return 4")

    def test_return_id(self):
        self.common.match_statement(const.RETURN_STMT, "return x")

    def test_return_var_as(self):
        self.common.match_statement(const.RETURN_STMT, "return x = 3")

    def test_return_function_call(self):
        self.common.match_statement(const.RETURN_STMT, "return b()")

    def test_return_enumerable_object(self):
        self.common.match_statement(const.RETURN_STMT, "return []")

    def test_invalid_param_value(self):
        self.common.status_error("function x(1 as Integer)")
