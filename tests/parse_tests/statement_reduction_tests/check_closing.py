import unittest

from bslint import constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestCheckClosingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_end_if(self):
        self.common.match_statement(const.END_IF, "endif")

    def test_end_if_space(self):
        self.common.match_statement(const.END_IF, "end if")

    def test_end_while(self):
        self.common.match_statement(const.END_WHILE, "endwhile")

    def test_end_while_space(self):
        self.common.match_statement(const.END_WHILE, "end while")

    def test_end_for(self):
        self.common.match_statement(const.END_FOR, "endfor")

    def test_end_for_space(self):
        self.common.match_statement(const.END_FOR, "end for")

    def test_end_sub(self):
        self.common.match_statement(const.END_FUNCTION, "endsub")

    def test_end_sub_space(self):
        self.common.match_statement(const.END_FUNCTION, "end sub")

    def test_end_function(self):
        self.common.match_statement(const.END_FUNCTION, "endfunction")

    def test_end_function_space(self):
        self.common.match_statement(const.END_FUNCTION, "end function")

    def test_end(self):
        self.common.match_statement(const.END, "end")
