import unittest
import bslint
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os
import bslint.commands as commands


class TestConsecutiveEmptyLines(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../resources/EmptyLinesTestFiles/")

    def testNoEmptyLines(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "NoEmptyLines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOneConsecutiveEmptyLine(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "OneConsecutiveEmptyLine.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLines(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "OnlyEmptyLines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [
            self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1, 2]),
            self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1, 3]),
            self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtEnd(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "EmptyLinesAtEnd.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,3]),
                   self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtStart(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "EmptyLinesAtStart.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,2]),
                   self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddle(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "EmptyLinesInMiddle.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testCommentNotEmptyLines(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "CommentNotEmptyLines.brs"
        file = bslint.get_string_to_parse(file_name)
        
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultipleTokensAndEmptyLines(self):
        config = bslint.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "MultipleTokensAndEmptyLines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddleCustomConfig(self):
        config = bslint.load_config_file(user="EmptyLines/double-empty-lines-config.json", default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "EmptyLinesInMiddle.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLinesCustomConfig(self):
        config = bslint.load_config_file(user="EmptyLines/double-empty-lines-config.json", default='test-config.json')
        commands.config = config
        self.lexer = bslint.Lexer()
        file_name = self.tests_filepath_prefix + "OnlyEmptyLines.brs"
        file = bslint.get_string_to_parse(file_name)
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [2, 3]),
                   self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [2, 4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)