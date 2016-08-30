import unittest

import Constants as const
import src


class TestIdentifierRegex(unittest.TestCase):

    TYPE_GROUP = 'type'
    VALUE_GROUP = 'value'

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        
    def testBasicIdentifier(self):
        identifier = "testId"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.ID)

    def testIdentifierWithUnderscore(self):
        identifier = "test_Id"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.ID)

    def testIdentifierStartingWithUnderscore(self):
        identifier = "_testId"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.ID)

    def testIdentifierWithNumbersNotStart(self):
        identifier = "test123ID"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.ID)

    def testOneLetterIdentifier(self):
        identifier = "t"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.ID)

    def testIdentifierInStatementWithSpace(self):
        identifier = "_testId ="
        exp_result = [('_testId', const.ID, 1), ('=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementDollar(self):
        identifier = "_testId$="
        exp_result = [('_testId', const.ID, '$', 1), ('=', const.OPERATOR, 1)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierAsUnderscore(self):
        identifier = "_"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.ID)

    def testIdentifierInStatementPercentage(self):
        identifier = "_testId%"
        exp_result = "_testId"
        exp_type = "%"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(exp_result, result.group(self.VALUE_GROUP))
        self.assertEqual(exp_type, result.group(self.TYPE_GROUP))
        self.assertEqual(regex_type, const.ID)

    def testIdentifierInStatementExclamation(self):
        identifier = "_testId!"
        exp_result = "_testId"
        exp_type = "!"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(exp_result, result.group(self.VALUE_GROUP))
        self.assertEqual(exp_type, result.group(self.TYPE_GROUP))
        self.assertEqual(regex_type, const.ID)

    def testIdentifierInStatementHashtag(self):
        identifier = "_testId#"
        exp_result = "_testId"
        exp_type = "#"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(exp_result, result.group(self.VALUE_GROUP))
        self.assertEqual(exp_type, result.group(self.TYPE_GROUP))
        self.assertEqual(regex_type, const.ID)

    def testIdentifierInStatementAmpersand(self):
        identifier = "_testId&"
        exp_result = "_testId"
        exp_type = "&"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(exp_result, result.group(self.VALUE_GROUP))
        self.assertEqual(exp_type, result.group(self.TYPE_GROUP))
        self.assertEqual(regex_type, const.ID)
