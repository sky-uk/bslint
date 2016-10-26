import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser
from bslint.utilities import config_loader


class TestFunctionDeclarationParse(unittest.TestCase):

    def setUp(self):
        config_loader.load_config_file()

    def test_function_idopen_parenthesis_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("function x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def test_function_idopen_parenthesis_parameter_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("function x(y as Object)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS], parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def test_function_idopen_parenthesis_idclose_parenthesis(self):
        parser = Parser()
        result = parser.parse("function x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def test_function_idopen_parenthesis_argument_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("function x(y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def test_sub_idopen_parenthesis_value_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("sub x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def test_sub_idopen_parenthesis_parameter_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("sub x(y as String)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def test_sub_idopen_parenthesis_idclose_parenthesis(self):
        parser = Parser()
        result = parser.parse("sub x(y)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[0])

    def test_sub_idopen_parenthesis_argument_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("sub x(y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.FUNCTION_DECLARATION], parser.all_statements[1])

    def test_anonymous_sub_idopen_parenthesis_value_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("sub ()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ANONYMOUS_FUNCTION_DECLARATION], parser.all_statements[0])

    def test_anonymous_idopen_parenthesis_argument_close_parenthesis(self):
        parser = Parser()
        result = parser.parse("function (y, z)")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FUNCTION, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.ANONYMOUS_FUNCTION_DECLARATION], parser.all_statements[1])

    def function_declaration_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def test_invalid_function_declaraion_value(self):
        self.function_declaration_exception_runner("function 1()")

    def test_invalid_function_declaraion_missing_parenthesis(self):
        self.function_declaration_exception_runner("function x(")

    def test_invalid_function_declaraion_extra_parenthesis(self):
        self.function_declaration_exception_runner("function x(())")
