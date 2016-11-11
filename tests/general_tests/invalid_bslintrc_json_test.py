import unittest
import os
from io import StringIO

import bslint
from bslint.messages import print_constants as print_const
from bslint.messages import handler as msg_handler
from filepaths import TESTS_RESOURCES_PATH
from filepaths import DEFAULT_CONFIG_FILE_PATH


class TestInvalidBSLintJSON(unittest.TestCase):
    def test_printed_message(self):
        out = StringIO()
        invalid_json_path = os.path.join(TESTS_RESOURCES_PATH,
                                         'general_test_files/invalid_bslintrc_test_files/.bslintrc')
        bslint.config_loader.load_config_file(invalid_json_path, DEFAULT_CONFIG_FILE_PATH, out)
        result = out.getvalue()
        out.close()
        self.assertEqual(result, msg_handler.get_print_msg(print_const.CANNOT_PARSE_BSLINTRC))
