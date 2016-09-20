import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as err
import bslint.utilities.commands as commands
import bslint.lexer as lexer


class TestSkipLineCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    def testSkipLineCommandSkipTypo(self):
        config = bslint.load_config_file()
        commands.config = config
        exp_result = []
        result = lexer.lex("'BSLint_skip_line \nxgygu= 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandEmptyLine(self):
        exp_result = []
        result = lexer.lex("'BSLint_skip_line \n\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandWithTypo(self):
        config = bslint.load_config_file()
        commands.config = config
        exp_result = [err.get_message(err_const.TYPO_IN_CODE, [3])]
        result = lexer.lex("'BSLint_skip_line \ny=4\nxgygu = 22\n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandInactive(self):
        config = bslint.load_config_file("BSLintCommands/inactive-skip-line-config.json")
        commands.config = config
        exp_result = [err.get_message(err_const.TYPO_IN_CODE, [2])]
        result = lexer.lex("'BSLint_skip_line \nxgygu = 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])