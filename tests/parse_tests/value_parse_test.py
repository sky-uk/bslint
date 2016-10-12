import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestValueParse(unittest.TestCase):

    def testIDOperatorID(self):
        parser = Parser()
        result = parser.parse("x / y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueOperatorValue(self):
        parser = Parser()
        result = parser.parse("1 / 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueOperatorID(self):
        parser = Parser()
        result = parser.parse("1 / y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDOperatorValue(self):
        parser = Parser()
        result = parser.parse("x / 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDOperatorFunctionCall(self):
        parser = Parser()
        result = parser.parse("x / y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallOperatorID(self):
        parser = Parser()
        result = parser.parse("x() / y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValueOperatorFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 / y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallOperatorValue(self):
        parser = Parser()
        result = parser.parse("x() / 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallOperatorFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() / y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testIDPlusID(self):
        parser = Parser()
        result = parser.parse("x + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDPlusPlusID(self):
        parser = Parser()
        result = parser.parse("x + +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDPlusMinusID(self):
        parser = Parser()
        result = parser.parse("x + -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValuePlusValue(self):
        parser = Parser()
        result = parser.parse("1 + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValuePlusPlusValue(self):
        parser = Parser()
        result = parser.parse("1 + +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueMinusPlusValue(self):
        parser = Parser()
        result = parser.parse("1 - +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValuePlusID(self):
        parser = Parser()
        result = parser.parse("1 + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValuePlusPlusID(self):
        parser = Parser()
        result = parser.parse("1 + +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValuePlusMinusID(self):
        parser = Parser()
        result = parser.parse("1 + -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDPlusValue(self):
        parser = Parser()
        result = parser.parse("x + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDPlusPlusValue(self):
        parser = Parser()
        result = parser.parse("x + +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDPlusMinusValue(self):
        parser = Parser()
        result = parser.parse("x + -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testIDPlusPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x + +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testIDPlusMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x + -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusID(self):
        parser = Parser()
        result = parser.parse("x() + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusPlusID(self):
        parser = Parser()
        result = parser.parse("x() + +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusMinusID(self):
        parser = Parser()
        result = parser.parse("x() + -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValuePlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValuePlusPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 + +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValuePlusMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 + -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusValue(self):
        parser = Parser()
        result = parser.parse("x() + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusPlusValue(self):
        parser = Parser()
        result = parser.parse("x() + +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusMinusValue(self):
        parser = Parser()
        result = parser.parse("x() + -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testFunctionCallPlusPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() + +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testFunctionCallPlusMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() + -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testIDMinusID(self):
        parser = Parser()
        result = parser.parse("x - y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDMinusPlusID(self):
        parser = Parser()
        result = parser.parse("x - +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDMinusMinusID(self):
        parser = Parser()
        result = parser.parse("x - -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueMinusValue(self):
        parser = Parser()
        result = parser.parse("1 - 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValuePlusMinusValue(self):
        parser = Parser()
        result = parser.parse("1 + -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueMinusMinusValue(self):
        parser = Parser()
        result = parser.parse("1 - -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueMinusID(self):
        parser = Parser()
        result = parser.parse("1 - y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueMinusPlusID(self):
        parser = Parser()
        result = parser.parse("1 - +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueMinusMinusID(self):
        parser = Parser()
        result = parser.parse("1 - -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDMinusValue(self):
        parser = Parser()
        result = parser.parse("x - 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDMinusPlusValue(self):
        parser = Parser()
        result = parser.parse("x - +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDMinusMinusValue(self):
        parser = Parser()
        result = parser.parse("x - -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x - y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testIDMinusPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x - +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testIDMinusMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x - -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusID(self):
        parser = Parser()
        result = parser.parse("x() - y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusPlusID(self):
        parser = Parser()
        result = parser.parse("x() - +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusMinusID(self):
        parser = Parser()
        result = parser.parse("x() - -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValueMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 - y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValueMinusPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 - +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValueMinusMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 - -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusValue(self):
        parser = Parser()
        result = parser.parse("x() - 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusPlusValue(self):
        parser = Parser()
        result = parser.parse("x() - +1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusMinusValue(self):
        parser = Parser()
        result = parser.parse("x() - -1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() - y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testFunctionCallMinusPlusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() - +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testFunctionCallMinusMinusFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() - -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testOpenParenthesisValueCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("(1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    # Only ID Test
    def testOpenParenthesisIDCloseParenthesis(self):
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

    def testInvalidValueMultiplePlus(self):
        self.value_exception_runner("+ + + + + + + + + +")

    def testInvalidValueMinus(self):
        self.value_exception_runner("3-")

    def testInvalidValueIDPlusWhile(self):
        self.value_exception_runner("a + while")
