import unittest
import bslint
import bslint.constants as const
import bslint.utilities.regex_handler as regex_handler


class TestSkipLineRegex(unittest.TestCase):

    COMMAND_GROUP = 'command'
    SKIP_LINE = 'skip_line'
    SKIP_FILE = 'skip_file'

    def testSkipLineSingleSpace(self):
        identifier = "' BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipLineNoSpaces(self):
        identifier = "'BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipLineTextAfterCommand(self):
        identifier = "' BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipLineFiveSpaces(self):
        identifier = "'     BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipLineWithText(self):
        identifier = "' randomText BSLINT_skip_line \n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def testSkipFile(self):
        identifier = "'BSLINT_skip_file\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_FILE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipFileWithRemCommand(self):
        identifier = "rem BSLINT_skip_file\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_FILE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipRemLineSingleSpace(self):
        identifier = "rem BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipRemLineNoSpaces(self):
        identifier = "remBSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipRemLineTextAfterCommand(self):
        identifier = "rem BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipRemLineFiveSpaces(self):
        identifier = "rem     BSLINT_skip_line\n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_lexer_type"], const.BSLINT_COMMAND)
        self.assertEqual(result["token_parser_type"], const.BSLINT_COMMAND)

    def testSkipRemLineWithText(self):
        identifier = "rem randomText BSLINT_skip_line \n"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)
