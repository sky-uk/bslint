import unittest
import os

import bslint
import bslint.error_messages.handler as err
import bslint.error_messages.constants as err_const
from tests.resources.common.test_methods import CommonMethods as Common
from filepaths import BSLINT_COMMAND_CONFIG_PATH


class TestSkipLineCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_skip_line_command_skip_typo(self):
        bslint.load_config_file()
        self.common.lex_warnings_match("'BSLint_skip_line \nxgygu= 22\ny = 4", [])

    def test_skip_line_command_empty_line(self):
        self.common.lex_warnings_match("'BSLint_skip_line \n\ny = 4", [])

    def test_skip_line_command_with_typo(self):
        bslint.load_config_file()
        self.common.lex_warnings_match("'BSLint_skip_line \ny=4\nxgygu = 22\n",
                                       [err.get_message(err_const.TYPO_IN_CODE, [3])])

    def test_skip_line_command_inactive(self):
        inactive_skip_line_config_path = os.path.join(BSLINT_COMMAND_CONFIG_PATH,
                                                      'inactive-skip-line-config.json')
        bslint.load_config_file(user_filepath=inactive_skip_line_config_path)
        self.common.lex_warnings_match("'BSLint_skip_line \nxgygu = 22\ny = 4",
                                       [err.get_message(err_const.TYPO_IN_CODE, [2])])
