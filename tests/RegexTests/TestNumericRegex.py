import unittest
import src.Constants as const
import src


class TestNumericRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    def setUp(self):
        config = src.load_config_file(default='test-config.json')
        self.lexer = src.Lexer(config)
        self.regex_handler = src.RegexHandler()

    def testInteger(self):
        identifier = "1234"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.NUMERIC)

    def testDecimal(self):
        identifier = "123.456"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.NUMERIC)

    def testIntegerWithTrailingPoints(self):
        identifier = "123."
        exp_result = [('123', const.NUMERIC, 1), ('.', const.SPECIAL_OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalNumbers(self):
        identifier = "123.123.123"
        exp_result = [('123.123', const.NUMERIC, 1), ('.', const.SPECIAL_OPERATOR, 1), ('123', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testMultipleDecimalPoints(self):
        identifier = "123..123"
        exp_result = [('123', const.NUMERIC, 1), ('.', const.SPECIAL_OPERATOR, 1), ('.', const.SPECIAL_OPERATOR, 1),
                      ('123', const.NUMERIC, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result[self.TOKENS], exp_result)
