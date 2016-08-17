import unittest
import src
import resources.Constants as const


class TestAssignments(unittest.TestCase):

    string_file = ''
    int_file = ''

    @classmethod
    def setUpClass(cls):
        cls.string_file = src.main("../resources/BasicStringAssignment.txt")
        cls.int_file = src.main("../resources/BasicIntegerAssignment.txt")

    def testString(self):
        test_string = '"test123ID"'
        exp_result = [("test123ID", const.STRING)]
        result = src.lexer(test_string)
        self.assertEqual(result, exp_result)

    def testVariableAssignmentString(self):
        exp_result = [('string', const.ID), ('=', const.STMT), ("words", const.STRING)]
        result = src.lexer(self.string_file)
        self.assertEqual(result, exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = [('""', const.STRING)]
        result = src.lexer(test_string)
        self.assertEqual(result, exp_result)