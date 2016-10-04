import unittest
import bslint
import bslint.constants as const
import os
import bslint.utilities.regex_handler as regex_handler
import bslint.lexer as lexer


class TestStringRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.string_file = bslint.get_string_to_parse(
            os.path.join(this_dir, "../resources/LexingTestFiles/BasicStringAssignment.txt"))
        cls.multi_line_file = bslint.get_string_to_parse(
            os.path.join(this_dir, "../resources/StylingTestFiles/MultilineAssignment.txt"))

    def testString(self):
        test_string = '"test123ID"'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(), test_string)
        self.assertEqual(result["token_lexer_type"], const.STRING)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testUnclosedQuotes(self):
        test_string = '"test123ID\n'
        with self.assertRaises(ValueError):
            result = regex_handler.find_match(test_string)
            self.assertEqual(result["match"].group(), test_string)
            self.assertEqual(result["token_lexer_type"], const.STRING)
            self.assertEqual(result["token_parser_type"], const.VALUE)

    def testVariableAssignmentString(self):
        exp_result = [('myString', const.ID, const.ID, 1), ('=', const.OPERATOR, const.EQUALS, 1),
                      ("words", const.STRING, const.VALUE, 1)]
        result = lexer.lex(self.string_file)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = '""'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.STRING)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testMultilineAssignment(self):
        exp_result = [('myString', const.ID, const.ID, 1), ('=', const.OPERATOR, const.EQUALS, 1),
                      ("words", const.STRING, const.VALUE, 1),
                      ('test_String', const.ID, const.ID, 2), ('=', const.OPERATOR, const.EQUALS, 2),
                      ("this is words", const.STRING, const.VALUE, 2)]
        result = lexer.lex(self.multi_line_file)
        self.assertEqual(result[self.TOKENS], exp_result)
