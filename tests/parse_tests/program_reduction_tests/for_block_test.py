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

    def test_for_block(self):
        self.common.match_program("for x=10 To 3 Step zz\nx()\n end for", const.BLOCK_STATEMENT)

    def test_for_closed_for_endif(self):
        self.common.exception_runner("for x=10 To 3 Step zz\ni = 4\n end if")

    def test_for_closed_for_endwhile(self):
        self.common.exception_runner("for x=10 To 3 Step zz\ni = 4\n end while")

    def test_for_each_block(self):
        self.common.match_program("For Each char In x\nprint test\n end for", const.BLOCK_STATEMENT)

    def test_for_each_closed_for_endif(self):
        self.common.exception_runner("For Each char In x\ni = 4\n end if")

    def test_for_each_closed_for_endwhile(self):
        self.common.exception_runner("For Each char In x\ni = 4\n end while")