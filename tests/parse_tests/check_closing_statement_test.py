import unittest
from bslint import constants as const
from bslint.parser.parser import Parser
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error


class TestCheckClosingStatement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.preceding_token_type = const.CLOSE_CURLY_BRACKET

    def check_operation_stack(self, token):
        try:
            Parser('').check_operation_stack(token)
        except:
            self.fail('Unexpected exception raised')

    def raises_correct_error(self, token, expected):
        with self.assertRaises(ValueError) as ve:
            Parser('').check_operation_stack(token)
        self.assertEqual(err_const.UNMATCHED_TOKEN, ve.exception.args[0])
        self.assertEqual({"expected": expected, "actual": token[0]}, ve.exception.args[1])

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
        statement = 'end sub'
        token = (statement, const.KEYWORD, const.KEYWORD, 1)
        with self.assertRaises(ValueError) as ve:
            Parser('').check_operation_stack(token)
        self.assertEqual(err_const.UNMATCHED_TOKEN, ve.exception.args[0])
        self.assertEqual({"expected": None, "actual": statement}, ve.exception.args[1])

    def testEndWhileEmptyStack(self):
        token = ('end while', const.KEYWORD, const.KEYWORD, 1)
        self.raises_correct_error(token, None)

    def testEndIfEmptyStack(self):
        token = ('end if', const.KEYWORD, const.KEYWORD, 1)
        self.raises_correct_error(token, None)

    def testEndFunctionEmptyStack(self):
        token = ('end function', const.KEYWORD, const.KEYWORD, 1)
        self.raises_correct_error(token, None)

    def testEndForEmptyStack(self):
        token = ('end for', const.KEYWORD, const.KEYWORD, 1)
        self.raises_correct_error(token, None)
