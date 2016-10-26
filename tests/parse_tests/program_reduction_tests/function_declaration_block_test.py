import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestMultiLineReductionParse(unittest.TestCase):
    def _match(self, str, expected_program_reduction):
        parser = Parser()
        result = parser.parse(str)
        self.assertEqual("Success", result["Status"])
        index = 0
        for expect in expected_program_reduction:
            self.assertEqual(expect, parser.line_reductions[index])
            index += 1

    def _exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def test_function_declaration_block(self):
        self._match("function x(y, z)\n?test\n end function",
                    [[const.FUNCTION_DECLARATION, const.BLOCK_STATEMENT, const.END_FUNCTION],
                     [const.BLOCK_STATEMENT]])

    def test_function_declaration_closed_for_endif(self):
        self._exception_runner("function x(y, z)\n?test\n end if")

    def test_function_declaration_closed_for_endwhile(self):
        self._exception_runner("function x(y, z)\n?test\n end while")
