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
        result = bslint.bslint.runner("GeneralTestFiles/SubDirectory1TestFiles/Print.brs")
        exp_result = ["GeneralTestFiles/SubDirectory1TestFiles/Print.brs"]
        self.assertEqual(exp_result, result)

    def testBSFileWithPathLexed(self):
        result = bslint.bslint.runner("GeneralTestFiles/IncorrectCommentSpelling.bs")
        exp_result = ["GeneralTestFiles/IncorrectCommentSpelling.bs"]
        self.assertEqual(exp_result, result)

    def testDirectoryWithPathLexed(self):
        result = bslint.bslint.runner("GeneralTestFiles/SubDirectory1TestFiles")
        exp_result = ["GeneralTestFiles/SubDirectory1TestFiles/Print.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryLexed(self):
        result = bslint.bslint.runner("GeneralTestFiles")
        exp_result = ["GeneralTestFiles/IncorrectCommentSpelling.bs",
                      "GeneralTestFiles/SubDirectory1TestFiles/Print.brs",
                      "GeneralTestFiles/SubDirectory2TestFiles/QuestionMark.brs"]
        self.assertEqual(exp_result, result)

    def testSubDirectoryIgnored(self):
        result = bslint.bslint.runner("GeneralIgnoreTestFiles")
        exp_result = ["GeneralIgnoreTestFiles/IncorrectCommentSpelling.bs",
                      "GeneralIgnoreTestFiles/SubDirectory2TestFiles/QuestionMark.brs"]
        self.assertEqual(exp_result, result)