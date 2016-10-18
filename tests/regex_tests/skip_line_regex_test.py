import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestSkipLineRegex(unittest.TestCase):

    COMMAND_GROUP = 'command'
    SKIP_LINE = 'skip_line'
    SKIP_FILE = 'skip_file'

    def test_skip_line_single_space(self):
        identifier = "' BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_line_no_spaces(self):
        identifier = "'BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def test_skip_line_text_after_command(self):
        identifier = "' BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_line_five_spaces(self):
        identifier = "'     BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_line_with_text(self):
        identifier = "' randomText BSLINT_skip_line \n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def test_skip_file(self):
        identifier = "'BSLINT_skip_file\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_FILE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_file_with_rem_command(self):
        identifier = "rem BSLINT_skip_file\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_FILE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_rem_line_single_space(self):
        identifier = "rem BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_rem_line_no_spaces(self):
        identifier = "remBSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def test_skip_rem_line_text_after_command(self):
        identifier = "rem BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_rem_line_five_spaces(self):
        identifier = "rem     BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def test_skip_rem_line_with_text(self):
        identifier = "rem randomText BSLINT_skip_line \n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)
