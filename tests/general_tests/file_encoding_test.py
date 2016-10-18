import os
import unittest

import bslint
import bslint.error_messages.constants as err_const
import bslint.lexer.commands as commands
from bslint.interface_handler import InterfaceHandler as InterfaceHandler


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
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/encoding_test_files/")

    def test_ascii_chars(self):
        bslint.load_config_file(user_filepath="file_encoding/ASCII-encoding-config.json")
        file_path = self.tests_filepath_prefix + "ASCII-chars.brs"
        result = commands.check_file_encoding(file_path)
        exp_result = None
        self.assertEqual(result, exp_result)

    def test_non_ascii_chars(self):
        bslint.load_config_file(user_filepath="file_encoding/ASCII-encoding-config.json")
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = commands.check_file_encoding(file_path)
        self.assertEqual(result['error_key'], err_const.FILE_ENCODING)

    def test_utf_8_chars(self):
        bslint.load_config_file(user_filepath="file_encoding/UTF8-encoding-config.json")
        file_path = self.tests_filepath_prefix + "NON-ASCII-chars.brs"
        result = commands.check_file_encoding(file_path)
        exp_result = None
        self.assertEqual(result, exp_result)

    def test_file_reader(self):
        bslint.load_config_file(user_filepath="file_encoding/ASCII-encoding-config.json")
        file_path = self.tests_filepath_prefix + "ASCII-chars.brs"
        fo = open(file_path, "r+")
        str_to_lex = fo.read()
        result = InterfaceHandler.file_reader(file_path)
        exp_result = {"invalid_encoding": None, "str_to_lex": str_to_lex}
        self.assertEqual(result, exp_result)
