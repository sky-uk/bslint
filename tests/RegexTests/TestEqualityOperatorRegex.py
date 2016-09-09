import unittest
import src.Constants as const
import src


class TestEqualityOperatorRegex(unittest.TestCase):

    def setUp(self):
        self.regex_handler = src.RegexHandler()

    def testNotEquals(self):
        identifier = "<>"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLessThanOrEqual(self):
        identifier = "<="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLessThanOrEqualSec(self):
        identifier = "=<"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testGreaterThanOrEqual(self):
        identifier = ">="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testGreaterThanOrEqualSec(self):
        identifier = "=>"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testGreaterThan(self):
        identifier = ">"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLessThan(self):
        identifier = "<"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testMOD(self):
        identifier = "MOD "
        exp_result = "MOD"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testNOT(self):
        identifier = "NOT "
        exp_result = "NOT"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testAND(self):
        identifier = "AND "
        exp_result = "AND"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testOR(self):
        identifier = "OR "
        exp_result = "OR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)