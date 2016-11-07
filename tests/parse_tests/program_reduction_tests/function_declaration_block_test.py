import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestFunctionDeclarationBlockParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_function_declaration_block(self):
        self.common.match_program("function x(y, z)\n?test\n end function", const.BLOCK_STMT)

    def test_function_declaration_with_return_block(self):
        self.common.match_program("function x(y, z)\nx = 3\n return x\nend function", const.BLOCK_STMT)

    def test_function_declaration_closed_for_endif(self):
        self.common.status_error("function x(y, z)\n?test\n end if")

    def test_function_declaration_closed_for_endwhile(self):
        self.common.status_error("function x(y, z)\n?test\n end while")
