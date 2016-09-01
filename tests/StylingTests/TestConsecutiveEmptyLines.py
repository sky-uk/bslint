import unittest
import sys
import src


class TestConsecutiveEmptyLines(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
            cls.tests_filepath_prefix = "./resources/EmptyLinesTestFiles/"
        else:
            cls.filepath_prefix = "../resources/"
            cls.tests_filepath_prefix = "../resources/EmptyLinesTestFiles/"


    def testNoEmptyLines(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "NoEmptyLines.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOneConsecutiveEmptyLine(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "OneConsecutiveEmptyLine.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLines(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "OnlyEmptyLines.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ["WARNING: Cannot have more than 1 consecutive empty lines. Line number: 2",
                   "WARNING: Cannot have more than 1 consecutive empty lines. Line number: 3"]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtEnd(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesAtEnd.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ["WARNING: Cannot have more than 1 consecutive empty lines. Line number: 3"]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesAtStart(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesAtStart.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ["WARNING: Cannot have more than 1 consecutive empty lines. Line number: 2",
                   "WARNING: Cannot have more than 1 consecutive empty lines. Line number: 3"]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddle(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesInMiddle.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ["WARNING: Cannot have more than 1 consecutive empty lines. Line number: 4"]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testCommentNotEmptyLines(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "CommentNotEmptyLines.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ['WARNING: Comments must be TODOs and must follow convention. Line number: 2']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultipleTokensAndEmptyLines(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "MultipleTokensAndEmptyLines.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ["WARNING: Cannot have more than 1 consecutive empty lines. Line number: 3"]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEmptyLinesInMiddleCustomConfig(self):
        config = src.load_config_file(self.filepath_prefix + "config/consecutive-empty-lines-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "EmptyLinesInMiddle.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testOnlyEmptyLinesCustomConfig(self):
        config = src.load_config_file(self.filepath_prefix + "config/consecutive-empty-lines-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.tests_filepath_prefix + "OnlyEmptyLines.brs"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_res = ["WARNING: Cannot have more than 2 consecutive empty lines. Line number: 3"]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_res)
        self.assertEqual(result[self.STATUS], self.SUCCESS)