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
from tests.resources.common.test_methods import CommonMethods as Common


class TestSpellCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")
        cls.common = Common()

    def setUp(self):
        spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH,
                                                    'spell_check/spellcheck-config.json')
        bslint.load_config_file(user_filepath=spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)

    def check_spell_check(self, input, exp_result):
        result = commands.check_spelling(input, const.ID)
        self.assertEqual(result, exp_result)

    def test_m(self):
        self.check_spell_check("m", None)

    def test_single_lcase(self):
        self.check_spell_check("bad", None)

    def test_camel_case(self):
        self.check_spell_check("badGood", None)

    def test_single_upper_case(self):
        self.check_spell_check("GOOD", None)

    def test_single_underscore_camel_case(self):
        self.check_spell_check("bad_Good", None)

    def test_single_underscore_lower_case(self):
        self.check_spell_check("bad_good", None)

    def test_non_letter(self):
        self.check_spell_check("bad_Good$", None)

    def test_start_ucase_correct(self):
        self.check_spell_check("Brother", None)

    def test_start_ucase_incorrect(self):
        self.check_spell_check("Badsfddsf", {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_incorrect_spelling(self):
        self.check_spell_check("sfgsdrgser",
                               {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_incorrect_camel_case(self):
        self.check_spell_check("badGrgdrfdfg",
                               {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_real_file(self):
        spell_check_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'spell-check.brs')
        file = open(spell_check_file_path, "r+").read()
        exp_res = [error.get_message(err_const.TYPO_IN_CODE, [2])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.common.WARNINGS], exp_res)
        self.assertEqual(result[self.common.STATUS], self.common.SUCCESS)

    def test_misspelled_comment_from_file(self):
        incorrect_comment_spelling_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'incorrect-comment-spelling.brs')
        file = open(incorrect_comment_spelling_file_path, "r+").read()
        self.assertNotEqual(file, "")
        exp_res = [error.get_message(err_const.TYPO_IN_CODE, [1])]
        result = Lexer().lex(file)
        self.assertEqual(result[self.common.WARNINGS], exp_res)
        self.assertEqual(result[self.common.STATUS], self.common.SUCCESS)

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
