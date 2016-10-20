import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestForEachParse(unittest.TestCase):

    def _match(self, str, expected):
        parser = Parser()
        result = parser.parse(str)
        self.assertEqual("Success", result["Status"])
        index = 0
        for expect in expected:
            self.assertEqual(expect, parser.all_statements[index])
            index += 1

    def test_for_each_id_in_id(self):
        self._match("For Each n In aa", [[const.FOR_EACH_STATEMENT]])

    def test_for_each_id_in_func_call(self):
        expected = [
            [const.FOR_EACH, const.ID, const.IN, const.FUNCTION_CALL],
            [const.FOR_EACH_STATEMENT]
        ]
        self._match("For Each n In aa()", expected)

    def test_for_each_id_in_value(self):
        self._match("For Each char In \"abc\"", [[const.FOR_EACH_STATEMENT]])

    def foreach_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_for_each_value_in_id(self):
        self.foreach_exception_runner("For Each 1 in num")

    def test_for_each_function_call_in_id(self):
        self.foreach_exception_runner("For Each x() in num")

