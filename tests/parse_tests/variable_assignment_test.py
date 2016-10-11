import unittest
from bslint.parser.parser import Parser
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const

class TestVariableAssignment(unittest.TestCase):

    def variableAssignmentRunner(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.VAR_AS], parser.statement)

    def testIdentifier(self):
        self.variableAssignmentRunner("jack = 3")

    def test2VariableDeclarations(self):
        self.variableAssignmentRunner('jack = 3\n zac = "no good at table tennis"')

    def testVariableDeclarationWithReduction(self):
        self.variableAssignmentRunner('jack = 3 + 2')

    def testVariableDeclarationWithMultipleReduction(self):
        self.variableAssignmentRunner('jack = 3 + 2 - 5')

    def testVariableDeclarationWithReduction(self):
        self.variableAssignmentRunner('jack = (3 + 2)')

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
