import os
import unittest
from io import StringIO
from bslint.messages import print_constants as print_const
from bslint.messages import handler as msg_handler
import bslint
from bslint.interface_handler import InterfaceHandler as InterfaceHandler
from filepaths import TESTS_PATH
from filepaths import TEST_CONFIG_FILE_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestDirectoryLexing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(TESTS_PATH)
        cls.common = Common()

    def setUp(self):
        self.InterfaceHandler = InterfaceHandler()

    def test_incorrect_path(self):
        out = StringIO()
        brs_file_path = "falsepath/file.brs"
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH, out=out)
        result = bslint.bslint.runner(to_lex=brs_file_path, out=out).printed_output
        self.assertEqual(msg_handler.get_print_msg(print_const.PATH_DOESNT_EXIST), result)

    def test_brs_file_with_path_lexed(self):
        brs_file_path = "resources/general_test_files/sub_directory1_test_files/print.brs"
        expected = ["resources/general_test_files/sub_directory1_test_files/print.brs"]
        self.common.directory_lexing(expected, brs_file_path)

    def test_bs_file_with_path_lexed(self):
        brs_file_path = "resources/general_test_files/incorrect-comment-spelling.bs"
        expected = ["resources/general_test_files/incorrect-comment-spelling.bs"]
        self.common.directory_lexing(expected, brs_file_path)

    def test_directory_with_path_lexed(self):
        brs_file_path = "resources/general_test_files/sub_directory1_test_files"
        expected = ["resources/general_test_files/sub_directory1_test_files/print.brs"]
        self.common.directory_lexing(expected, brs_file_path)

    def test_sub_directory_lexed(self):
        brs_file_path = "resources/general_test_files"
        expected = ["resources/general_test_files/incorrect-comment-spelling.bs",
                    "resources/general_test_files/sub_directory1_test_files/print.brs",
                    "resources/general_test_files/sub_directory2_test_files/question-mark.brs"]
        self.common.directory_lexing(expected, brs_file_path)

    def test_sub_directory_ignored(self):
        brs_file_path = "resources/general_ignore_test_files"
        expected = ["resources/general_ignore_test_files/incorrect-comment-spelling.bs",
                    "resources/general_ignore_test_files/sub_directory2_test_files/question-mark.brs"]
        self.common.directory_lexing(expected, brs_file_path)
