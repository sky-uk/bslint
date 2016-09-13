import unittest
import src
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os



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
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../../resources/")
        cls.tests_filepath_prefix = os.path.join(this_dir, "../EncodingTestFiles/")

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
        self.assertEqual(result['error_key'], ErrConst.FILE_ENCODING)

    def testUTF8Chars(self):
        config = src.load_config_file(user="FileEncoding/UTF8-encoding-config.json")
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = self.encodingCheck.execute({"file_path": file_path, **config['check_file_encoding']['params']})
        exp_result = None
        self.assertEqual(result, exp_result)
