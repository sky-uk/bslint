import unittest
import sys
import src
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import src.commands as commands


class TestSpacesAroundOperators(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        cls.config = src.load_config_file(user="SpacesAroundOperators/spaces-around-operators-config.json", default="test-config.json")


    def testCorrectSpaceBefore(self):
        exp_result = None
        commands.config = self.config
        result = commands.check_spaces_around_operators("a = 1", 3)
        self.assertEqual(result, exp_result)

    def testIncorrectSpaceBefore(self):
        exp_result = {"error_key": ErrConst.NO_SPACE_AROUND_OPERATORS, "error_params": [1]}
        result = commands.check_spaces_around_operators("a= 1", 1)
        self.assertEqual(result, exp_result)

    def testSpacesAfterOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this =      "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSpacesBeforeOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this       = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testCorrectSpacesAroundOperator(self):
        exp_result = []
        commands.config = self.config
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this    =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperatorWithConfig(self):
        config = src.load_config_file("SpacesAroundOperators/3-spaces-around-operators-config.json")
        commands.config = config
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [3, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this   =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testNoSpacesAroundOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        commands.config = self.config
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this="words"')
        self.assertEqual(exp_result, result[self.WARNINGS])