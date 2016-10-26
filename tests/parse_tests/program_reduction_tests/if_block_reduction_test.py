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

    def test_if_statements_block(self):
        self._match("if x = 3\n x = 4\n end if",
                    [[const.IF_STATEMENT, const.BLOCK_STATEMENT, const.END_IF], [const.BLOCK_STATEMENT]])

    def test_if_then_statements_block(self):
        self._match("if x() then\n x = 4\n end if",
                    [[const.IF_STATEMENT, const.BLOCK_STATEMENT, const.END_IF], [const.BLOCK_STATEMENT]])

    def test_if_closed_endwhile(self):
        self._exception_runner("if function() then\n x = 4\n end while")

    def test_if_closed_endfor(self):
        self._exception_runner("if function() then\n x = 4\n end for")

    def test_if_with_else_if_closed_endfor(self):
        self._match("if x = 3 then\n x = 4\n else if x = 4\n x = 5\n end if",
                    [[const.IF_STATEMENT, const.VAR_AS, const.ELSE_IF_STATEMENT, const.BLOCK_STATEMENT, const.END_IF],
                     [const.IF_STATEMENT, const.VAR_AS, const.ELSE_IF_BLOCK, const.END_IF],
                     [const.IF_STATEMENT, const.BLOCK_STATEMENT, const.ELSE_IF_BLOCK, const.END_IF],
                     [const.IF_BLOCK, const.ELSE_IF_BLOCK, const.END_IF],
                     [const.BLOCK_STATEMENT]])

    def test_if_with_else_closed_endfor(self):
        self._match("if x = 3 then\n x = 4\n else\n x = 5\n end if",
                    [[const.IF_STATEMENT, const.VAR_AS, const.ELSE_STATEMENT, const.BLOCK_STATEMENT, const.END_IF],
                     [const.IF_STATEMENT, const.VAR_AS, const.END_IF],
                     [const.IF_STATEMENT, const.BLOCK_STATEMENT, const.END_IF],
                     [const.BLOCK_STATEMENT]])

    def test_if_with_else_if_and_ele_closed_endfor(self):
        self._match("if x = 3 then\n x = 4\n else if x = 4 then\n x = 5\nelse\n x = 6\n end if",
                    [[const.IF_STATEMENT, const.VAR_AS, const.ELSE_IF_STATEMENT, const.VAR_AS, const.ELSE_STATEMENT, const.BLOCK_STATEMENT, const.END_IF],
                     [const.IF_STATEMENT, const.VAR_AS, const.ELSE_IF_STATEMENT, const.VAR_AS, const.END_IF],
                     [const.IF_STATEMENT, const.VAR_AS, const.ELSE_IF_STATEMENT, const.BLOCK_STATEMENT, const.END_IF],
                     [const.IF_STATEMENT, const.VAR_AS, const.ELSE_IF_BLOCK, const.END_IF],
                     [const.IF_STATEMENT, const.BLOCK_STATEMENT, const.ELSE_IF_BLOCK, const.END_IF],
                     [const.IF_BLOCK, const.ELSE_IF_BLOCK, const.END_IF],
                     [const.BLOCK_STATEMENT]])

    def test_else_if_closed_endfor(self):
        self._exception_runner("if x = 3 then\n x = 4\n else\n x = 5\n end for")

    def test_else_if_closed_endwhile(self):
        self._exception_runner("if x = 3 then\n x = 4\n else\n x = 5\n end while")

    def test_incorrect_else(self):
        self._exception_runner("if x = 3 then\n x = 4\n else\n x = 5\nelse if x = 5\n x = 6\n end if")

    def test_incorrect_else_if(self):
        self._exception_runner("if x = 3 then\n x = 4\n else if\n x = 5\n end if")