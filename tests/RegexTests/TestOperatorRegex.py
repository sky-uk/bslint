import unittest
import src.Constants as const
import src


class TestOperatorRegex(unittest.TestCase):

    def setUp(self):
        self.regex_handler = src.RegexHandler()

    def testAddEqual(self):
        identifier = "+="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testSubtractEqual(self):
        identifier = "-="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testMultiplyEqual(self):
        identifier = "*="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testDivideEqual(self):
        identifier = "/="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testAdd(self):
        identifier = "+"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testSubtract(self):
        identifier = "-"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testMultiply(self):
        identifier = "*"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testDivide(self):
        identifier = "/"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testExponent(self):
        identifier = "^"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLeftShiftAssign(self):
        identifier = "<<="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testRightShiftAssign(self):
        identifier = ">>="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLeftShift(self):
        identifier = "<<"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testRightShift(self):
        identifier = ">>"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testDivideInteger(self):
        identifier = "\="
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)