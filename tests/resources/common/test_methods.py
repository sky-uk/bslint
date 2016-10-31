import unittest
from bslint.parser.parser import Parser
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer
import bslint.lexer.handlers.regex_handler as regex_handler


class CommonMethods(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    def exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def match_statement(self, input, expected):
        parser = Parser()
        result = parser.parse(input)
        self.assertEqual("Success", result["Status"])
        self.assertEqual(expected, parser.all_statements[-1][0])

    def match_program(self, input, expected):
        parser = Parser()
        result = parser.parse(input)
        self.assertEqual("Success", result["Status"])
        self.assertEqual(expected, parser.line_reductions[-1][0])

    def lex_warnings_match(self, input, exp_result):
        result = Lexer().lex(input)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def match_regex(self, identifier, match_group, lexer_type, parser_type):
        result = regex_handler.find_match(identifier)
        if match_group is None:
            self.assertEqual(result["match"].group(), identifier)
        else:
            self.assertEqual(result["match"].group(match_group), identifier)
        self.assertEqual(result["token_lexer_type"], lexer_type)
        self.assertEqual(result["token_parser_type"], parser_type)