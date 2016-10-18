import unittest

import bslint
import bslint.error_messages.handler as err
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer


class TestSkipLineCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    def test_skip_line_command_skip_typo(self):
        bslint.load_config_file()
        exp_result = []
        result = Lexer().lex("'BSLint_skip_line \nxgygu= 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def test_skip_line_command_empty_line(self):
        exp_result = []
        result = Lexer().lex("'BSLint_skip_line \n\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def test_skip_line_command_with_typo(self):
        bslint.load_config_file()
        exp_result = [err.get_message(err_const.TYPO_IN_CODE, [3])]
        result = Lexer().lex("'BSLint_skip_line \ny=4\nxgygu = 22\n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def test_skip_line_command_inactive(self):
        bslint.load_config_file("bslint_commands/inactive-skip-line-config.json")
        exp_result = [err.get_message(err_const.TYPO_IN_CODE, [2])]
        result = Lexer().lex("'BSLint_skip_line \nxgygu = 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])