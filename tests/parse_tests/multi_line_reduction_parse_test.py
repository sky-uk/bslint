import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestMultiLineReductionParse(unittest.TestCase):
    def _match(self, str, expected_stmt_production, expected_program_reduction):
        parser = Parser()
        result = parser.parse(str)
        self.assertEqual("Success", result["Status"])
        index = 0
        for expect in expected_program_reduction:
            self.assertEqual(expect, parser.line_reductions[index])
            index += 1
        index = 0
        for expect in expected_stmt_production:
            self.assertEqual(expect, parser.all_statements[index])
            index += 1

    def test_var_as_var_as(self):
        self._match("x = 3\n y = 5", [[const.VAR_AS], [const.VAR_AS]], [[const.BLOCK_STATEMENT]])

    def test_var_as_function_call(self):
        self._match("x = 3\n y()", [[const.VAR_AS], [const.FUNCTION_CALL]], [[const.BLOCK_STATEMENT]])

    def test_var_as_print(self):
        self._match("x = 3\n print 5", [[const.VAR_AS], [const.PRINT_STATEMENT]], [[const.BLOCK_STATEMENT]])

    def test_var_as_block(self):
        self._match("x = 3\n print 5\n print 65", [[const.VAR_AS], [const.PRINT_STATEMENT], [const.PRINT_STATEMENT]],
                     [[const.VAR_AS, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]])

        # def testForEachIDInFuncCall(self):
        #     expected = [
        #         [const.FOR_EACH, const.ID, const.IN, const.FUNCTION_CALL],
        #         [const.FOR_EACH_STATEMENT]
        #     ]
        #     self._match("For Each n In aa()", expected)
        #
        # def foreach_exception_runner(self, str_to_parse):
        #     parser = Parser()
        #     exp_exception_msg = err_const.PARSING_FAILED
        #     with self.assertRaises(ValueError) as ve:
        #         parser.parse(str_to_parse)
        #         self.assertEqual(ve.exception.args[0], exp_exception_msg)
        #
        # def testForEachValueInID(self):
        #     self.foreach_exception_runner("For Each 1 in num")
        #
        # def testForEachFunctionCallInID(self):
        #     self.foreach_exception_runner("For Each x() in num")
