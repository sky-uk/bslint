import unittest
import sys
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class TestMaxLineLength(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/StylingTestFiles/"
        else:
            cls.filepath_prefix = "../resources/StylingTestFiles/"

    def testValidLineLength(self):
        config = src.load_config_file(default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ShortLineLength.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testExceedMaxLineLength(self):
        config = src.load_config_file(user="LineLength/small-max-line-length-config.json", default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "ShortLineLength.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = [self.error.get(ErrConst.LINE_LENGTH, [11, 1])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEqualMaxLineLength(self):
        config = src.load_config_file(user="LineLength/small-max-line-length-config.json", default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "EqualMaxLineLength.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultiLineErrors(self):
        config = src.load_config_file(user="LineLength/small-max-line-length-config.json", default='test-config.json')
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "MultilineAssignment.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = [self.error.get(ErrConst.LINE_LENGTH, [11, 1]),
                      self.error.get(ErrConst.LINE_LENGTH, [11, 2])]
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)
