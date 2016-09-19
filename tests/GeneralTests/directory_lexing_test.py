import unittest
import bslint
import os


class TestDirectoryLexing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../")
        os.chdir(cls.filepath_prefix)

    def testBRSFileWithPathLexed(self):
        result = bslint.bslint.runner("resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs")
        exp_result = ["resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs"]
        self.assertEqual(exp_result, result)

    def testBSFileWithPathLexed(self):
        result = bslint.bslint.runner("resources/GeneralTestFiles/IncorrectCommentSpelling.bs")
        exp_result = ["resources/GeneralTestFiles/IncorrectCommentSpelling.bs"]
        self.assertEqual(exp_result, result)

    def testDirectoryWithPathLexed(self):
        result = bslint.bslint.runner("resources/GeneralTestFiles/SubDirectory1TestFiles")
        exp_result = ["resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryLexed(self):
        result = bslint.bslint.runner("resources/GeneralTestFiles")
        exp_result = ["resources/GeneralTestFiles/IncorrectCommentSpelling.bs",
                      "resources/GeneralTestFiles/SubDirectory1TestFiles/Print.brs",
                      "resources/GeneralTestFiles/SubDirectory2TestFiles/QuestionMark.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryIgnored(self):
        result = bslint.bslint.runner("resources/GeneralIgnoreTestFiles")
        exp_result = ["resources/GeneralIgnoreTestFiles/IncorrectCommentSpelling.bs",
                      "resources/GeneralIgnoreTestFiles/SubDirectory2TestFiles/QuestionMark.brs"]
        self.assertEqual(exp_result, result)

    def testConfigurationLoaded(self):
        bslint.bslint.runner("resources/GeneralIgnoreTestFiles")
        self.assertEqual(False, bslint.config_loader.CONFIG["check_trace_free"]["active"])
        self.assertEqual(["SubDirectory1TestFiles"], bslint.config_loader.CONFIG["ignore"])
