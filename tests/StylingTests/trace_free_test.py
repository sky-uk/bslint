import os
import unittest

import bslint
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as error
import bslint.utilities.commands as commands
import bslint.lexer as lexer


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/TraceTestFiles/")

    def testPRINT(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        file_name = self.tests_filepath_prefix + "Print.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TRACEABLE_CODE, [3])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testQuestionMark(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        file_name = self.tests_filepath_prefix + "QuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TRACEABLE_CODE, [3])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testPrintAndQuestionMark(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [error.get_message(err_const.TRACEABLE_CODE, [3]),
                   error.get_message(err_const.TRACEABLE_CODE, [4])]
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoPrintNoQuestionMark(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        file_name = self.tests_filepath_prefix + "NoPrintNoQuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testInactivePrintAndQuestionMark(self):
        config = bslint.load_config_file(default="test-config.json")
        commands.config = config
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)