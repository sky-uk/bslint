import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as err
from bslint.lexer import Lexer as Lexer


class TestSkipLineCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    def testSkipLineCommandSkipTypo(self):
        bslint.load_config_file()
        exp_result = []
        result = Lexer().lex("'BSLint_skip_line \nxgygu= 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandEmptyLine(self):
        exp_result = []
        result = Lexer().lex("'BSLint_skip_line \n\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandWithTypo(self):
        bslint.load_config_file()
        exp_result = [err.get_message(err_const.TYPO_IN_CODE, [3])]
        result = Lexer().lex("'BSLint_skip_line \ny=4\nxgygu = 22\n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandInactive(self):
        bslint.load_config_file("bslint_commands/inactive-skip-line-config.json")
        exp_result = [err.get_message(err_const.TYPO_IN_CODE, [2])]
        result = Lexer().lex("'BSLint_skip_line \nxgygu = 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])