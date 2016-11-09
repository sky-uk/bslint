import os
import unittest
from io import StringIO

import bslint
import bslint.constants as const
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
        bslint.bslint.runner(to_lex=brs_file_path, out=out)
        result = out.getvalue()
        out.close()
        self.assertEqual(result,
                         const.ERROR_COLOUR + "The path you have provided does not exist." + const.END_COLOUR + "\n")

    def test_brs_file_with_path_lexed(self):
        brs_file_path = "resources/general_test_files/sub_directory1_test_files/print.brs"
        exp_result = ["resources/general_test_files/sub_directory1_test_files/print.brs"]
        self.common.directory_lexing(brs_file_path, exp_result)

    def test_bs_file_with_path_lexed(self):
        brs_file_path = "resources/general_test_files/incorrect-comment-spelling.bs"
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs"]
        self.common.directory_lexing(brs_file_path, exp_result)

    def test_directory_with_path_lexed(self):
        brs_file_path = "resources/general_test_files/sub_directory1_test_files"
        exp_result = ["resources/general_test_files/sub_directory1_test_files/print.brs"]
        self.common.directory_lexing(brs_file_path, exp_result)

    def test_sub_directory_lexed(self):
        brs_file_path = "resources/general_test_files"
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs",
                      "resources/general_test_files/sub_directory1_test_files/print.brs",
                      "resources/general_test_files/sub_directory2_test_files/question-mark.brs"]
        self.common.directory_lexing(brs_file_path, exp_result)

    def test_sub_directory_ignored(self):
        brs_file_path = "resources/general_ignore_test_files"
        exp_result = ["resources/general_ignore_test_files/incorrect-comment-spelling.bs",
                      "resources/general_ignore_test_files/sub_directory2_test_files/question-mark.brs"]
        self.common.directory_lexing(brs_file_path, exp_result)
