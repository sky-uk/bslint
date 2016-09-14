import unittest
import os
import src
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import src.commands as commands


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../TraceTestFiles/")

    def testPRINT(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "Print.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testQuestionMark(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "QuestionMark.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testPrintAndQuestionMark(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3]),
                   self.error.get(ErrConst.TRACEABLE_CODE, [4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoPrintNoQuestionMark(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "NoPrintNoQuestionMark.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testInactivePrintAndQuestionMark(self):
        config = src.load_config_file(default="test-config.json")
        commands.config = config
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)