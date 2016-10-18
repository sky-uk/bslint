import os
import unittest

import bslint


class TestDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../")
        os.chdir(cls.filepath_prefix)

    def test_brs_file_with_path_lexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files/sub-directory1-test-files/print.brs").files
        exp_result = ["resources/general_test_files/sub-directory1-test-files/print.brs"]
        self.assertEqual(exp_result, result)

    def test_bs_file_with_path_lexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files/incorrect-comment-spelling.bs").files
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs"]
        self.assertEqual(exp_result, result)

    def test_directory_with_path_lexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files/sub-directory1-test-files").files
        exp_result = ["resources/general_test_files/sub-directory1-test-files/print.brs"]
        self.assertEqual(exp_result, result)

    def test_sub_directory_lexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files").files
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs",
                      "resources/general_test_files/sub-directory1-test-files/print.brs",
                      "resources/general_test_files/sub-directory2-test-files/question-mark.brs"]
        self.assertEqual(exp_result, result)

    def test_sub_directory_ignored(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_ignore_test_files").files
        exp_result = ["resources/general_ignore_test_files/incorrect-comment-spelling.bs",
                      "resources/general_ignore_test_files/sub-directory2-test-files/question-mark.brs"]
        self.assertEqual(exp_result, result)
