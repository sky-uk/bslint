import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestWhileParse(unittest.TestCase):

    def while_runner(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.statement)

    def testWhileValue(self):
        self.while_runner("while true")

    def testWhileID(self):
        self.while_runner("while x")

    def testWhileVarAs(self):
        self.while_runner("while x = 3")

    def testWhileFunctionCall(self):
        self.while_runner("while x()")

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