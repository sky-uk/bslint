import os
import unittest

import bslint
import bslint.messages.error_constants as err_const
import bslint.messages.handler as error
import bslint.lexer.commands as commands
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import STYLING_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestSpellCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir = os.path.dirname(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")
        cls.common = Common()

    def setUp(self):
        spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/spellcheck-config.json')
        bslint.load_config_file(user_filepath=spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)

    def test_m(self):
        self.common.spell_check(None, "m")

    def test_single_lcase(self):
        self.common.spell_check(None, "bad")

    def test_camel_case(self):
        self.common.spell_check(None, "badGood")

    def test_single_upper_case(self):
        self.common.spell_check(None, "GOOD")

    def test_single_underscore_camel_case(self):
        self.common.spell_check(None, "bad_Good")

    def test_single_underscore_lower_case(self):
        self.common.spell_check(None, "bad_good")

    def test_non_letter(self):
        self.common.spell_check(None, "bad_Good$")

    def test_start_ucase_correct(self):
        self.common.spell_check(None, "Brother")

    def test_start_ucase_incorrect(self):
        self.common.spell_check({"error_key": err_const.TYPO_IN_CODE, "error_params": []}, "Badsfddsf")

    def test_incorrect_spelling(self):
        self.common.spell_check({"error_key": err_const.TYPO_IN_CODE, "error_params": []}, "sfgsdrgser")

    def test_incorrect_camel_case(self):
        self.common.spell_check({"error_key": err_const.TYPO_IN_CODE, "error_params": []}, "badGrgdrfdfg")

    def test_real_file(self):
        spell_check_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'spell-check.brs')
        self.common.lex_file([error.get_error_msg(err_const.TYPO_IN_CODE, [2])], spell_check_file_path)

    def test_misspelled_comment_from_file(self):
        incorrect_comment_spelling_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'incorrect-comment-spelling.brs')
        self.common.lex_file([error.get_error_msg(err_const.TYPO_IN_CODE, [1])], incorrect_comment_spelling_file_path)

    def test_us_dictionary_failing(self):
        us_spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/us-spellcheck-config.json')
        bslint.load_config_file(user_filepath=us_spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        commands.change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        self.common.spell_check({"error_key": err_const.TYPO_IN_CODE, "error_params": []}, "specialised")

    def test_us_dictionary_passing(self):
        us_spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/us-spellcheck-config.json')
        bslint.load_config_file(user_filepath=us_spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        commands.change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        self.common.spell_check(None, "specialized")
