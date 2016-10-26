import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestValueParse(unittest.TestCase):

    def test_id_operator_id(self):
        parser = Parser()
        result = parser.parse("x / y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_operator_value(self):
        parser = Parser()
        result = parser.parse("1 / 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_operator_id(self):
        parser = Parser()
        result = parser.parse("1 / y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_operator_value(self):
        parser = Parser()
        result = parser.parse("x / 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_operator_function_call(self):
        parser = Parser()
        result = parser.parse("x / y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_operator_id(self):
        parser = Parser()
        result = parser.parse("x() / y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_operator_function_call(self):
        parser = Parser()
        result = parser.parse("1 / y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_operator_value(self):
        parser = Parser()
        result = parser.parse("x() / 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_operator_function_call(self):
        parser = Parser()
        result = parser.parse("x() / y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_id_plus_id(self):
        parser = Parser()
        result = parser.parse("x + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_plus_plus_id(self):
        parser = Parser()
        result = parser.parse("x + +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_plus_minus_id(self):
        parser = Parser()
        result = parser.parse("x + -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_plus_value(self):
        parser = Parser()
        result = parser.parse("1 + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_plus_plus_value(self):
        parser = Parser()
        result = parser.parse("1 + +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_minus_plus_value(self):
        parser = Parser()
        result = parser.parse("1 - +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_plus_id(self):
        parser = Parser()
        result = parser.parse("1 + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_plus_plus_id(self):
        parser = Parser()
        result = parser.parse("1 + +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_plus_minus_id(self):
        parser = Parser()
        result = parser.parse("1 + -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_plus_value(self):
        parser = Parser()
        result = parser.parse("x + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_plus_plus_value(self):
        parser = Parser()
        result = parser.parse("x + +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_plus_minus_value(self):
        parser = Parser()
        result = parser.parse("x + -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_id_plus_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x + +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_id_plus_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x + -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_id(self):
        parser = Parser()
        result = parser.parse("x() + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_plus_id(self):
        parser = Parser()
        result = parser.parse("x() + +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_minus_id(self):
        parser = Parser()
        result = parser.parse("x() + -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_plus_function_call(self):
        parser = Parser()
        result = parser.parse("1 + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_plus_plus_function_call(self):
        parser = Parser()
        result = parser.parse("1 + +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_plus_minus_function_call(self):
        parser = Parser()
        result = parser.parse("1 + -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_value(self):
        parser = Parser()
        result = parser.parse("x() + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_plus_value(self):
        parser = Parser()
        result = parser.parse("x() + +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_minus_value(self):
        parser = Parser()
        result = parser.parse("x() + -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x() + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_function_call_plus_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x() + +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_function_call_plus_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x() + -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_id_minus_id(self):
        parser = Parser()
        result = parser.parse("x - y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_minus_plus_id(self):
        parser = Parser()
        result = parser.parse("x - +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_minus_minus_id(self):
        parser = Parser()
        result = parser.parse("x - -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_minus_value(self):
        parser = Parser()
        result = parser.parse("1 - 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_plus_minus_value(self):
        parser = Parser()
        result = parser.parse("1 + -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_minus_minus_value(self):
        parser = Parser()
        result = parser.parse("1 - -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_minus_id(self):
        parser = Parser()
        result = parser.parse("1 - y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_minus_plus_id(self):
        parser = Parser()
        result = parser.parse("1 - +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_value_minus_minus_id(self):
        parser = Parser()
        result = parser.parse("1 - -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_minus_value(self):
        parser = Parser()
        result = parser.parse("x - 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_minus_plus_value(self):
        parser = Parser()
        result = parser.parse("x - +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_minus_minus_value(self):
        parser = Parser()
        result = parser.parse("x - -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_id_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x - y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_id_minus_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x - +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_id_minus_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x - -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_id(self):
        parser = Parser()
        result = parser.parse("x() - y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_plus_id(self):
        parser = Parser()
        result = parser.parse("x() - +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_minus_id(self):
        parser = Parser()
        result = parser.parse("x() - -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_minus_function_call(self):
        parser = Parser()
        result = parser.parse("1 - y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_minus_plus_function_call(self):
        parser = Parser()
        result = parser.parse("1 - +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_value_minus_minus_function_call(self):
        parser = Parser()
        result = parser.parse("1 - -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_value(self):
        parser = Parser()
        result = parser.parse("x() - 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_plus_value(self):
        parser = Parser()
        result = parser.parse("x() - +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_minus_value(self):
        parser = Parser()
        result = parser.parse("x() - -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def test_function_call_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x() - y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_function_call_minus_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x() - +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_function_call_minus_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x() - -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def test_open_parenthesis_value_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("(1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def test_function_call_dot_id(self):
        parser = Parser()
        result = parser.parse("func_name().id")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.DOT, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    # Only ID Test
    def test_open_parenthesis_id_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("(x)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID], parser.all_statements[0])

    def value_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_invalid_value_multiple_plus(self):
        self.value_exception_runner("+ + + + + + + + + +")

    def test_invalid_value_minus(self):
        self.value_exception_runner("3-")

    def test_invalid_value_idplus_while(self):
        self.value_exception_runner("a + while")
