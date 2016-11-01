import os
import unittest

from filepaths import TESTS_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.chdir(TESTS_PATH)
        cls.common = Common()

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
