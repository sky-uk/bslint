import unittest
import src
import sys
import Constants as const


class TestSpellCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spellCheck = src.SpellCheckCommand()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def setUp(self):
        self.lexer = src.Lexer()

    def tearDown(self):
        self.lexer = None

    def testSingleLCase(self):
        test_string = "bad"
        exp_result = None
        result = self.spellCheck.execute({'token' : test_string, 'type': const.ID})
        self.assertEquals(result , exp_result)

    def testCamelCase(self):
        test_string = "badGood"
        exp_result = None
        result = self.spellCheck.execute({'token' : test_string, 'type': const.ID})
        self.assertEquals(result , exp_result)

    def testSingleUpperCase(self):
        test_string = "GOOD"
        exp_result = None
        result = self.spellCheck.execute({'token' : test_string, 'type': const.ID})
        self.assertEquals(result , exp_result)

    def testSingleUnderscore(self):
        test_string = "bad_Good"
        exp_result = None
        result = self.spellCheck.execute({'token' : test_string, 'type': const.ID})
        self.assertEquals(result , exp_result)

    def testIncorrect(self):
        test_string = "bad_Good"
        exp_result = None
        result = self.spellCheck.execute({'token' : test_string, 'type': const.ID})
        self.assertEquals(result , exp_result)

    def testNonLetter(self):
        test_string = "bad_Good$"
        exp_result = None
        result = self.spellCheck.execute({'token' : test_string, 'type': const.ID})
        self.assertEquals(result , exp_result)

    def testStartLCaseCorrect(self):
        test_string = "Brother"
        exp_result = None
        result = self.spellCheck.execute({'token': test_string, 'type': const.ID})
        self.assertEquals(result, exp_result)

    def testStartUCaseIncorrect(self):
        test_string = "Badsfddsf"
        exp_result = "Warning. You have spelling mistakes in your code. line number: 1"
        result = self.spellCheck.execute({'token': test_string, 'line_number': 1, 'type': const.ID})
        self.assertEquals(result, exp_result)

    def testIncorrectSpelling(self):
        test_string = "sfgsdrgser"
        exp_result = "Warning. You have spelling mistakes in your code. line number: 1"
        result = self.spellCheck.execute({'token' : test_string, 'line_number': 1, 'type': const.ID})
        self.assertEquals(result, exp_result)

    def testIncorrectCamelCase(self):
        test_string = "badGrgdrfdfg"
        exp_result = "Warning. You have spelling mistakes in your code. line number: 1"
        result = self.spellCheck.execute({'token' : test_string, 'line_number': 1, 'type': const.ID})
        self.assertEquals(result, exp_result)

    def testRealFile(self):
        file_name = self.filepath_prefix + "SpellCheck.brs"
        file = src.main(file_name)
        exp_res = ['Warning. You have spelling mistakes in your code. line number: 2']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)

    def testMisspelledCommentFromFile(self):
        file_name = self.filepath_prefix + "IncorrectCommentSpelling.brs"
        file = src.main(file_name)
        exp_res = ['Warning. You have spelling mistakes in your code. line number: 1']
        result = self.lexer.lex(file)
        self.assertEqual(result["Warnings"], exp_res)