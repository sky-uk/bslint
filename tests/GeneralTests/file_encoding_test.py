import unittest
import bslint
import bslint.commands as commands
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os


class TestEncodingCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'
    TOKEN = "token"
    TYPE = "type"
    LINE_NUMBER = "line_number"

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../../resources/")
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/EncodingTestFiles/")

    def testASCIIChars(self):
        config = bslint.load_config_file(user="FileEncoding/ASCII-encoding-config.json")
        commands.config = config
        file_path = self.tests_filepath_prefix + "ASCII-chars.brs"
        result = commands.check_file_encoding(file_path)
        exp_result = None
        self.assertEqual(result, exp_result)

    def testNonASCIIChars(self):
        config = bslint.load_config_file(user="FileEncoding/ASCII-encoding-config.json")
        commands.config = config
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = commands.check_file_encoding(file_path)
        self.assertEqual(result['error_key'], ErrConst.FILE_ENCODING)

    def testUTF8Chars(self):
        config = bslint.load_config_file(user="FileEncoding/UTF8-encoding-config.json")
        commands.config = config
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = commands.check_file_encoding(file_path)
        exp_result = None
        self.assertEqual(result, exp_result)

    def testFileReader(self):
        config = bslint.load_config_file(user="FileEncoding/ASCII-encoding-config.json")
        commands.config = config
        file_path = self.tests_filepath_prefix + "ASCII-chars.brs"
        fo = open(file_path, "r+")
        str_to_lex = fo.read()
        result = bslint.FileReader.read_file(file_path)
        exp_result = {"invalid_encoding": None, "str_to_lex": str_to_lex}
        self.assertEqual(result, exp_result)
