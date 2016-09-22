import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
import bslint.utilities.commands as commands
import bslint.lexer as lexer


class TestSpacesAroundOperators(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.config = bslint.load_config_file(user="SpacesAroundOperators/spaces-around-operators-config.json", default="test-config.json")

    def testCorrectSpaceBefore(self):
        exp_result = None
        commands.config = self.config
        result = commands.check_spaces_around_operators("a = 1", 3)
        self.assertEqual(result, exp_result)

    def testIncorrectSpaceBefore(self):
        exp_result = {"error_key": err_const.NO_SPACE_AROUND_OPERATORS, "error_params": [1]}
        result = commands.check_spaces_around_operators("a= 1", 1)
        self.assertEqual(result, exp_result)

    def testSpacesAfterOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        result = lexer.lex('this =      "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSpacesBeforeOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        result = lexer.lex('this       = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testCorrectSpacesAroundOperator(self):
        exp_result = []
        commands.config = self.config
        result = lexer.lex('this = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        result = lexer.lex('this    =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperatorWithConfig(self):
        config = bslint.load_config_file("SpacesAroundOperators/3-spaces-around-operators-config.json")
        commands.config = config
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [3, 1])]
        result = lexer.lex('this   =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testNoSpacesAroundOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        result = lexer.lex('this="words"')
        self.assertEqual(exp_result, result[self.WARNINGS])