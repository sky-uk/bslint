import os
import unittest

import bslint
import bslint.constants as const
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer


class TestSpellCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")

    def setUp(self):
        bslint.load_config_file(user_filepath='spell_check/spellcheck-config.json', default_filepath='test-config.json')

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
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testIncorrectSpelling(self):
        test_string = "sfgsdrgser"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testIncorrectCamelCase(self):
        test_string = "badGrgdrfdfg"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testRealFile(self):
        file_name = self.filepath_prefix + "spell-check.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TYPO_IN_CODE, [2])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMisspelledCommentFromFile(self):
        file_name = self.filepath_prefix + "incorrect-comment-spelling.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [error.get_message(err_const.TYPO_IN_CODE, [1])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testUSDictionaryFailing(self):
        bslint.load_config_file(user_filepath='spell_check/us-spellcheck-config.json', default_filepath='test-config.json')
        commands._change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        test_string = "specialised"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def testUSDictionaryPassing(self):
        bslint.load_config_file(user_filepath='spell_check/us-spellcheck-config.json', default_filepath='test-config.json')
        commands._change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        test_string = "specialized"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)
