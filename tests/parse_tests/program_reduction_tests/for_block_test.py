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

    def test_for_block(self):
        self._match("for x=10 To 3 Step zz\nx()\n end for",
                    [[const.FOR_STATEMENT, const.BLOCK_STATEMENT, const.END_FOR],
                     [const.BLOCK_STATEMENT]])

    def test_for_closed_for_endif(self):
        self._exception_runner("for x=10 To 3 Step zz\ni = 4\n end if")

    def test_for_closed_for_endwhile(self):
        self._exception_runner("for x=10 To 3 Step zz\ni = 4\n end while")

    def test_for_each_block(self):
        self._match("For Each char In x\nprint test\n end for",
                    [[const.FOR_EACH_STATEMENT, const.BLOCK_STATEMENT, const.END_FOR],
                     [const.BLOCK_STATEMENT]])

    def test_for_each_closed_for_endif(self):
        self._exception_runner("For Each char In x\ni = 4\n end if")

    def test_for_each_closed_for_endwhile(self):
        self._exception_runner("For Each char In x\ni = 4\n end while")