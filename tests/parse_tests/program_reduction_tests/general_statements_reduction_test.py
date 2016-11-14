import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestGeneralStatementsReductionParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_var_as_var_as(self):
        self.common.match_program(const.BLOCK_STMT, "x = 3\n y = 5")

    def test_var_as_function_call(self):
        self.common.match_program(const.BLOCK_STMT, "x = 3\n y()")

    def test_var_as_print(self):
        self.common.match_program(const.BLOCK_STMT, "x = 3\n print 5")

    def test_var_as_block(self):
        self.common.match_program(const.BLOCK_STMT, "x = 3\n print 5\n print 65")
