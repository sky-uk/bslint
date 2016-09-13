import unittest
import src
import src.ErrorMessagesBuilder.error_message_handler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst


class TestSkipFileCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        cls.indentCheck = src.CheckIndentationCommand()

    def testSkipFileCommandSkipStart(self):
        config = src.load_config_file()
        lexer = src.Lexer(config)
        exp_result = []
        result = lexer.lex("'BSLint_skip_file \nxgygu= 22\ny=4\n sdfsf=2 \n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipHalfWay(self):
        config = src.load_config_file()
        lexer = src.Lexer(config)
        exp_result = []
        result = lexer.lex("one = 22\ntwo = 4\n'BSLint_skip_file \n sdfsf=2 \n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipStartInactive(self):
        config = src.load_config_file(user="BSLintCommands/inactive-skip-file-config.json")
        lexer = src.Lexer(config)
        exp_result = [self.error.get(ErrConst.TYPO_IN_CODE, [2])]
        result = lexer.lex("'BSLint_skip_file \nxgygu = 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipHalfwayInactive(self):
        config = src.load_config_file(user="BSLintCommands/inactive-skip-file-config.json")
        lexer = src.Lexer(config)
        exp_result = []
        result = lexer.lex("one = 22\ntwo = 4\n'BSLint_skip_file\ntwo = 2\n")
        self.assertEqual(exp_result, result[self.WARNINGS])
