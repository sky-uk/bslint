import unittest
import src
import sys
import src.Constants as const
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestSpellCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'
    TOKEN = "token"
    TYPE = "type"
    LINE_NUMBER = "line_number"

    @classmethod
    def setUpClass(cls):
        cls.spellCheck = src.SpellCheckCommand()
        cls.error = Err.ErrorMessageHandler()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/StylingTestFiles/"
        else:
            cls.filepath_prefix = "../resources/StylingTestFiles/"

    def setUp(self):
        self.config = src.load_config_file(user='SpellCheck/spellcheck-config.json', default='test-config.json')
        self.lexer = src.Lexer(self.config)

    def testSingleLCase(self):
        test_string = "bad"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testCamelCase(self):
        test_string = "badGood"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testSingleUpperCase(self):
        test_string = "GOOD"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testSingleUnderscoreCamelCase(self):
        test_string = "bad_Good"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testSingleUnderscoreLowerCase(self):
        test_string = "bad_good"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testIncorrect(self):
        test_string = "bad_Good"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testNonLetter(self):
        test_string = "bad_Good$"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testStartLCaseCorrect(self):
        test_string = "Brother"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testStartUCaseIncorrect(self):
        test_string = "Badsfddsf"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.LINE_NUMBER: 1, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testIncorrectSpelling(self):
        test_string = "sfgsdrgser"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.LINE_NUMBER: 1, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testIncorrectCamelCase(self):
        test_string = "badGrgdrfdfg"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.LINE_NUMBER: 1, self.TYPE: const.ID, **self.config["spell_check"]["params"]})
        self.assertEqual(result, exp_result)

    def testRealFile(self):
        file_name = self.filepath_prefix + "SpellCheck.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TYPO_IN_CODE, [2])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMisspelledCommentFromFile(self):
        file_name = self.filepath_prefix + "IncorrectCommentSpelling.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TYPO_IN_CODE, [1])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)