import sys
import unittest

import Constants as const
import src


class TestStringRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.string_file = src.main("./resources/BasicStringAssignment.txt")
            cls.multi_line_file = src.main("./resources/MultilineAssignment.txt")
        else:
            cls.string_file = src.main("../resources/BasicStringAssignment.txt")
            cls.multi_line_file = src.main("../resources/MultilineAssignment.txt")

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)

    def testString(self):
        test_string = '"test123ID"'
        result, regex_type = self.lexer.regex_handler(test_string)
        self.assertEqual(test_string, result.group())
        self.assertEqual(regex_type, const.STRING)

    def testUnclosedQuotes(self):
        test_string = '"test123ID\n'
        exp_result = "NO MATCH FOUND"
        with self.assertRaises(ValueError):
            result = self.lexer.regex_handler(test_string)
            self.assertEqual(exp_result, result)

    def testVariableAssignmentString(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1)]
        result = self.lexer.lex(self.string_file)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = '""'
        result, regex_type = self.lexer.regex_handler(test_string)
        self.assertEqual(test_string, result.group())
        self.assertEqual(regex_type, const.STRING)

    def testMultilineAssignment(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1),
                      ('teststring', const.ID, 2), ('=', const.OPERATOR, 2), ("this is words", const.STRING, 2)]
        result = self.lexer.lex(self.multi_line_file)
        self.assertEqual(result[self.TOKENS], exp_result)