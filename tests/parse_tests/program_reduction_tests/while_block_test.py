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

    def test_while_block(self):
        self._match("while x = 3\ni = 4\nendwhile",
                    [[const.WHILE_STATEMENT, const.BLOCK_STATEMENT, const.END_WHILE], [const.BLOCK_STATEMENT]])

    def test_while_closed_with_endfor(self):
        self._exception_runner("while x = 3\ni = 4\n end for")

    def test_while_closed_with_endif(self):
        self._exception_runner("while x = 3\ni = 4\n end if")