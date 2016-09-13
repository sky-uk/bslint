import unittest
import src
import os
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestConsecutiveEmptyLines(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        this_dir, this_filename = os.path.split(__file__)
        cls.tests_filepath_prefix = os.path.join(this_dir, "../EmptyLinesTestFiles/")


    def testNoEmptyLines(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "NoEmptyLines.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOneConsecutiveEmptyLine(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "OneConsecutiveEmptyLine.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLines(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "OnlyEmptyLines.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [
            self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1, 2]),
            self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1, 3]),
            self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1, 4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtEnd(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesAtEnd.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,3]),
                   self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtStart(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesAtStart.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,2]),
                   self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddle(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesInMiddle.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testCommentNotEmptyLines(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "CommentNotEmptyLines.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultipleTokensAndEmptyLines(self):
        config = src.load_config_file(user='EmptyLines/single-empty-lines-config.json', default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "MultipleTokensAndEmptyLines.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [1,3])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddleCustomConfig(self):
        config = src.load_config_file(user="EmptyLines/double-empty-lines-config.json", default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesInMiddle.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLinesCustomConfig(self):
        config = src.load_config_file(user="EmptyLines/double-empty-lines-config.json", default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "OnlyEmptyLines.brs"
        file = src.get_string_to_parse(file_name)
        self.assertNotEqual(file, "")
        exp_res = [self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [2, 3]),
                   self.error.get(ErrConst.CONSECUTIVE_EMPTY_LINES, [2, 4])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)