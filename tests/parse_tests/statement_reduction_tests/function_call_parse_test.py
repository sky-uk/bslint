import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestFunctionCallParse(unittest.TestCase):

    def test_id_open_parenthesis_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[0])

    def test_id_open_parenthesis_argument_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("x(y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def test_id_open_parenthesis_value_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("x(1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[0])

    def test_id_open_parenthesis_id_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[0])

    def test_id_dot_function_call(self):
        parser = Parser()
        result = parser.parse("z.x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.DOT, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def test_function_call_dot_function_call(self):
        parser = Parser()
        result = parser.parse("z(i).x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS, const.DOT, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.DOT, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[2])

    def test_id_open_parenthesis_id_equals_value_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("x(y = 1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS],
            parser.all_statements[0])

        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def function_call_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_invalid_function_call_missing_parenthesis(self):
        self.function_call_exception_runner("x(")

    def test_invalid_function_call_extra_parenthesis(self):
        self.function_call_exception_runner("x(())")

    def test_invalid_function_call_comment(self):
        self.function_call_exception_runner("'x()")
