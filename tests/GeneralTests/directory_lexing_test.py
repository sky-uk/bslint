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
        result = bslint.bslint.runner("resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs")
        exp_result = ["resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs"]
        self.assertEqual(exp_result, result)

    def testBSFileWithPathLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/GeneralTestFiles/IncorrectCommentSpelling.bs")
        exp_result = ["resources/GeneralTestFiles/IncorrectCommentSpelling.bs"]
        self.assertEqual(exp_result, result)

    def testDirectoryWithPathLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/GeneralTestFiles/SubDirectory1TestFiles")
        exp_result = ["resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryLexed(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/GeneralTestFiles")
        exp_result = ["resources/GeneralTestFiles/IncorrectCommentSpelling.bs",
                      "resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs",
                      "resources/GeneralTestFiles/SubDirectory2TestFiles/QuestionMark.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryIgnored(self):
        bslint.load_config_file(default_filepath='test-config.json')
        result = bslint.bslint.runner("resources/GeneralIgnoreTestFiles")
        exp_result = ["resources/GeneralIgnoreTestFiles/IncorrectCommentSpelling.bs",
                      "resources/GeneralIgnoreTestFiles/SubDirectory2TestFiles/QuestionMark.brs"]
        self.assertEqual(exp_result, result)
