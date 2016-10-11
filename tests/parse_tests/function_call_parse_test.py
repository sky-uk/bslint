import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const



class TestFunctionCallParse(unittest.TestCase):

    def function_call_runner(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.statement)

    def testIDOpenParenthesisCloseParenthesis(self):
        self.function_call_runner("x()")

    def testIDOpenParenthesisArgumnetCloseParenthesis(self):
        self.function_call_runner("x(y, z)")

    def testIDOpenParenthesisValueCloseParenthesis(self):
        self.function_call_runner("x(1)")

    def testIDOpenParenthesisIDCloseParenthesis(self):
        self.function_call_runner("x(y)")

    def testIDOpenParenthesisIDCloseParenthesis(self):
        self.function_call_runner("x(y = 1)")

    def function_call_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def testInvalidFunctionCallMissingParenthesis(self):
        self.function_call_exception_runner("x(")

    def testInvalidFunctionCallExtraParenthesis(self):
        self.function_call_exception_runner("x(())")

    def testInvalidFunctionCallComment(self):
        self.function_call_exception_runner("'x()")
