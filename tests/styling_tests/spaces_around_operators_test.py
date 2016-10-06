import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer


class TestSpacesAroundOperators(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    def setUp(self):
        self.config = bslint.load_config_file(user_filepath="spaces_around_operators/spaces-around-operators-config.json", default_filepath="test-config.json")

    def testCorrectSpaceBefore(self):
        exp_result = None
        result = commands.check_spaces_around_operators("a = 1", 3)
        self.assertEqual(result, exp_result)

    def testIncorrectSpaceBefore(self):
        exp_result = {"error_key": err_const.NO_SPACE_AROUND_OPERATORS, "error_params": [1]}
        result = commands.check_spaces_around_operators("a= 1", 1)
        self.assertEqual(result, exp_result)

    def testSpacesAfterOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this =      "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSpacesBeforeOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this       = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testCorrectSpacesAroundOperator(self):
        exp_result = []
        result = Lexer().lex('this = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this    =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperatorWithConfig(self):
        bslint.load_config_file("spaces_around_operators/3-spaces-around-operators-config.json")
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [3, 1])]
        result = Lexer().lex('this   =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testNoSpacesAroundOperator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this="words"')
        self.assertEqual(exp_result, result[self.WARNINGS])
