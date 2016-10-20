import os
import unittest

import bslint
import bslint.constants as const
import bslint.error_messages.constants as err_const
import bslint.error_messages.handler as error
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import STYLING_TEST_FILES_PATH


class TestSpellCheck(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")

    def setUp(self):
        spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                    'spell_check/spellcheck-config.json')
        bslint.load_config_file(user_filepath=spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)

    def test_m(self):
        test_string = "m"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_single_lcase(self):
        test_string = "bad"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_camel_case(self):
        test_string = "badGood"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_single_upper_case(self):
        test_string = "GOOD"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_single_underscore_camel_case(self):
        test_string = "bad_Good"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_single_underscore_lower_case(self):
        test_string = "bad_good"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_incorrect(self):
        test_string = "bad_Good"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_non_letter(self):
        test_string = "bad_Good$"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_start_lcase_correct(self):
        test_string = "Brother"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_start_ucase_incorrect(self):
        test_string = "Badsfddsf"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_incorrect_spelling(self):
        test_string = "sfgsdrgser"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_incorrect_camel_case(self):
        test_string = "badGrgdrfdfg"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_real_file(self):
        spell_check_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'spell-check.brs')
        file = open(spell_check_file_path, "r+").read()
        exp_res = [error.get_message(err_const.TYPO_IN_CODE, [2])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_misspelled_comment_from_file(self):
        incorrect_comment_spelling_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'incorrect-comment-spelling.brs')
        file = open(incorrect_comment_spelling_file_path, "r+").read()
        self.assertNotEqual(file, "")
        exp_res = [error.get_message(err_const.TYPO_IN_CODE, [1])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def test_us_dictionary_failing(self):
        us_spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/us-spellcheck-config.json')
        bslint.load_config_file(user_filepath=us_spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        commands._change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        test_string = "specialised"
        exp_result = {"error_key": err_const.TYPO_IN_CODE, "error_params": []}
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)

    def test_us_dictionary_passing(self):
        us_spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/us-spellcheck-config.json')
        bslint.load_config_file(user_filepath=us_spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        commands._change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        test_string = "specialized"
        exp_result = None
        result = commands.check_spelling(test_string, const.ID)
        self.assertEqual(result, exp_result)
