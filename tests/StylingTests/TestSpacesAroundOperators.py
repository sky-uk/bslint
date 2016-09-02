import unittest
import sys
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestSpacesAroundOperators(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        cls.spacesAroundOperatorsCheck = src.SpacesAroundOperatorsCommand()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def testCorrectSpaceBefore(self):
        exp_result = None
        result = self.spacesAroundOperatorsCheck.execute({"line_number": 1,
                                                          "white_space": 1,
                                                          "on_operator": True,
                                                          "spaces_around_operators": 1})
        self.assertEqual(result, exp_result)

    def testIncorrectSpaceBefore(self):
        exp_result = self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])
        result = self.spacesAroundOperatorsCheck.execute({"line_number": 1,
                                                          "white_space": 3,
                                                          "on_operator": True,
                                                          "spaces_around_operators": 1})
        self.assertEqual(result, exp_result)

    def testSpacesAfterOperator(self):
        config = src.load_config_file()
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this =      "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSpacesBeforeOperator(self):
        config = src.load_config_file()
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this       = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testCorrectSpacesAroundOperator(self):
        config = src.load_config_file()
        exp_result = []
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this = "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperator(self):
        config = src.load_config_file()
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1]),
                      self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this    =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testManySpacesAroundOperatorWithConfig(self):
        config = src.load_config_file(self.filepath_prefix + "config/more-spaces-around-operators-config.json")
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [3, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this   =        "words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testNoSpacesAroundOperator(self):
        config = src.load_config_file()
        exp_result = [self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1]),
                      self.error.get(ErrConst.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this="words"')
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSpacesAroundOperatorWithComment(self):
        config = src.load_config_file()
        exp_result = []
        self.lexer = src.Lexer(config)
        result = self.lexer.lex('this = rem TODO ZRV Check')
        self.assertEqual(exp_result, result[self.WARNINGS])