import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestParamParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_id_as_type(self):
        self.common.match_statement("function x(y as Object)", const.FUNCTION_DECLARATION)

    def test_var_as_as_type(self):
        self.common.match_statement('sub x(y = "test" as String)', const.FUNCTION_DECLARATION)

    def test_param_comma_param(self):
        self.common.match_statement("function x(y as Object, z as Double)", const.FUNCTION_DECLARATION)

    def test_invalid_param_value(self):
        self.common.exception_runner("function x(1 as Integer)")

    def test_invalid_param_while(self):
        self.common.exception_runner("function x(while)")

    def test_invalid_param_plus(self):
        self.common.exception_runner("function x(+)")
