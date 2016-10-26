import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestVariableAssignment(unittest.TestCase):

    def test_value(self):
        parser = Parser()
        result = parser.parse("jack = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test_identifier(self):
        parser = Parser()
        result = parser.parse("x = y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test_function_call(self):
        parser = Parser()
        result = parser.parse("x = y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_empty_enumerable_object(self):
        parser = Parser()
        result = parser.parse("x = []")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_enumerable_object(self):
        parser = Parser()
        result = parser.parse("x = {x:3}")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.OPEN_CURLY_BRACKET, const.ASSOCIATIVE_ARRAY_ARGUMENT,
                          const.CLOSE_CURLY_BRACKET], parser.all_statements[0])
        self.assertEqual([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT], parser.all_statements[1])
        self.assertEqual([const.VAR_AS], parser.all_statements[2])

    def test_variable_assignment_with_plus_value(self):
        parser = Parser()
        result = parser.parse("x = +3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test_variable_assignment_with_minus_value(self):
        parser = Parser()
        result = parser.parse("x = -3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test_variable_assignment_with_plus_id(self):
        parser = Parser()
        result = parser.parse("x = +y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test_variable_assignment_with_minus_id(self):
        parser = Parser()
        result = parser.parse("x = -y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test_variable_assignment_with_plus_function_call(self):
        parser = Parser()
        result = parser.parse("x = +y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.PLUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_variable_assignment_with_minus_function_call(self):
        parser = Parser()
        result = parser.parse("x = -y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.MINUS, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_open_parenthesis_variable_assignment_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("(x = 1)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_2variable_declarations(self):
        parser = Parser()
        result = parser.parse('jack = 3\n zac = "no good at table tennis"')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_variable_declaration_with_reduction(self):
        parser = Parser()
        result = parser.parse('jack = 3 + 2')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def test_variable_declaration_with_multiple_reduction(self):
        parser = Parser()
        result = parser.parse('jack = 3 + 2 - 5')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE, const.PLUS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE], parser.all_statements[1])
        self.assertEqual([const.VAR_AS], parser.all_statements[2])

    def test_variable_declaration_with_reduction_and_parenthesis(self):
        parser = Parser()
        result = parser.parse('jack = (3 + 2)')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE], parser.all_statements[1])
        self.assertEqual([const.VAR_AS], parser.all_statements[2])

    def variable_assignment_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_invalid_variable_assignment_while(self):
        self.variable_assignment_exception_runner("jack = while")

    def test_invalid_variable_assignment_extra_equals(self):
        self.variable_assignment_exception_runner("jack == 3")

    def test_invalid_variable_assignment_incorrect_order(self):
        self.variable_assignment_exception_runner("3 = jack")
