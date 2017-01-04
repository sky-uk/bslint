import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestIfBlockParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_if_statements_block(self):
        self.common.match_program(const.BLOCK_STMT, "if x = 3\n x = 4\n end if")

    def test_if_then_statements_block(self):
        self.common.match_program(const.BLOCK_STMT, "if x() then\n x = 4\n end if")

    def test_if_no_body(self):
        self.common.match_program(const.BLOCK_STMT, "if x() \n end if")

    def test_if_closed_endwhile(self):
        self.common.status_error("if function() then\n x = 4\n end while")

    def test_if_closed_endfor(self):
        self.common.status_error("if function() then\n x = 4\n end for")

    def test_if_elseif_endif(self):
        self.common.match_program(const.BLOCK_STMT, "if x = 3 then\n x = 4\n else if x = 4\n x = 5\n end if")

    def test_if_else_endif(self):
        self.common.match_program(const.BLOCK_STMT, "if x = 3 then\n x = 4\n else\n x = 5\n end if")

    def test_if_with_else_if_and_ele_closed_endfor(self):
        self.common.match_program(const.BLOCK_STMT,
                                  "if x = 3 then\n x = 4\n else if x = 4 then\n x = 5\nelse\n x = 6\n end if")

    def test_else_if_closed_endfor(self):
        self.common.status_error("if x = 3 then\n x = 4\n else\n x = 5\n end for")

    def test_else_if_closed_endwhile(self):
        self.common.status_error("if x = 3 then\n x = 4\n else\n x = 5\n end while")

    def test_incorrect_else(self):
        self.common.status_error("if x = 3 then\n x = 4\n else\n x = 5\nelse if x = 5\n x = 6\n end if")

    def test_incorrect_else_if(self):
        self.common.status_error("if x = 3 then\n x = 4\n else if\n x = 5\n end if")
