import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestSkipLineRegex(unittest.TestCase):

    COMMAND_GROUP = 'command'
    SKIP_LINE = 'skip_line'
    SKIP_FILE = 'skip_file'

    def _match(self, identifier, token_type, match):
        result = regex_handler.find_match(identifier)
        self.assertEqual(match, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], token_type)
        self.assertEqual(result["token_parser_type"], token_type)

    def test_skip_line_single_space(self):
        self._match("' BSLINT_skip_line\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    def test_skip_line_no_spaces(self):
        self._match("'BSLINT_skip_line\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    # Should be interpreted as a string
    def test_skip_line_text_after_command(self):
        self._match("'     BSLINT_skip_line\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    def test_skip_line_with_text(self):
        identifier = "' randomText BSLINT_skip_line \n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def test_skip_file(self):
        self._match("'BSLINT_skip_file\n", const.BSLINT_COMMAND, self.SKIP_FILE)

    def test_skip_file_with_rem_command(self):
        self._match("rem BSLINT_skip_file\n", const.BSLINT_COMMAND, self.SKIP_FILE)

    def test_skip_rem_line_single_space(self):
        self._match("rem BSLINT_skip_line\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    def test_skip_rem_line_no_spaces(self):
        self._match("remBSLINT_skip_line\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    # Should be interpreted as a string
    def test_skip_rem_line_text_after_command(self):
        self._match("rem BSLINT_skip_line asfasfasfsadfsafsaf\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    def test_skip_rem_line_five_spaces(self):
        self._match("rem     BSLINT_skip_line\n", const.BSLINT_COMMAND, self.SKIP_LINE)

    def test_skip_rem_line_with_text(self):
        identifier = "rem randomText BSLINT_skip_line \n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)
