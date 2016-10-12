import os
import unittest

import bslint


class TestDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../")
        os.chdir(cls.filepath_prefix)

    def testBRSFileWithPathLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files/sub-directory1-test-files/print.brs").files
        exp_result = ["resources/general_test_files/sub-directory1-test-files/print.brs"]
        self.assertEqual(exp_result, result)

    def testBSFileWithPathLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files/incorrect-comment-spelling.bs").files
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs"]
        self.assertEqual(exp_result, result)

    def testDirectoryWithPathLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files/sub-directory1-test-files").files
        exp_result = ["resources/general_test_files/sub-directory1-test-files/print.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_test_files").files
        exp_result = ["resources/general_test_files/incorrect-comment-spelling.bs",
                      "resources/general_test_files/sub-directory1-test-files/print.brs",
                      "resources/general_test_files/sub-directory2-test-files/question-mark.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryIgnored(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/general_ignore_test_files").files
        exp_result = ["resources/general_ignore_test_files/incorrect-comment-spelling.bs",
                      "resources/general_ignore_test_files/sub-directory2-test-files/question-mark.brs"]
        self.assertEqual(exp_result, result)
