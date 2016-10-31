import unittest
import os

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
import bslint.lexer.commands as commands
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestSpacesAroundOperators(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()
    
    def setUp(self):
        spaces_around_operators_path = os.path.join(TESTS_CONFIG_PATH,
                                                    'spaces_around_operators/spaces-around-operators-config.json')
        self.config = bslint.load_config_file(user_filepath=spaces_around_operators_path,
                                              default_filepath=TEST_CONFIG_FILE_PATH)

    def test_correct_space_before(self):
        exp_result = None
        result = commands.check_spaces_around_operators("a = 1", 3)
        self.assertEqual(result, exp_result)

    def test_incorrect_space_before(self):
        exp_result = {"error_key": err_const.NO_SPACE_AROUND_OPERATORS, "error_params": [1]}
        result = commands.check_spaces_around_operators("a= 1", 1)
        self.assertEqual(result, exp_result)

    def test_spaces_after_operator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this =      "words"')
        self.assertEqual(exp_result, result[self.common.WARNINGS])

    def test_spaces_before_operator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this       = "words"')
        self.assertEqual(exp_result, result[self.common.WARNINGS])

    def test_correct_spaces_around_operator(self):
        exp_result = []
        result = Lexer().lex('this = "words"')
        self.assertEqual(exp_result, result[self.common.WARNINGS])

    def test_many_spaces_around_operator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this    =        "words"')
        self.assertEqual(exp_result, result[self.common.WARNINGS])

    def test_many_spaces_around_operator_with_config(self):
        three_spaces_around_operators_path = os.path.join(TESTS_CONFIG_PATH,
                                                    'spaces_around_operators/3-spaces-around-operators-config.json')
        bslint.load_config_file(user_filepath=three_spaces_around_operators_path)
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [3, 1])]
        result = Lexer().lex('this   =        "words"')
        self.assertEqual(exp_result, result[self.common.WARNINGS])

    def test_no_spaces_around_operator(self):
        exp_result = [error.get_message(err_const.NO_SPACE_AROUND_OPERATORS, [1, 1])]
        result = Lexer().lex('this="words"')
        self.assertEqual(exp_result, result[self.common.WARNINGS])
