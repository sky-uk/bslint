import unittest
import os
import bslint
import bslint.messages.handler as msg_handler
import bslint.messages.error_constants as err_const
from tests.resources.common.test_methods import CommonMethods as Common
from filepaths import BSLINT_COMMAND_CONFIG_PATH
from filepaths import TEST_CONFIG_FILE_PATH


class TestSkipFileCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_skip_file_command_skip_start(self):
        active_skip_file_config_path = os.path.join(BSLINT_COMMAND_CONFIG_PATH, 'active-skip-file-config.json')
        bslint.load_config_file(user_filepath=active_skip_file_config_path)
        self.common.lex_warnings_match([], "'BSLint_skip_file \nxgygu= 22\n  y=4\n sdfsf=2 \n")

    def test_skip_file_command_skip_half_way(self):
        self.common.lex_warnings_match([], "one = 22\ntwo = 4\n'BSLint_skip_file \n sdfsf=2 \n")

    def test_skip_file_command_skip_start_inactive(self):
        inactive_skip_file_config_path = os.path.join(BSLINT_COMMAND_CONFIG_PATH, 'inactive-skip-file-config.json')
        bslint.load_config_file(user_filepath=inactive_skip_file_config_path, default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.lex_warnings_match([msg_handler.get_error_msg(err_const.TYPO_IN_CODE, [2]),
                                        msg_handler.get_error_msg(err_const.NO_SPACE_AROUND_OPERATORS, [1, 2])],
                                       "'BSLint_skip_file\nxgygu =22\ny = 4")

    def test_skip_file_command_skip_halfway_inactive(self):
        self.common.lex_warnings_match([], "one = 22\ntwo = 4\n'BSLint_skip_file\ntwo= 2\n")
