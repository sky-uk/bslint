import unittest
import os
from io import StringIO

import bslint
from bslint.messages import print_constants as print_const
from bslint.messages import handler as msg_handler
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import DEFAULT_CONFIG_FILE_PATH
from filepaths import CONFIG_PATH
from filepaths import TESTS_RESOURCES_PATH
from filepaths import TESTS_CONFIG_PATH


class TestConfigFileLoading(unittest.TestCase):

    def test_read_json_correctly(self):
        config_file = DEFAULT_CONFIG_FILE_PATH
        expected = 18
        config_json = bslint.read_json(config_file)
        result = len(config_json)
        self.assertEqual(expected, result)

    def test_read_json_bad_file_name(self):
        out = StringIO()
        config_file = os.path.join(CONFIG_PATH, 'fig.json')
        bslint.load_config_file(config_file, out=out)
        result = out.getvalue()
        out.close()
        expected = msg_handler.get_print_msg(print_const.NO_BSLINTRC)
        self.assertEqual(expected, result)

    def test_load_config_file_check_read(self):
        expected = ""
        out = StringIO()
        bslint.load_config_file(out=out)
        result = out.getvalue()
        out.close()
        self.assertEqual(expected, result)

    def test_default_config_overwritten(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        general_ignore_test_files_path = os.path.join(TESTS_RESOURCES_PATH, 'general_ignore_test_files')
        result = bslint.bslint.runner(general_ignore_test_files_path)
        self.assertFalse(result.config["check_trace_free"]["active"])
        self.assertEqual(["sub_directory1_test_files"], result.config["ignore"])

    def test_default_config_persists(self):
        expected = True
        config = bslint.load_config_file()
        result = config["spell_check"]["active"]
        self.assertEqual(expected, result)

    def test_read_json(self):
        indentation_config_path = os.path.join(TESTS_CONFIG_PATH, 'indentation/indentation-config.json')
        json = bslint.config_loader.read_json(indentation_config_path)
        expected = {'check_indentation': {'active': True, 'params': {'tab_size': 4, 'only_tab_indents': False}}}
        self.assertEqual(expected, json)
