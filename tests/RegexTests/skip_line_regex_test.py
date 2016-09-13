import unittest
import src
import src.constants as const


class TestSkipLineRegex(unittest.TestCase):

    COMMAND_GROUP = 'command'
    SKIP_LINE = 'skip_line'
    SKIP_FILE = 'skip_file'

    def setUp(self):
        self.regex_handler = src.RegexHandler()

    def testSkipLineSingleSpace(self):
        identifier = "' BSLINT_skip_line\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipLineNoSpaces(self):
        identifier = "'BSLINT_skip_line\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipLineTextAfterCommand(self):
        identifier = "' BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipLineFiveSpaces(self):
        identifier = "'     BSLINT_skip_line\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipLineWithText(self):
        identifier = "' randomText BSLINT_skip_line \n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["token_type"], const.COMMENT)

    def testSkipFile(self):
        identifier = "'BSLINT_skip_file\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_FILE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipFileWithRemCommand(self):
        identifier = "rem BSLINT_skip_file\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_FILE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipRemLineSingleSpace(self):
        identifier = "rem BSLINT_skip_line\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipRemLineNoSpaces(self):
        identifier = "remBSLINT_skip_line\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipRemLineTextAfterCommand(self):
        identifier = "rem BSLINT_skip_line asfasfasfsadfsafsaf\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipRemLineFiveSpaces(self):
        identifier = "rem     BSLINT_skip_line\n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(self.SKIP_LINE, result["match"].group(self.COMMAND_GROUP))
        self.assertEqual(result["token_type"], const.BSLINT_COMMAND)

    def testSkipRemLineWithText(self):
        identifier = "rem randomText BSLINT_skip_line \n"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["token_type"], const.COMMENT)

