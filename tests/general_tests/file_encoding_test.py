import os
import unittest

import bslint
import bslint.error_messages.constants as err_const
import bslint.lexer.commands as commands
from bslint.interface_handler import InterfaceHandler as InterfaceHandler
from filepaths import TESTS_CONFIG_PATH
from filepaths import TESTS_RESOURCES_PATH


class TestEncodingCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'
    TOKEN = "token"
    TYPE = "type"
    LINE_NUMBER = "line_number"

    @classmethod
    def setUpClass(cls):
        cls.ascii_encoding_config_path = os.path.join(TESTS_CONFIG_PATH, 'file_encoding/ASCII-encoding-config.json')
        cls.ascii_chars_file_path = os.path.join(TESTS_RESOURCES_PATH, 'encoding_test_files/ASCII-chars.brs')
        cls.non_ascii_chars_file_path = os.path.join(TESTS_RESOURCES_PATH, 'encoding_test_files/NON-ASCII-chars.brs')

    def test_ascii_chars(self):
        bslint.load_config_file(user_filepath=self.ascii_encoding_config_path)
        file_path = self.ascii_chars_file_path
        result = commands.check_file_encoding(file_path)
        exp_result = None
        self.assertEqual(result, exp_result)

    def test_non_ascii_chars(self):
        bslint.load_config_file(user_filepath=self.ascii_encoding_config_path)
        file_path = self.non_ascii_chars_file_path
        result = commands.check_file_encoding(file_path)
        self.assertEqual(result['error_key'], err_const.FILE_ENCODING)

    def test_utf_8_chars(self):
        utf8_encoding_config_path = os.path.join(TESTS_CONFIG_PATH, 'file_encoding/UTF8-encoding-config.json')
        bslint.load_config_file(user_filepath=utf8_encoding_config_path)
        file_path = self.non_ascii_chars_file_path
        result = commands.check_file_encoding(file_path)
        exp_result = None
        self.assertEqual(result, exp_result)

    def test_file_reader(self):
        bslint.load_config_file(user_filepath=self.ascii_encoding_config_path)
        file_path = self.ascii_chars_file_path
        fo = open(file_path, "r+")
        str_to_lex = fo.read()
        result = InterfaceHandler.file_reader(file_path)
        exp_result = {"invalid_encoding": None, "str_to_lex": str_to_lex}
        self.assertEqual(result, exp_result)
