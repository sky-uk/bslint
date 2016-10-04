import unittest
from bslint.parser.parser import Parser


class TestVariableAssignment(unittest.TestCase):

    def testIdentifier(self):
        str_to_parse = "jack = +1"
        result = Parser().parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
