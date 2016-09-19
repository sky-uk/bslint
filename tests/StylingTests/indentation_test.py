import unittest
import bslint
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os
import bslint.commands as commands


class TestIndentation(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/StylingTestFiles/")

    def testNoIndentation(self):
        config = bslint.load_config_file(user='Indentation/indentation-config.json', default='test-config.json')
        commands.config = config
        exp_result = None
        current_indentation_level = 0
        characters = "var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(result[0], exp_result)

    def testSingleIndentation(self):
        config = bslint.load_config_file(user='Indentation/indentation-config.json', default='test-config.json')
        commands.config = config
        exp_result = None
        current_indentation_level = 1
        characters = "    var i = 3"
        indentation_level = 0
        result = commands.check_indentation(current_indentation_level, characters, indentation_level)
        self.assertEqual(result[0], exp_result)

    def testIndentationError(self):
        config = bslint.load_config_file(user='Indentation/indentation-config.json', default='test-config.json')
        commands.config = config
        file_name = self.filepath_prefix + "BasicIndentation.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = [self.error.get(ErrConst.TAB_INDENTATION_ERROR, [4, 2])]
        self.lexer = bslint.Lexer()
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testAdvancedIndentationSuccess(self):
        config = bslint.load_config_file(user='Indentation/indentation-config.json', default='test-config.json')
        commands.config = config
        file_name = self.filepath_prefix + "AdvancedIndentation.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = []
        self.lexer = bslint.Lexer()
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testIndentWithOnlyTabsWithError(self):
        config = bslint.load_config_file(user="Indentation/tab-only-indentation.json", default='test-config.json')
        commands.config = config
        file_name = self.filepath_prefix + "IndentWithTabsOnly.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = [self.error.get(ErrConst.TAB_AND_SPACES, [10])]
        self.lexer = bslint.Lexer()
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testReallyAdvancedIndentation(self):
        config = bslint.load_config_file(user="Indentation/indentation-config.json", default='test-config.json')
        commands.config = config
        file_name = self.filepath_prefix + "SampleAdvancedIndentation.txt"
        file = bslint.get_string_to_parse(file_name)
        exp_result = []
        exp_status = "Success"
        self.lexer = bslint.Lexer()
        result = self.lexer.lex(file)
        self.assertEqual(exp_result, result[self.WARNINGS])
        self.assertEqual(exp_status, result[self.STATUS])
