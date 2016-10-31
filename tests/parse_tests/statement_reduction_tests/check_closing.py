import unittest

from bslint import constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestCheckClosingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_end_if(self):
        self.common.match_statement("endif", const.END_IF)

    def test_end_if_space(self):
        self.common.match_statement("end if", const.END_IF)

    def test_end_while(self):
        self.common.match_statement("endwhile", const.END_WHILE)

    def test_end_while_space(self):
        self.common.match_statement("end while", const.END_WHILE)

    def test_end_for(self):
        self.common.match_statement("endfor", const.END_FOR)

    def test_end_for_space(self):
        self.common.match_statement("end for", const.END_FOR)

    def test_end_sub(self):
        self.common.match_statement("endsub", const.END_FUNCTION)

    def test_end_sub_space(self):
        self.common.match_statement("end sub", const.END_FUNCTION)

    def test_end_function(self):
        self.common.match_statement("endfunction", const.END_FUNCTION)

    def test_end_function_space(self):
        self.common.match_statement("end function", const.END_FUNCTION)

    def test_end(self):
        self.common.match_statement("end", const.END)
