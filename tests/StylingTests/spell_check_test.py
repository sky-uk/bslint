import unittest
import bslint
import bslint.constants as const
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os
import bslint.commands as commands


class TestSpellCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/StylingTestFiles/")

    def setUp(self):
        config = bslint.load_config_file(user='SpellCheck/spellcheck-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()

    def testM(self):
        test_string = "m"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testSingleLCase(self):
        test_string = "bad"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testCamelCase(self):
        test_string = "badGood"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testSingleUpperCase(self):
        test_string = "GOOD"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testSingleUnderscoreCamelCase(self):
        test_string = "bad_Good"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testSingleUnderscoreLowerCase(self):
        test_string = "bad_good"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testIncorrect(self):
        test_string = "bad_Good"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testNonLetter(self):
        test_string = "bad_Good$"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testStartLCaseCorrect(self):
        test_string = "Brother"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testStartUCaseIncorrect(self):
        test_string = "Badsfddsf"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testIncorrectSpelling(self):
        test_string = "sfgsdrgser"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testIncorrectCamelCase(self):
        test_string = "badGrgdrfdfg"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testRealFile(self):
        file_name = self.filepath_prefix + "SpellCheck.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [self.error.get(ErrConst.TYPO_IN_CODE, [2])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMisspelledCommentFromFile(self):
        file_name = self.filepath_prefix + "IncorrectCommentSpelling.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TYPO_IN_CODE, [1])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testUSDictionaryFailing(self):
        us_config = bslint.load_config_file(user='SpellCheck/us-spellcheck-config.json', default='test-config.json')
        commands.config = us_config
        commands._change_dict_lang(us_config["spell_check"]["params"]["dictionary"])
        self.lexer = bslint.Lexer()
        test_string = "specialised"
        exp_result = {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testUSDictionaryPassing(self):
        us_config = bslint.load_config_file(user='SpellCheck/us-spellcheck-config.json', default='test-config.json')
        commands.config = us_config
        commands._change_dict_lang(us_config["spell_check"]["params"]["dictionary"])
        self.lexer = bslint.Lexer()
        test_string = "specialized"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)
