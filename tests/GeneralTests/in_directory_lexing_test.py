import os
import unittest

import bslint


class TestInDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/GeneralTestFiles/SubDirectory1TestFiles")
        os.chdir(cls.filepath_prefix)

    def testBRSFileWithoutPathLexed(self):
        config = bslint.load_config_file(default='test-config.json')
        bslint.commands.config = config
        result = bslint.bslint.runner("Print.brs")
        exp_result = ["Print.brs"]
        self.assertEqual(exp_result, result)

    def testDirectoryWithoutPathLexed(self):
        config = bslint.load_config_file(default='test-config.json')
        bslint.commands.config = config
        result = bslint.bslint.runner()
        exp_result = ["Print.brs"]
        self.assertEqual(exp_result, result)
