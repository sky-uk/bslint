import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestWhileParse(unittest.TestCase):

    def testWhileValue(self):
        parser = Parser()
        result = parser.parse("while true")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def testWhileID(self):
        parser = Parser()
        result = parser.parse("while x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def testWhileVarAs(self):
        parser = Parser()
        result = parser.parse("while x = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[1])

    def testWhileFunctionCall(self):
        parser = Parser()
        result = parser.parse("while x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[1])

    def while_exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def testInvalidWhileParenthesis(self):
        self.while_exception_runner("while )")

    def testInvalidWhileFor(self):
        self.while_exception_runner("while (for)")

    def testInvalidWhileEndWhile(self):
        self.while_exception_runner("while endwhile")