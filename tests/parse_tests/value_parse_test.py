import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestValueParse(unittest.TestCase):

    def testIDOperatorID(self):
        parser = Parser()
        result = parser.parse("x + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueOperatorValue(self):
        parser = Parser()
        result = parser.parse("1 + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testValueOperatorID(self):
        parser = Parser()
        result = parser.parse("1 + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDOperatorValue(self):
        parser = Parser()
        result = parser.parse("x + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testIDOperatorFunctionCall(self):
        parser = Parser()
        result = parser.parse("x + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallOperatorID(self):
        parser = Parser()
        result = parser.parse("x() + y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.ID], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testValueOperatorFunctionCall(self):
        parser = Parser()
        result = parser.parse("1 + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallOperatorValue(self):
        parser = Parser()
        result = parser.parse("x() + 1")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VALUE], parser.all_statements[1])

    def testFunctionCallOperatorFunctionCall(self):
        parser = Parser()
        result = parser.parse("x() + y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.VALUE], parser.all_statements[2])

    def testOpenParenthesisValueCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("(1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.all_statements[0])

    def testOpenParenthesisIDCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("(x)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID], parser.all_statements[0])

    def testOpenParenthesisVariableAssignmentCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("(x = 1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def value_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def testInvalidValueMultiplePlus(self):
        self.value_exception_runner("+ + + + + + + + + +")

    def testInvalidValueWhile(self):
        self.value_exception_runner("while + 3")

    def testInvalidValuePlusMinus(self):
        self.value_exception_runner("2 +- 3")
