import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestWhileParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_while_value(self):
        self.common.match_statement("while true", const.WHILE_STMT)

    def test_while_plus_value(self):
        self.common.match_statement("while + 3", const.WHILE_STMT)

    def test_while_minus_value(self):
        self.common.match_statement("while - 3", const.WHILE_STMT)

    def test_while_id(self):
        self.common.match_statement("while x", const.WHILE_STMT)

    def test_while_plus_id(self):
        self.common.match_statement("while +x", const.WHILE_STMT)

    def test_while_minus_id(self):
        self.common.match_statement("while -x", const.WHILE_STMT)

    def test_while_var_as(self):
        self.common.match_statement("while x = 3", const.WHILE_STMT)

    def test_while_function_call(self):
        self.common.match_statement("while x()", const.WHILE_STMT)

    def test_while_plus_function_call(self):
        self.common.match_statement("while +x()", const.WHILE_STMT)

    def test_while_minus_function_call(self):
        self.common.match_statement("while -x()", const.WHILE_STMT)

    def test_invalid_while_parenthesis(self):
        self.common.status_error("while )")

    def test_invalid_while_for(self):
        self.common.status_error("while (for)")

    def test_invalid_while_end_while(self):
        self.common.status_error("while endwhile")
