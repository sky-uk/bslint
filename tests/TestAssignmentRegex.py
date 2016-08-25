import sys
import unittest

import Constants as const
import src


class TestAssignments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.string_file = src.main("./resources/BasicStringAssignment.txt")
            cls.int_file = src.main("./resources/BasicIntegerAssignment.txt")
        else:
            cls.string_file = src.main("../resources/BasicStringAssignment.txt")
            cls.int_file = src.main("../resources/BasicIntegerAssignment.txt")

    def setUp(self):
        self.lexer = src.Lexer()

    def testString(self):
        test_string = '"test123ID"'
        exp_result = [("test123ID", const.STRING, 1)]
        result = self.lexer.lex(test_string)
        self.assertEqual(result["Tokens"], exp_result)

    def testUnclosedQuotes(self):
        test_string = '"test123ID\n'
        exp_result = ([("Syntax error at: " + test_string, 1)])
        result = self.lexer.lex(test_string)
        self.assertEqual(result["Tokens"], exp_result)

    def testVariableAssignmentString(self):
        exp_result = [('string', const.ID, 1), ('=', const.OPERATOR, 1), ("words", const.STRING, 1)]
        result = self.lexer.lex(self.string_file)
        self.assertEqual(result["Tokens"], exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = [('""', const.STRING, 1)]
        result = self.lexer.lex(test_string)
        self.assertEqual(result["Tokens"], exp_result)