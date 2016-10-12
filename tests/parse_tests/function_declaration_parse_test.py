import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const


class TestFunctionDeclarationParse(unittest.TestCase):

    def testFunctionIDOpenParenthesisCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("function x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def testFunctionIDOpenParenthesisParameterCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("function x(y as Object)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def testFunctionIDOpenParenthesisIDCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("function x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def testFunctionIDOpenParenthesisArgumentCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("function x(y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def testSubIDOpenParenthesisValueCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("sub x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def testSubIDOpenParenthesisParameterCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("sub x(y as String)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def testSubIDOpenParenthesisIDCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("sub x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def testSubIDOpenParenthesisArgumentCloseParenthesis(self):
        parser = Parser()
        result = parser.parse("sub x(y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

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
