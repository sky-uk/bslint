import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser
from tests.resources.common.test_methods import CommonMethods as Common


class TestMultiLineReductionParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def _exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def test_function_declaration_block(self):
        self.common.match_program("function x(y, z)\n?test\n end function", const.BLOCK_STATEMENT)

    def test_function_declaration_closed_for_endif(self):
        self.common.exception_runner("function x(y, z)\n?test\n end if")

    def test_function_declaration_closed_for_endwhile(self):
        self.common.exception_runner("function x(y, z)\n?test\n end while")
