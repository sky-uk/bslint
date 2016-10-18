import os
import unittest

import bslint


class TestInDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/general_test_files/sub-directory1-test-files")
        os.chdir(cls.filepath_prefix)

    def test_brs_file_without_path_lexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("print.brs").files
        exp_result = ["print.brs"]
        self.assertEqual(exp_result, result)

    def test_directory_without_path_lexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner().files
        exp_result = ["print.brs"]
        self.assertEqual(exp_result, result)
