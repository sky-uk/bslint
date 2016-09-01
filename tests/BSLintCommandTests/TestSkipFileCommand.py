import unittest
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst
import sys


class TestSkipFileCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        cls.indentCheck = src.CheckIndentationCommand()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def testSkipFileCommandSkipStart(self):
        config = src.load_config_file()
        src.lexer = src.Lexer(config)
        exp_result = []
        result = src.lexer.lex("'BSLint_skip_file \nxgygu= 22\ny=4\n sdfsf=2 \n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipHalfWay(self):
        config = src.load_config_file()
        src.lexer = src.Lexer(config)
        exp_result = []
        result = src.lexer.lex("one= 22\ntwo=4\n'BSLint_skip_file \n sdfsf=2 \n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipStartInactive(self):
        config = src.load_config_file(self.filepath_prefix + "config/inactive-skip-file-config.json")
        src.lexer = src.Lexer(config)
        exp_result = [self.error.get(ErrConst.TYPO_IN_CODE, [2])]
        result = src.lexer.lex("'BSLint_skip_file \nxgygu= 22\ny=4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipHalfwayInactive(self):
        config = src.load_config_file(self.filepath_prefix + "config/inactive-skip-file-config.json")
        src.lexer = src.Lexer(config)
        exp_result = []
        result = src.lexer.lex("one=22\ntwo=4\n'BSLint_skip_file\ntwo=2\n")
        self.assertEqual(exp_result, result[self.WARNINGS])