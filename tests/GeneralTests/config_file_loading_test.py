import unittest
import bslint
import os
from io import StringIO


class TestConfigFileLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../../bslint/config/")

    def testReadJsonCorrectly(self):
        config_file = self.filepath_prefix + "default-config.json"
        exp_res = 15
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
        self.assertEqual(result, exp_res)

    def testDefaultConfigOverwritten(self):
        exp_res = 666
        config = bslint.load_config_file()
        result = config["max_line_length"]["params"]["max_line_length"]
        self.assertEqual(result, exp_res)

    def testDefaultConfigPersists(self):
        exp_res = True
        config = bslint.load_config_file()
        result = config["spell_check"]["active"]
        self.assertEqual(result, exp_res)
