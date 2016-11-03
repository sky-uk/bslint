import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestParamParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_return(self):
        self.common.match_statement("return", const.RETURN_STMT)

    def test_return_value(self):
        self.common.match_statement("return 4", const.RETURN_STMT)

    def test_return_id(self):
        self.common.match_statement("return x", const.RETURN_STMT)

    def test_return_var_as(self):
        self.common.match_statement("return x = 3", const.RETURN_STMT)

    def test_return_function_call(self):
        self.common.match_statement("return b()", const.RETURN_STMT)

    def test_return_enumerable_object(self):
        self.common.match_statement("return []", const.RETURN_STMT)

    def test_invalid_param_value(self):
        self.common.status_error("function x(1 as Integer)")
