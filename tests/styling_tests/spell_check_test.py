import os
import unittest

import bslint
import bslint.error_messages.constants as err_const
import bslint.error_messages.handler as error
import bslint.lexer.commands as commands
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
        spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/spellcheck-config.json')
        bslint.load_config_file(user_filepath=spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)

    def test_m(self):
        self.common.spell_check("m", None)

    def test_single_lcase(self):
        self.common.spell_check("bad", None)

    def test_camel_case(self):
        self.common.spell_check("badGood", None)

    def test_single_upper_case(self):
        self.common.spell_check("GOOD", None)

    def test_single_underscore_camel_case(self):
        self.common.spell_check("bad_Good", None)

    def test_single_underscore_lower_case(self):
        self.common.spell_check("bad_good", None)

    def test_non_letter(self):
        self.common.spell_check("bad_Good$", None)

    def test_start_ucase_correct(self):
        self.common.spell_check("Brother", None)

    def test_start_ucase_incorrect(self):
        self.common.spell_check("Badsfddsf", {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_incorrect_spelling(self):
        self.common.spell_check("sfgsdrgser",
                                {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_incorrect_camel_case(self):
        self.common.spell_check("badGrgdrfdfg",
                                {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_real_file(self):
        spell_check_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'spell-check.brs')
        self.common.lex_file(spell_check_file_path, [error.get_message(err_const.TYPO_IN_CODE, [2])])

    def test_misspelled_comment_from_file(self):
        incorrect_comment_spelling_file_path = os.path.join(STYLING_TEST_FILES_PATH, 'incorrect-comment-spelling.brs')
        self.common.lex_file(incorrect_comment_spelling_file_path, [error.get_message(err_const.TYPO_IN_CODE, [1])])

    def test_us_dictionary_failing(self):
        us_spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/us-spellcheck-config.json')
        bslint.load_config_file(user_filepath=us_spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        commands._change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        self.common.spell_check("specialised", {"error_key": err_const.TYPO_IN_CODE, "error_params": []})

    def test_us_dictionary_passing(self):
        us_spellcheck_config_path = os.path.join(TESTS_CONFIG_PATH, 'spell_check/us-spellcheck-config.json')
        bslint.load_config_file(user_filepath=us_spellcheck_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        commands._change_dict_lang(bslint.config_loader.CONFIG["spell_check"]["params"]["dictionary"])
        self.common.spell_check("specialized", None)
