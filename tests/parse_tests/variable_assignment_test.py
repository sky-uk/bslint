import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const


class TestVariableAssignment(unittest.TestCase):

    def testIdentifier(self):
        parser = Parser()
        result = parser.parse("jack = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.all_statements[0])

    def test2VariableDeclarations(self):
        parser = Parser()
        result = parser.parse('jack = 3\n zac = "no good at table tennis"')
        self.assertEqual("Success", result["Status"])
        print(parser.all_statements)
        self.assertEqual([const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def testVariableDeclarationWithReduction(self):
        parser = Parser()
        result = parser.parse('jack = 3 + 2')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.VAR_AS], parser.all_statements[1])

    def testVariableDeclarationWithMultipleReduction(self):
        parser = Parser()
        result = parser.parse('jack = 3 + 2 - 5')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE, const.OPERATOR, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE], parser.all_statements[1])
        self.assertEqual([const.VAR_AS], parser.all_statements[2])

    def testVariableDeclarationWithReductionAndParenthesis(self):
        parser = Parser()
        result = parser.parse('jack = (3 + 2)')
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.ID, const.EQUALS, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS],
                         parser.all_statements[0])
        self.assertEqual([const.ID, const.EQUALS, const.VALUE], parser.all_statements[1])
        self.assertEqual([const.VAR_AS], parser.all_statements[2])

    def variable_assignment_exception_runner(self, str_to_parse):
        parser = Parser()
        exp_exception_msg = err_const.PARSING_FAILED
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
            self.assertEqual(ve.exception.args[0], exp_exception_msg)

    def testInvalidVariableAssignmentWhile(self):
        self.variable_assignment_exception_runner("jack = while")

    def testInvalidVariableAssignmentExtraEquals(self):
        self.variable_assignment_exception_runner("jack == 3")

    def testInvalidVariableAssignmentIncorrectOrder(self):
        self.variable_assignment_exception_runner("3 = jack")
