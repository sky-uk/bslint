import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages.constants as err_const


class TestArgumentParse(unittest.TestCase):
    def testOpenCurlyBracketCloseCurlyBracket(self):
        parser = Parser()
        result = parser.parse("{}")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[0])

    def testOpenCurlyBracketIDColonValueCloseCurlyBracket(self):
        parser = Parser()
        result = parser.parse("{a:1}")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.OPEN_CURLY_BRACKET, const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET],
                         parser.all_statements[0])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[1])

    def testOpenCurlyBracketObjectCommaObjectCloseCurlyBracket(self):
        parser = Parser()
        result = parser.parse("{a:1, b:2}")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.OPEN_CURLY_BRACKET, const.ID, const.COLON, const.VALUE, const.COMMA,
                          const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET],
                         parser.all_statements[0])
        self.assertEqual(
            [const.OPEN_CURLY_BRACKET, const.ASSOCIATIVE_ARRAY_ARGUMENT, const.COMMA, const.ASSOCIATIVE_ARRAY_ARGUMENT,
             const.CLOSE_CURLY_BRACKET], parser.all_statements[1])
        self.assertEqual([const.OPEN_CURLY_BRACKET, const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET],
                         parser.all_statements[2])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[3])

    def testOpenSquareBracketCloseSquareBracket(self):
        parser = Parser()
        result = parser.parse("[]")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[0])

    def testOpenSquareBracketValueCloseSquareBracket(self):
        parser = Parser()
        result = parser.parse("[5]")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[0])

    def testOpenSquareBracketIDCloseSquareBracket(self):
        parser = Parser()
        result = parser.parse("[x]")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[0])

    def testOpenSquareBracketValueCommaIDCloseSquareBracket(self):
        parser = Parser()
        result = parser.parse("[5, x]")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.OPEN_SQUARE_BRACKET, const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET],
                         parser.all_statements[0])
        self.assertEqual([const.ENUMERABLE_OBJECT], parser.all_statements[1])

    def argument_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def testInvalidAssociativeArrayVarAs(self):
        self.argument_exception_runner("{x = 3}")

    def testInvalidArrayVarAs(self):
        self.argument_exception_runner("[y = 2]")

    def testInvalidMismatchedArrayBraces(self):
        self.argument_exception_runner("[}")
