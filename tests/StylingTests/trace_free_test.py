import unittest
import os
import bslint
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import bslint.commands as commands


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../TraceTestFiles/")

    def testPRINT(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "Print.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testQuestionMark(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "QuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testPrintAndQuestionMark(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3]),
                   self.error.get(ErrConst.TRACEABLE_CODE, [4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoPrintNoQuestionMark(self):
        config = bslint.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "NoPrintNoQuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testInactivePrintAndQuestionMark(self):
        config = bslint.load_config_file(default="test-config.json")
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = bslint.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)