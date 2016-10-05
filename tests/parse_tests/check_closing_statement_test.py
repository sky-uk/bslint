import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestCheckClosingStatement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.CLOSE_CURLY_BRACKET


    def check_operation_stack(self, token):
        try:
            result = Parser('').check_operation_stack(token)
        except:
            self.fail('Unexpected exception raised')


    def testFunctionValidStack(self):
        token = ('function', const.KEYWORD, const.FUNCTION, 1)
        self.check_operation_stack(token)

    def testWhileValidStack(self):
        token = ('while', const.KEYWORD, const.WHILE, 1)
        self.check_operation_stack(token)

    def testIfValidStack(self):
        token = ('if', const.KEYWORD, const.IF_STATEMENT, 1)
        self.check_operation_stack(token)

    def testForValidStack(self):
        token = ('for', const.KEYWORD, const.FOR, 1)
        self.check_operation_stack(token)

    def testForEachValidStack(self):
        token = ('for each', const.KEYWORD, const.FOR_EACH, 1)
        self.check_operation_stack(token)

    def testSubValidStack(self):
        token = ('sub', const.KEYWORD, const.SUB, 1)
        self.check_operation_stack(token)

    def testEndSubEmptyStack(self):
        token = ('end sub', const.KEYWORD, const.KEYWORD, 1)
        with self.assertRaises(ValueError):
            Parser('').check_operation_stack(token)

    def testEndWhileEmptyStack(self):
        token = ('end while', const.KEYWORD, const.KEYWORD, 1)
        with self.assertRaises(ValueError):
            Parser('').check_operation_stack(token)

    def testEndIfEmptyStack(self):
        token = ('end if', const.KEYWORD, const.KEYWORD, 1)
        with self.assertRaises(ValueError):
            Parser('').check_operation_stack(token)

    def testEndFunctionEmptyStack(self):
        token = ('end function', const.KEYWORD, const.KEYWORD, 1)
        with self.assertRaises(ValueError):
            Parser('').check_operation_stack(token)

    def testEndForEmptyStack(self):
        token = ('end for', const.KEYWORD, const.KEYWORD, 1)
        with self.assertRaises(ValueError):
            Parser('').check_operation_stack(token)
