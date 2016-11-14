import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestExitParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_exit_while(self):
        self.common.match_statement(const.EXIT_STMT, "exit while")

    def test_exit_for(self):
        self.common.match_statement(const.EXIT_STMT, "exit for")

    def test_exit_if(self):
        self.common.status_error("exit if")
