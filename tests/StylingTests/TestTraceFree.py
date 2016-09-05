import unittest
import sys
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestTraceFree(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
            cls.tests_filepath_prefix = "./resources/TraceTestFiles/"
        else:
            cls.filepath_prefix = "../resources/"
            cls.tests_filepath_prefix = "../resources/TraceTestFiles/"

    def testPRINT(self):
        config = src.load_config_file(self.filepath_prefix + "config/trace-free-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "Print.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testQuestionMark(self):
        config = src.load_config_file(self.filepath_prefix + "config/trace-free-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "QuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.TRACEABLE_CODE, [3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testPrintAndQuestionMark(self):
        config = src.load_config_file(self.filepath_prefix + "config/trace-free-config.json")
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
        config = src.load_config_file(self.filepath_prefix + "config/trace-free-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "NoPrintNoQuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testInactivePrintAndQuestionMark(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "PrintAndQuestionMark.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)