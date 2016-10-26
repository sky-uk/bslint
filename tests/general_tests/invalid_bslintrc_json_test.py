import unittest
import os
import bslint
import bslint.constants as const
from io import StringIO

from filepaths import TESTS_RESOURCES_PATH
from filepaths import DEFAULT_CONFIG_FILE_PATH


class TestInvalidBSLintJSON(unittest.TestCase):

    def test_printed_message(self):
        out = StringIO()
        invalid_json_path = os.path.join(TESTS_RESOURCES_PATH, 'general_test_files/invalid_bslintrc_test_files/.bslintrc')
        bslint.config_loader.load_config_file(invalid_json_path, DEFAULT_CONFIG_FILE_PATH, out)
        result = out.getvalue()
        out.close()
        self.assertEqual(result, const.ERROR_COLOUR + 'Unable to parse JSON in .bslintrc file' + const.END_COLOUR)
