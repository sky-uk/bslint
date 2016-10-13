import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const


class TestFunctionCallParse(unittest.TestCase):

    def testIDOpenParenthesisCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[0])

    def testIDOpenParenthesisArgumnetCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("x(y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def testIDOpenParenthesisValueCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("x(1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[0])

    def testIDOpenParenthesisIDCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[0])

    def testIDOpenParenthesisIDEqualsValueCloseParenthesis(self):
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

    def testInvalidFunctionCallMissingParenthesis(self):
        self.function_call_exception_runner("x(")

    def testInvalidFunctionCallExtraParenthesis(self):
        self.function_call_exception_runner("x(())")

    def testInvalidFunctionCallComment(self):
        self.function_call_exception_runner("'x()")
