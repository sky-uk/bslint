import unittest

from filepaths import TEST_CONFIG_FILE_PATH
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer
import bslint.lexer.handlers.regex_handler as regex_handler
import bslint


class CommonMethods(unittest.TestCase):

    def status_error(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual(const.ERROR, result["Status"])

    def match_statement(self, expected, characters):
        parser = Parser()
        parser.parse(characters)
        self.assertEqual(expected, parser.all_statements[-1][0])
        self.assertEqual(len(parser.all_statements[-1]), 1)

    def match_program(self, expected, characters):
        parser = Parser()
        result = parser.parse(characters)
        self.assertEqual(const.SUCCESS, result["Status"])
        self.assertEqual(expected, parser.line_reductions[-1][0])

    def lex_warnings_match(self, expected, characters):
        result = Lexer().lex(characters)
        self.assertEqual(expected, result[const.WARNINGS])

    def match_regex(self, identifier, match_group, lexer_type, parser_type):
        result = regex_handler.find_match(identifier)
        if match_group is None:
            self.assertEqual(identifier, result[const.MATCH].group())
        else:
            self.assertEqual(identifier, result[const.MATCH].group(match_group))
        self.assertEqual(lexer_type, result[const.TOKEN_LEXER_TYPE])
        self.assertEqual(parser_type, result[const.TOKEN_PARSER_TYPE])

    def directory_lexing(self, expected, brs_file_path):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner(brs_file_path).files
        expected.sort()
        result.sort()
        self.assertEqual(expected, result)

    def method_dec_spacing(self, expected, string):
        result = commands.check_method_dec_spacing(string)
        self.assertEqual(expected, result)

    def spaces_around_operators(self, expected, string, chars_index, operator):
        result = commands.check_spaces_around_operators(string, chars_index, operator)
        self.assertEqual(expected, result)

    def spell_check(self, expected, string):
        result = commands.check_spelling(string, const.ID)
        self.assertEqual(expected, result)

    def lex_file(self, expected, file):
        file = open(file, "r+").read()
        result = Lexer().lex(file)
        self.assertEqual(expected, result[const.WARNINGS])
        self.assertEqual(const.SUCCESS, result[const.STATUS])

    def lex_string(self, expected, string):
        result = Lexer().lex(string)
        self.assertEqual(expected, result[const.WARNINGS])
        self.assertEqual(const.SUCCESS, result[const.STATUS])

    def lex_identifier(self, expected, identifier):
        lexer = Lexer()
        lexer.lex(identifier)
        self.assertEqual(expected, lexer.statements_counter)

    def match(self, identifier, match_group):
        result = regex_handler.find_match(identifier)
        self.assertEqual(identifier, result[const.MATCH].group(match_group))
        self.assertEqual(const.ID, result[const.TOKEN_LEXER_TYPE])
        self.assertEqual(const.ID, result[const.TOKEN_PARSER_TYPE])
