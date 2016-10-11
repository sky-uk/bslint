import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const


class TestArgumentParse(unittest.TestCase):

    def testArgumentCommaArgument(self):
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

    def testValueCommaValue(self):
        parser = Parser()
        result = parser.parse("a(1, 2)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def testIDCommaID(self):
        parser = Parser()
        result = parser.parse("a(x, y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def testValueCommaArgument(self):
        parser = Parser()
        result = parser.parse("a(2, 1, y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.VALUE, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
            parser.all_statements[0])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[1])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[2])

    def testIDCommaArgument(self):
        parser = Parser()
        result = parser.parse("a(x, y, 2)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ID, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
            parser.all_statements[0])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[1])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[2])

    def testIIDCommaValue(self):
        parser = Parser()
        result = parser.parse("a(x, 1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def testValueCommaID(self):
        parser = Parser()
        result = parser.parse("a(2, y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_CALL], parser.all_statements[1])

    def testFunctionCall(self):
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

    def testInvalidArgumentWhile(self):
        self.argument_exception_runner("x(while, 1)")

    def testInvalidArgumentMinus(self):
        self.argument_exception_runner("x(-)")

    def testInvalidArgumentComment(self):
        self.argument_exception_runner("x(')")
