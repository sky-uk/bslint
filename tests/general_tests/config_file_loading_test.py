import unittest
import bslint
import os
from io import StringIO


class TestConfigFileLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../../bslint/config/")
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/")

    def testReadJsonCorrectly(self):
        config_file = self.filepath_prefix + "default-config.json"
        exp_res = 16
        config_json = bslint.read_json(config_file)
        result = len(config_json)
        self.assertEqual(result, exp_res)

    def testReadJsonBadFileName(self):
        config_file = self.filepath_prefix + "fig.json"
        with self.assertRaises(FileNotFoundError):
            bslint.read_json(config_file)

    def testLoadConfigFileCheckRead(self):
        exp_res = ""
        out = StringIO()
        bslint.load_config_file(out=out)
        result = out.getvalue().strip()
        out.close()
        self.assertEqual(result, exp_res)

    def testDefaultConfigOverwritten(self):
        bslint.load_config_file(default_filepath='test-config.json')
        bslint.bslint.runner(self.tests_filepath_prefix + "general_ignore_test_files")
        self.assertEqual(False, bslint.config_loader.CONFIG["check_trace_free"]["active"])
        self.assertEqual(["sub-directory1-test-files"], bslint.config_loader.CONFIG["ignore"])

    def testDefaultConfigPersists(self):
        exp_res = True
        config = bslint.load_config_file()
        result = config["spell_check"]["active"]
        self.assertEqual(result, exp_res)
