import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestWhileParse(unittest.TestCase):

    def test_while_value(self):
        parser = Parser()
        result = parser.parse("while true")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def test_while_plus_value(self):
        parser = Parser()
        result = parser.parse("while + 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def test_while_minus_value(self):
        parser = Parser()
        result = parser.parse("while - 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def test_while_id(self):
        parser = Parser()
        result = parser.parse("while x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def test_while_plus_id(self):
        parser = Parser()
        result = parser.parse("while +x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def test_while_minus_id(self):
        parser = Parser()
        result = parser.parse("while -x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[0])

    def test_while_var_as(self):
        parser = Parser()
        result = parser.parse("while x = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[1])

    def test_while_function_call(self):
        parser = Parser()
        result = parser.parse("while x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[1])

    def test_while_plus_function_call(self):
        parser = Parser()
        result = parser.parse("while +x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[1])

    def test_while_minus_function_call(self):
        parser = Parser()
        result = parser.parse("while -x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.WHILE, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.WHILE_STATEMENT], parser.all_statements[1])

    def while_exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def test_invalid_while_parenthesis(self):
        self.while_exception_runner("while )")

    def test_invalid_while_for(self):
        self.while_exception_runner("while (for)")

    def test_invalid_while_end_while(self):
        self.while_exception_runner("while endwhile")