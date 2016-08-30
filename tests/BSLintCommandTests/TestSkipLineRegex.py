import unittest
import src
import Constants as const


class TestSkipLineRegex(unittest.TestCase):

    COMMAND_GROUP = 'command'
    SKIP_LINE = 'skip_line'
    SKIP_FILE = 'skip_file'

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testSkipLineSingleSpace(self):
        identifier = "' BSLINT_skip_line\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipLineNoSpaces(self):
        identifier = "'BSLINT_skip_line\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipLineTextAfterCommand(self):
        identifier = "' BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipLineFiveSpaces(self):
        identifier = "'     BSLINT_skip_line\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipLineWithText(self):
        identifier = "' randomText BSLINT_skip_line \n"
        result, regex = self.lexer.regex_handler(identifier)
        self.assertEqual(regex, const.COMMENT)

    def testSkipFile(self):
        identifier = "'BSLINT_skip_file\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_FILE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipFileWithRemCommand(self):
        identifier = "rem BSLINT_skip_file\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_FILE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipRemLineSingleSpace(self):
        identifier = "rem BSLINT_skip_line\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipRemLineNoSpaces(self):
        identifier = "remBSLINT_skip_line\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipRemLineTextAfterCommand(self):
        identifier = "rem BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipRemLineFiveSpaces(self):
        identifier = "rem     BSLINT_skip_line\n"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(result.group(self.COMMAND_GROUP), self.SKIP_LINE)
        self.assertEqual(regex_type, const.BSLINT_COMMAND)

    def testSkipRemLineWithText(self):
        identifier = "rem randomText BSLINT_skip_line \n"
        result, regex = self.lexer.regex_handler(identifier)
        self.assertEqual(regex, const.COMMENT)

