import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestValueParse(unittest.TestCase):

    def value_runner(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VALUE], parser.statement)

    def testIDOperatorID(self):
        self.value_runner("x + y")

    def testValueOperatorValue(self):
        self.value_runner("1 + 1")

    def testValueOperatorID(self):
        self.value_runner("1 + y")

    def testIDOperatorValue(self):
        self.value_runner("x + 1")

    def testIDOperatorFunctionCall(self):
        self.value_runner("x + y()")

    def testFunctionCallOperatorID(self):
        self.value_runner("x() + y")

    def testValueOperatorFunctionCall(self):
        self.value_runner("1 + y()")

    def testFunctionCallOperatorValue(self):
        self.value_runner("x() + 1")

    def testFunctionCallOperatorFunctionCall(self):
        self.value_runner("x() + y()")

    def testOpenParenthesisValueCloseParenthesis(self):
        self.value_runner("(1)")

    def testOpenParenthesisIDCloseParenthesis(self):
        self.value_runner("(x)")

    def testOpenParenthesisVariableAssignmentCloseParenthesis(self):
        self.value_runner("(x = 1)")

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
