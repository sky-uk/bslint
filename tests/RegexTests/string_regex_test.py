import unittest
import bslint
import bslint.constants as const
import os
import bslint.utilities.regex_handler as regex_handler
from bslint.lexer import Lexer as Lexer


class TestStringRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.string_file = bslint.get_string_to_parse(os.path.join(this_dir, "../resources/LexingTestFiles/BasicStringAssignment.txt"))
        cls.multi_line_file = bslint.get_string_to_parse(
            os.path.join(this_dir, "../resources/StylingTestFiles/MultilineAssignment.txt"))

    def testString(self):
        test_string = '"test123ID"'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(), test_string)
        self.assertEqual(result["token_type"], const.STRING)

    def testUnclosedQuotes(self):
        test_string = '"test123ID\n'
        with self.assertRaises(ValueError):
            result = regex_handler.find_match(test_string)
            self.assertEqual(result["match"].group(), test_string)
            self.assertEqual(result["token_type"], const.STRING)

    def testVariableAssignmentString(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1)]
        result = Lexer(self.string_file).lex()
        self.assertEqual(result[self.TOKENS], exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = '""'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.STRING)

    def testMultilineAssignment(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1),
                      ('test_String', const.ID, 2), ('=', const.OPERATOR, 2), ("this is words", const.STRING, 2)]
        result = Lexer(self.multi_line_file).lex()
        self.assertEqual(result[self.TOKENS], exp_result)
