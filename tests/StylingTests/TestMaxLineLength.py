import unittest
import sys
import src


class TestMaxLineLength(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        if sys.argv[0].endswith('nosetests'):
            cls.filepath_prefix = "./resources/"
        else:
            cls.filepath_prefix = "../resources/"

    def testValidLineLength(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "BasicStringAssignment.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = []
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testExceedMaxLineLength(self):
        config = src.load_config_file(self.filepath_prefix + "config/small-max-line-length-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "BasicStringAssignment.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = ['Line length exceeds max line length [11]. Line number: 1']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testEqualMaxLineLength(self):
        config = src.load_config_file(self.filepath_prefix + "config/small-max-line-length-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "brightscript.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = ['Warning. You have spelling mistakes in your code. line number: 1']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)

    def testMultiLineErrors(self):
        config = src.load_config_file(self.filepath_prefix + "config/small-max-line-length-config.json")
        self.lexer = src.Lexer(config)
        file_name = self.filepath_prefix + "MultilineAssignment.txt"
        file = src.main(file_name)
        self.assertNotEqual(file, "")
        exp_result = ['Line length exceeds max line length [11]. Line number: 1',
                      'Line length exceeds max line length [11]. Line number: 2']
        result = self.lexer.lex(file)
        self.assertEqual(result[self.WARNINGS], exp_result)
        self.assertEqual(result[self.STATUS], self.SUCCESS)
