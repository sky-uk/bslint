import unittest
import src
import sys
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestEncodingCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'
    TOKEN = "token"
    TYPE = "type"
    LINE_NUMBER = "line_number"

    def setUp(self):
        self.encodingCheck = src.CheckFileEncodingCommand()

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
            cls.tests_filepath_prefix = "./resources/EncodingTestFiles/"
        else:
            cls.filepath_prefix = "../resources/"
            cls.tests_filepath_prefix = "../resources/EncodingTestFiles/"

    def testASCIIChars(self):
        config = src.load_config_file(user="FileEncoding/ASCII-encoding-config.json")
        file_path = self.tests_filepath_prefix + "ASCII-chars.brs"
        result = self.encodingCheck.execute({"file_path": file_path, **config['check_file_encoding']['params']})
        exp_result = None
        self.assertEqual(result, exp_result)

    def testNonASCIIChars(self):
        config = src.load_config_file(user="FileEncoding/ASCII-encoding-config.json")
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = self.encodingCheck.execute({"file_path": file_path, **config['check_file_encoding']['params']})
        error = Err.ErrorMessageHandler()
        exp_result = error.get(ErrConst.FILE_ENCODING,
                               [config['check_file_encoding']['params']["source_file_encoding"]])
        self.assertEqual(result, exp_result)

    def testUTF8Chars(self):
        config = src.load_config_file(user="FileEncoding/UTF8-encoding-config.json")
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = self.encodingCheck.execute({"file_path": file_path, **config['check_file_encoding']['params']})
        exp_result = None
        self.assertEqual(result, exp_result)
