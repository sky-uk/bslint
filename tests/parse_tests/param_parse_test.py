import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestParamParse(unittest.TestCase):
    def testIDAsType(self):
        parser = Parser()
        result = parser.parse("function x(y as Object)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
            parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def testVar_AsAsType(self):
        parser = Parser()
        result = parser.parse('sub x(y = "test" as String)')
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.SUB, const.ID, const.OPEN_PARENTHESIS, const.VAR_AS, const.AS, const.TYPE,
             const.CLOSE_PARENTHESIS],
            parser.all_statements[0])
        self.assertEqual(
            [const.SUB, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
            parser.all_statements[1])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[2])

    def testParamCommaParam(self):
        parser = Parser()
        result = parser.parse("function x(y as Object, z as Double)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ID, const.AS, const.TYPE, const.COMMA, const.PARAM,
             const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual(
            [const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.COMMA, const.PARAM,
             const.CLOSE_PARENTHESIS], parser.all_statements[1])
        self.assertEqual(
            [const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
            parser.all_statements[2])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[3])

    def param_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def testInvalidParamValue(self):
        self.param_exception_runner("function x(1 as Integer)")

    def testInvalidParamWhile(self):
        self.param_exception_runner("function x(while)")

    def testInvalidParamPlus(self):
        self.param_exception_runner("function x(+)")
