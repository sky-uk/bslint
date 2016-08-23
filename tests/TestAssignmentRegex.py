import unittest
import src
import resources.Constants as const
import sys


class TestAssignments(unittest.TestCase):

    string_file = ''
    int_file = ''

    @classmethod
    def setUpClass(cls):
        cls.lexer = src.Lexer()
        if sys.argv[0].endswith('nosetests'):
            cls.string_file = src.main("./resources/BasicStringAssignment.txt")
            cls.int_file = src.main("./resources/BasicIntegerAssignment.txt")
        else:
            cls.string_file = src.main("../resources/BasicStringAssignment.txt")
            cls.int_file = src.main("../resources/BasicIntegerAssignment.txt")

    def testString(self):
        test_string = '"test123ID"'
        exp_result = [("test123ID", const.STRING, 0)]
        result = self.lexer.lex(test_string)
        self.assertEqual(result, exp_result)

    def testUnclosedQuotes(self):
        test_string = '"test123ID'
        exp_result = ("Errors", ["Syntax error at: " + test_string[:5]])
        result = self.lexer.lex(test_string)
        self.assertEqual(result, exp_result)

    def testVariableAssignmentString(self):
        exp_result = [('string', const.ID, 0), ('=', const.OPERATOR, 0), ("words", const.STRING, 0)]
        result = self.lexer.lex(self.string_file)
        self.assertEqual(result, exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = [('""', const.STRING, 0)]
        result = self.lexer.lex(test_string)
        self.assertEqual(result, exp_result)