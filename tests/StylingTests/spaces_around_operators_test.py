import unittest
import sys
import src
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst


class TestSpacesAroundOperators(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        cls.spacesAroundOperatorsCheck = src.SpacesAroundOperatorsCommand()
        cls.config = src.load_config_file(user="SpacesAroundOperators/spaces-around-operators-config.json", default="test-config.json")

    def testCorrectSpaceBefore(self):
        exp_result = None
        result = self.spacesAroundOperatorsCheck.execute({"characters": "a = 1",
                                                          "spaces_around_operators": 1})
        self.assertEqual(result, exp_result)

    def testIncorrectSpaceBefore(self):
        exp_result = {"error_key": ErrConst.NO_SPACE_AROUND_OPERATORS, "error_params": [1]}
        result = self.spacesAroundOperatorsCheck.execute({"characters": "a= 1",
                                                          "spaces_around_operators": 1})
        self.assertEqual(result, exp_result)

    def testSpacesAfterOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this =      "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSpacesBeforeOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this       = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testCorrectSpacesAroundOperator(self):
        exp_result = []
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this    =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperatorWithConfig(self):
        config = src.load_config_file("SpacesAroundOperators/3-spaces-around-operators-config.json")
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [3, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this   =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testNoSpacesAroundOperator(self):
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(self.config)
        result = self.lexer.lex('this="words"')
        self.assertEqual(exp_result, result[self.WARNINGS])