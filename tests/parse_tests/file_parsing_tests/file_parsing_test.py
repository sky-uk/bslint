import unittest

from bslint.parser.parser import Parser
from filepaths import TESTS_RESOURCES_PATH


class TestMultiLineReductionParse(unittest.TestCase):

    def test_simple_file(self):
        file = open(TESTS_RESOURCES_PATH + "/files_to_parse/simple_parsing.brs", "r+").read()
        parser = Parser()
        result = parser.parse(file)
        self.assertEqual("Success", result["Status"])

    def test_complex_file(self):
        file = open(TESTS_RESOURCES_PATH + "/files_to_parse/complex_parsing.brs", "r+").read()
        parser = Parser()
        result = parser.parse(file)
        self.assertEqual("Success", result["Status"])

    def test_if_inside_function(self):
        file = open(TESTS_RESOURCES_PATH + "/files_to_parse/if_stmt_inside_function.brs", "r+").read()
        parser = Parser()
        result = parser.parse(file)
        self.assertEqual("Success", result["Status"])
