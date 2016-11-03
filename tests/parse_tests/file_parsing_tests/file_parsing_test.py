import unittest

from bslint.parser.parser import Parser
from filepaths import TESTS_RESOURCES_PATH


class TestMultiLineReductionParse(unittest.TestCase):
    def test_simple_file(self):
        file = open(TESTS_RESOURCES_PATH + "/files_to_parse/simple_parsing.brs", "r+").read()
        parser = Parser()
        result = parser.parse(file)
        self.assertEqual("Success", result["Status"])

