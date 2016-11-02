import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestMultiLineReductionParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_function_declaration_block(self):
        self.common.match_program("function x(y, z)\n?test\n end function", const.BLOCK_STATEMENT)

    def test_function_declaration_closed_for_endif(self):
        self.common.status_error("function x(y, z)\n?test\n end if")

    def test_function_declaration_closed_for_endwhile(self):
        self.common.status_error("function x(y, z)\n?test\n end while")
