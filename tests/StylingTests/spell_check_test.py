import unittest
import enchant
import src
import sys
import src.constants as const
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst


class TestSpellCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'
    TOKEN = "token"
    TYPE = "type"
    LINE_NUMBER = "line_number"
    COMBINED_DICTIONARY = "combined_dictionary"

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
        self.dictionary = self.config["spell_check"]["params"]["dictionary"]
        self.personal_words_list = self.lexer.personal_words_filepath()
        self.combined_dictionary = enchant.DictWithPWL(self.dictionary, self.personal_words_list)

    def testM(self):
        test_string = "m"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testSingleLCase(self):
        test_string = "bad"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testCamelCase(self):
        test_string = "badGood"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testSingleUpperCase(self):
        test_string = "GOOD"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testSingleUnderscoreCamelCase(self):
        test_string = "bad_Good"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testSingleUnderscoreLowerCase(self):
        test_string = "bad_good"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testIncorrect(self):
        test_string = "bad_Good"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testNonLetter(self):
        test_string = "bad_Good$"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testStartLCaseCorrect(self):
        test_string = "Brother"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testStartUCaseIncorrect(self):
        test_string = "Badsfddsf"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.LINE_NUMBER: 1, self.TYPE: const.ID,
             self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testIncorrectSpelling(self):
        test_string = "sfgsdrgser"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.LINE_NUMBER: 1, self.TYPE: const.ID,
             self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testIncorrectCamelCase(self):
        test_string = "badGrgdrfdfg"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.LINE_NUMBER: 1, self.TYPE: const.ID,
             self.COMBINED_DICTIONARY: self.combined_dictionary})
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

    def testUSDictionaryFailing(self):
        us_config = src.load_config_file(user='SpellCheck/us-spellcheck-config.json', default='test-config.json')
        self.lexer = src.Lexer(us_config)
        self.dictionary = us_config["spell_check"]["params"]["dictionary"]
        self.personal_words_list = self.lexer.personal_words_filepath()
        self.combined_dictionary = enchant.DictWithPWL(self.dictionary, self.personal_words_list)
        test_string = "specialised"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)

    def testUSDictionaryPassing(self):
        us_config = src.load_config_file(user='SpellCheck/us-spellcheck-config.json', default='test-config.json')
        self.lexer = src.Lexer(us_config)
        self.dictionary = us_config["spell_check"]["params"]["dictionary"]
        self.personal_words_list = self.lexer.personal_words_filepath()
        self.combined_dictionary = enchant.DictWithPWL(self.dictionary, self.personal_words_list)
        test_string = "specialized"
        exp_result = None
        result = self.spellCheck.execute(
            {self.TOKEN: test_string, self.TYPE: const.ID, self.COMBINED_DICTIONARY: self.combined_dictionary})
        self.assertEqual(result, exp_result)
