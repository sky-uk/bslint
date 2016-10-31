import os
import unittest

import bslint
import bslint.error_messages.handler as error
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer as Lexer
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from filepaths import TRACE_TEST_FILES_PATH
from tests.resources.common.test_methods import CommonMethods as Common


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.trace_free_config_path = os.path.join(TESTS_CONFIG_PATH, 'trace_free/trace-free-config.json')
        cls.common = Common()

    def trace_free_runner(self, file, exp_result):
        file = open(file, "r+").read()
        result = Lexer().lex(file)
        self.assertEqual(result[self.common.WARNINGS], exp_result)
        self.assertEqual(result[self.common.STATUS], self.common.SUCCESS)

    def test_print(self):
        bslint.load_config_file(user_filepath=self.trace_free_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        print_file_path = os.path.join(TRACE_TEST_FILES_PATH, 'print.brs')
        self.trace_free_runner(print_file_path,
                               [error.get_message(err_const.TRACEABLE_CODE, [3])])

    def test_question_mark(self):
        bslint.load_config_file(user_filepath=self.trace_free_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        question_mark_file_path = os.path.join(TRACE_TEST_FILES_PATH, 'question-mark.brs')
        self.trace_free_runner(question_mark_file_path,
                               [error.get_message(err_const.TRACEABLE_CODE, [3])])

    def test_print_and_question_mark(self):
        bslint.load_config_file(user_filepath=self.trace_free_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        print_and_question_mark_file_path = os.path.join(TRACE_TEST_FILES_PATH,
                                                         'print-and-question-mark.brs')
        self.trace_free_runner(print_and_question_mark_file_path,
                               [error.get_message(err_const.TRACEABLE_CODE, [3]),
                                     error.get_message(err_const.TRACEABLE_CODE, [4])])

    def test_no_print_no_question_mark(self):
        bslint.load_config_file(user_filepath=self.trace_free_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        no_print_no_question_mark_file_path = os.path.join(TRACE_TEST_FILES_PATH,
                                                           'no-print-no-question-mark.brs')
        self.trace_free_runner(no_print_no_question_mark_file_path, [])

    def test_inactive_print_and_question_mark(self):
        bslint.load_config_file(default_filepath=TEST_CONFIG_FILE_PATH)
        print_and_question_mark_file_path = os.path.join(TRACE_TEST_FILES_PATH,
                                                         'print-and-question-mark.brs')
        self.trace_free_runner(print_and_question_mark_file_path, [])
