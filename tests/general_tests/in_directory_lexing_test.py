import os
import unittest

import bslint
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_RESOURCES_PATH


class TestInDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        in_directory_lexing_path = os.path.join(TESTS_RESOURCES_PATH, 'general_test_files/sub_directory1_test_files')
        os.chdir(in_directory_lexing_path)

    def test_brs_file_without_path_lexed(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        runner = bslint.bslint.runner()
        result = runner.files
        runner.join()
        exp_result = ["print.brs"]
        self.assertEqual(exp_result, result)

    def test_directory_without_path_lexed(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        result = bslint.bslint.runner().files
        exp_result = ["print.brs"]
        self.assertEqual(exp_result, result)
