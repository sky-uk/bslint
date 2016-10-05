import unittest
import bslint.constants as const
from bslint.lexer import Lexer as Lexer
import bslint.utilities.regex_handler as regex_handler
from bslint.utilities.token import Token as Token


class TestIdentifierRegex(unittest.TestCase):

    TYPE_GROUP = 'type'
    VALUE_GROUP = 'value'

    def testBasicIdentifier(self):
        identifier = "testId"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierWithUnderscore(self):
        identifier = "test_Id"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierStartingWithUnderscore(self):
        identifier = "_testId"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierWithNumbersNotStart(self):
        identifier = "test123ID"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testOneLetterIdentifier(self):
        identifier = "t"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierInStatementWithSpace(self):
        identifier = "_testId ="
        exp_result = [Token('_testId', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1)]
        result = Lexer(identifier).lex()
        self.assertEqual(result["Tokens"], exp_result)

    def testIdentifierInStatementDollar(self):
        identifier = "_testId$="
        exp_result = [Token('_testId', const.ID, const.ID, 1, '$'), Token('=', const.OPERATOR, const.EQUALS, 1, None)]
        result = Lexer(identifier).lex()
        self.assertEqual(result['Tokens'], exp_result)

    def testIdentifierAsUnderscore(self):
        identifier = "_"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierInStatementPercentage(self):
        identifier = "_testId%"
        exp_result = "_testId"
        exp_type = "%"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierInStatementExclamation(self):
        identifier = "_testId!"
        exp_result = "_testId"
        exp_type = "!"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)

    def testIdentifierInStatementHashtag(self):
        identifier = "_testId#"
        exp_result = "_testId"
        exp_type = "#"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)

    def testIdentifierInStatementAmpersand(self):
        identifier = "_testId&"
        exp_result = "_testId"
        exp_type = "&"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(self.VALUE_GROUP), exp_result)
        self.assertEqual(result["match"].group(self.TYPE_GROUP), exp_type)
        self.assertEqual(result["token_lexer_type"], const.ID)
        self.assertEqual(result["token_parser_type"], const.ID)
