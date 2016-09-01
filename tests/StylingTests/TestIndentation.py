import unittest
import sys
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestIndentation(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        cls.indentCheck = src.CheckIndentationCommand()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def testNoIndentation(self):
        config = src.load_config_file()
        exp_result = None
        result = self.indentCheck.execute({"current_indentation_level": 0,
                                           "line_number": 1,
                                           "indentation": config["check_indentation"],
                                           "characters": "var i = 3",
                                           "indentation_level": 0})
        self.assertEqual(result[0], exp_result)

    def testSingleIndentation(self):
        config = src.load_config_file()
        exp_result = None
        result = self.indentCheck.execute({"current_indentation_level": 1,
                                           "line_number": 1,
                                           "indentation": config["check_indentation"],
                                           "characters": "    var i = 3",
                                           "indentation_level": 0})
        self.assertEqual(result[0], exp_result)

    def testIndentationError(self):
        config = src.load_config_file()
        file_name = self.filepath_prefix + "BasicIndentation.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = [self.error.get(ErrConst.TAB_INDENTATION_ERROR, [4, 2])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testAdvancedIndentationSuccess(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-spell-check-config.json")
        file_name = self.filepath_prefix + "AdvancedIndentation.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = []
        self.lexer = src.Lexer(config)
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testIndentWithOnlyTabsWithError(self):
        config = src.load_config_file(self.filepath_prefix + "config/no-spell-check-only-tab-indent-config.json")
        file_name = self.filepath_prefix + "IndentWithTabsOnly.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = [self.error.get(ErrConst.TAB_AND_SPACES, [11])]
        self.lexer = src.Lexer(config)
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])
