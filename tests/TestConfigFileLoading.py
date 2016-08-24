import unittest
import src
import sys
from io import StringIO


class TestConfigFileLoading(unittest.TestCase):

    filepath_prefix = ''

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/config/"
        else:
            cls.filepath_prefix = "../resources/config/"

    def testReadJsonCorrectly(self):
        config_file =  self.filepath_prefix + "default-config.json"
        exp_res = 17
        config_json = src.read_json(config_file)
        result = len(config_json)
        self.assertEqual(result, exp_res)

    def testReadJsonBadFileName(self):
        config_file = self.filepath_prefix + "fig.json"
        with self.assertRaises(FileNotFoundError):
            src.read_json(config_file)

    def testLoadConfigFileCheckRead(self):
        exp_res = "Read styling config JSON correctly."
        out = StringIO()
        src.load_config_file(out=out)
        result = out.getvalue().strip()
        self.assertEqual(result, exp_res)

    def testDefaultConfigOverwritten(self):
        exp_res = 666
        config = src.load_config_file()
        result = config["max_line_length"]
        self.assertEqual(result, exp_res)

    def testDefaultConfigPersists(self):
        exp_res = True
        config = src.load_config_file()
        result = config["spellcheck"]
        self.assertEqual(result, exp_res)
