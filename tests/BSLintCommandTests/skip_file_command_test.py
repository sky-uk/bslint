import unittest
import bslint
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import bslint.commands as commands


class TestSkipFileCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()

    def testSkipFileCommandSkipStart(self):
        lexer = bslint.Lexer()
        exp_result = []
        result = lexer.lex("'BSLint_skip_file \nxgygu= 22\ny=4\n sdfsf=2 \n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipHalfWay(self):
        lexer = bslint.Lexer()
        exp_result = []
        result = lexer.lex("one = 22\ntwo = 4\n'BSLint_skip_file \n sdfsf=2 \n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipStartInactive(self):
        config = bslint.load_config_file(user="BSLintCommands/inactive-skip-file-config.json")
        commands.config = config
        lexer = bslint.Lexer()
        exp_result = [self.error.get(ErrConst.TYPO_IN_CODE, [2])]
        result = lexer.lex("'BSLint_skip_file \nxgygu = 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipFileCommandSkipHalfwayInactive(self):
        lexer = bslint.Lexer()
        exp_result = []
        result = lexer.lex("one = 22\ntwo = 4\n'BSLint_skip_file\ntwo = 2\n")
        self.assertEqual(exp_result, result[self.WARNINGS])
