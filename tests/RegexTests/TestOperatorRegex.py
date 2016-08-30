import unittest

import Constants as const
import src


class TestOperatorRegex(unittest.TestCase):

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testAddEqual(self):
        identifier = "+="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testSubtractEqual(self):
        identifier = "-="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testMultiplyEqual(self):
        identifier = "*="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testDivideEqual(self):
        identifier = "/="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testAdd(self):
        identifier = "+"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testSubtract(self):
        identifier = "-"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testMultiply(self):
        identifier = "*"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testDivide(self):
        identifier = "/"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testExponent(self):
        identifier = "^"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testLeftShiftAssign(self):
        identifier = "<<="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testRightShiftAssign(self):
        identifier = ">>="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testLeftShift(self):
        identifier = "<<"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testRightShift(self):
        identifier = ">>"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)

    def testDivideInteger(self):
        identifier = "\="
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.OPERATOR)