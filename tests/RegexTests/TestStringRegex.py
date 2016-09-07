import sys
import unittest
import Constants as const
import src


class TestStringRegex(unittest.TestCase):

    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        cls.regex_handler = src.RegexHandler()
        if sys.argv[0].endswith('nosetests'):
            cls.string_file = src.main("./resources/LexingTestFiles/BasicStringAssignment.txt")
            cls.multi_line_file = src.main("./resources/StylingTestFiles/MultilineAssignment.txt")
        else:
            cls.string_file = src.main("../resources/LexingTestFiles/BasicStringAssignment.txt")
            cls.multi_line_file = src.main("../resources/StylingTestFiles/MultilineAssignment.txt")

    def setUp(self):
        config = src.load_config_file(default='test-config.json')
        self.lexer = src.Lexer(config)

    def testString(self):
        test_string = '"test123ID"'
        result = self.regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(), test_string)
        self.assertEqual(result["token_type"], const.STRING)

    def testUnclosedQuotes(self):
        test_string = '"test123ID\n'
        exp_result = "NO MATCH FOUND"
        with self.assertRaises(ValueError):
            result = self.regex_handler.find_match(test_string)
            self.assertEqual(result["match"].group(), test_string)
            self.assertEqual(result["token_type"], const.STRING)

    def testVariableAssignmentString(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1)]
        result = self.lexer.lex(self.string_file)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = '""'
        result = self.regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.STRING)

    def testMultilineAssignment(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1),
                      ('test_String', const.ID, 2), ('=', const.OPERATOR, 2), ("this is words", const.STRING, 2)]
        result = self.lexer.lex(self.multi_line_file)
        self.assertEqual(result[self.TOKENS], exp_result)