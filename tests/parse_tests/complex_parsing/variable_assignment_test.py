import unittest
from bslint.parser.parser import Parser


class TestVariableAssignment(unittest.TestCase):

    def testIdentifier(self):
        str_to_parse = "jack = 3"
        result = Parser().parse(str_to_parse)
        self.assertEqual("Success", result["Status"])

    def test2VariableDeclarations(self):
        str_to_parse = 'jack = 3\n zac = "no good at table tennis"'
        result = Parser().parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
