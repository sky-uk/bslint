import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const


class TestFunctionDeclarationParse(unittest.TestCase):

    def function_declaration_runner(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.statement)

    def testFunctionIDOpenParenthesisCloseParenthesis(self):
        self.function_declaration_runner("function x()")

    def testFunctionIDOpenParenthesisParameterCloseParenthesis(self):
        self.function_declaration_runner("function x(y as Object)")

    def testFunctionIDOpenParenthesisIDCloseParenthesis(self):
        self.function_declaration_runner("function x(y)")

    def testFunctionIDOpenParenthesisArgumentCloseParenthesis(self):
        self.function_declaration_runner("function x(y, z)")

    def testSubIDOpenParenthesisValueCloseParenthesis(self):
        self.function_declaration_runner("sub x()")

    def testSubIDOpenParenthesisParameterCloseParenthesis(self):
        self.function_declaration_runner("sub x(y as String)")

    def testSubIDOpenParenthesisIDCloseParenthesis(self):
        self.function_declaration_runner("sub x(y)")

    def testSubIDOpenParenthesisArgumentCloseParenthesis(self):
        self.function_declaration_runner("sub x(y, z)")

    def function_declaration_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def testInvalidFunctionDeclaraionValue(self):
        self.function_declaration_exception_runner("function 1()")

    def testInvalidFunctionDeclaraionMissingParenthesis(self):
        self.function_declaration_exception_runner("function x(")

    def testInvalidFunctionDeclaraionExtraParenthesis(self):
        self.function_declaration_exception_runner("function x(())")
