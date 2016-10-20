import os
import unittest

import bslint
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_PATH


class TestDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.chdir(TESTS_PATH)

    def test_brs_file_with_path_lexed(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner("resources/general_test_files/sub_directory1_test_files/print.brs").files
        exp_result = ["resources/general_test_files/sub_directory1_test_files/print.brs"]
        self.assertEqual(exp_result, result)

    def test_bs_file_with_path_lexed(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner("resources/general_test_files/incorrect-comment-spelling.bs").files
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs"]
        self.assertEqual(exp_result, result)

    def test_directory_with_path_lexed(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner("resources/general_test_files/sub_directory1_test_files").files
        exp_result = ["resources/general_test_files/sub_directory1_test_files/print.brs"]
        self.assertEqual(exp_result, result)

    def test_sub_directory_lexed(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner("resources/general_test_files").files
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs",
                      "resources/general_test_files/sub_directory1_test_files/print.brs",
                      "resources/general_test_files/sub_directory2_test_files/question-mark.brs"]
        self.assertEqual(exp_result, result)

    def test_sub_directory_ignored(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner("resources/general_ignore_test_files").files
        exp_result = ["resources/general_ignore_test_files/incorrect-comment-spelling.bs",
                      "resources/general_ignore_test_files/sub_directory2_test_files/question-mark.brs"]
        self.assertEqual(exp_result, result)
