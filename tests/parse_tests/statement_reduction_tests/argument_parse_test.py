import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestArgumentParse(unittest.TestCase):
    def test_argument_comma_argument(self):
        parser = Parser()
        result = parser.parse("a(x, 1, y, 2)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ID, const.COMMA, const.VALUE, const.COMMA, const.ARGUMENT,
             const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ID, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
            parser.all_statements[1])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[2])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[3])

    def test_value_comma_value(self):
        parser = Parser()
        result = parser.parse("a(1, 2)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def test_id_comma_id(self):
        parser = Parser()
        result = parser.parse("a(x, y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def test_value_comma_argument(self):
        parser = Parser()
        result = parser.parse("a(2, 1, y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.VALUE, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
            parser.all_statements[0])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[1])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[2])

    def test_id_comma_argument(self):
        parser = Parser()
        result = parser.parse("a(x, y, 2)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ID, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
            parser.all_statements[0])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[1])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[2])

    def test_id_comma_value(self):
        parser = Parser()
        result = parser.parse("a(x, 1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def test_value_comma_id(self):
        parser = Parser()
        result = parser.parse("a(2, y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def test_function_call(self):
        parser = Parser()
        result = parser.parse("a(b())")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.FUNCTION_CALL, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def argument_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_invalid_argument_while(self):
        self.argument_exception_runner("x(while, 1)")

    def test_invalid_argument_minus(self):
        self.argument_exception_runner("x(-)")

    def test_invalid_argument_comment(self):
        self.argument_exception_runner("x(')")
