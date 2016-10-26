import unittest
import os
import sys
from bslint.interface_handler import InterfaceHandler as InterfaceHandler
import bslint.constants as const
from io import StringIO

from filepaths import TESTS_RESOURCES_PATH


class TestInvalidBSLintJSON(unittest.TestCase):

    def test_printed_message(self):
        out = StringIO()
        interface_handler = InterfaceHandler(out)
        invalid_json_path = os.path.join(TESTS_RESOURCES_PATH, 'general_test_files/invalid_bslintrc_test_files/')
        sys.argv.pop()
        sys.argv.append(invalid_json_path)
        interface_handler.main()
        result = out.getvalue()
        out.close()
        self.assertEqual(result, const.ERROR_COLOUR + 'Unable to parse JSON in .bslintrc file' + const.END_COLOUR)