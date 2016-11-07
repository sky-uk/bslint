import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestForBlockParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_for_block(self):
        self.common.match_program("for x=10 To 3 Step zz\nx()\n end for", const.BLOCK_STMT)

    def test_for_closed_for_endif(self):
        self.common.status_error("for x=10 To 3 Step zz\ni = 4\n end if")

    def test_for_closed_for_endwhile(self):
        self.common.status_error("for x=10 To 3 Step zz\ni = 4\n end while")

    def test_for_each_block(self):
        self.common.match_program("For Each char In x\nprint test\n end for", const.BLOCK_STMT)

    def test_for_each_closed_for_endif(self):
        self.common.status_error("For Each char In x\ni = 4\n end if")

    def test_for_each_closed_for_endwhile(self):
        self.common.status_error("For Each char In x\ni = 4\n end while")
