import unittest
import sys
import src
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        if sys.argv[0].endswith('nosetests'):
            cls.tests_filepath_prefix = "./resources/TraceTestFiles/"
        else:
            cls.tests_filepath_prefix = "../resources/TraceTestFiles/"

    def testPRINT(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "Print.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testQuestionMark(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "QuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testPrintAndQuestionMark(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3]),
                   self.error.get(ErrConst.TRACEABLE_CODE, [4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testNoPrintNoQuestionMark(self):
        config = src.load_config_file(user="TraceFree/trace-free-config.json", default="test-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "NoPrintNoQuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testInactivePrintAndQuestionMark(self):
        config = src.load_config_file(default="test-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)