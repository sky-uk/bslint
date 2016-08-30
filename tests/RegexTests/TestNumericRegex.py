import unittest

import Constants as const
import src


class TestNumericRegex(unittest.TestCase):
    
    TOKENS = 'Tokens'
    
    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testInteger(self):
        identifier = "1234"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.NUMERIC)

    def testDecimal(self):
        identifier = "123.456"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.NUMERIC)

    def testIntegerWithTrailingPoints(self):
        identifier = "123."
        exp_result = [('123', const.NUMERIC, 1), ('.', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalNumbers(self):
        identifier = "123.123.123"
        exp_result = [('123.123', const.NUMERIC, 1), ('.', const.OPERATOR, 1), ('123', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalPoints(self):
        identifier = "123..123"
        exp_result = [('123', const.NUMERIC, 1), ('.', const.OPERATOR, 1), ('.', const.OPERATOR, 1), ('123', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

