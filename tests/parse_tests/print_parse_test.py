import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestPrintParse(unittest.TestCase):
    def testPrintValue(self):
        parser = Parser()
        result = parser.parse("print 4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[0])

    def testPrintID(self):
        parser = Parser()
        result = parser.parse("print x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[0])

    def testPrintVarAs(self):
        parser = Parser()
        result = parser.parse("print x = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintFunctionCall(self):
        parser = Parser()
        result = parser.parse("print x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintIDOperatorValue(self):
        parser = Parser()
        result = parser.parse("print x^5")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintValueCommaValue(self):
        parser = Parser()
        result = parser.parse("print 3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintValueCommaID(self):
        parser = Parser()
        result = parser.parse("print 3,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintValueCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("print 3,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintValueCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print 3,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintValueCommaArgument(self):
        parser = Parser()
        result = parser.parse("print 3,3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintIDCommaValue(self):
        parser = Parser()
        result = parser.parse("print X,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintIDCommaID(self):
        parser = Parser()
        result = parser.parse("print X,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintIDCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("print Y,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintIDCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print Y,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintIDCommaArgument(self):
        parser = Parser()
        result = parser.parse("print x,3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintFunctionCallCommaValue(self):
        parser = Parser()
        result = parser.parse("print X(),4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintFunctionCallCommaID(self):
        parser = Parser()
        result = parser.parse("print X(),d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.ID], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintFunctionCallCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("print Y(),x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA,
                          const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL],
                         parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testPrintFunctionCallCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print Y(),x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA, const.VAR_AS],
            parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.VAR_AS], parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testPrintFunctionCallCommaArgument(self):
        parser = Parser()
        result = parser.parse("print x(),3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA,
                          const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testPrintVariableAssignmentCommaValue(self):
        parser = Parser()
        result = parser.parse("print X=3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintVariableAssignmentCommaID(self):
        parser = Parser()
        result = parser.parse("print X=4,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintVariableAssignmentCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("print Y=4,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintVariableAssignmentCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print Y=4,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VAR_AS],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintVariableAssignmentCommaArgument(self):
        parser = Parser()
        result = parser.parse("print x=1,4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintValueSemiColonValue(self):
        parser = Parser()
        result = parser.parse("print 3;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintValueSemiColonID(self):
        parser = Parser()
        result = parser.parse("print 3;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintValueSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("print 3;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintValueSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print 3;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintValueSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("print 4;4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintIDSemiColonValue(self):
        parser = Parser()
        result = parser.parse("print X;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintIDSemiColonID(self):
        parser = Parser()
        result = parser.parse("print X;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintIDSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("print Y;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintIDSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print Y;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintIDSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("print x;4;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintFunctionCallSemiColonValue(self):
        parser = Parser()
        result = parser.parse("print X();4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintFunctionCallSemiColonID(self):
        parser = Parser()
        result = parser.parse("print X();d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.ID],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintFunctionCallSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("print Y();x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.SEMI_COLON,
             const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testPrintFunctionCallSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print Y();x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.SEMI_COLON,
             const.VAR_AS], parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS], parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testPrintFunctionCallSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("print x();4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.SEMI_COLON,
             const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT],
            parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testPrintVariableAssignmentSemiColonValue(self):
        parser = Parser()
        result = parser.parse("print X=3;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintVariableAssignmentSemiColonID(self):
        parser = Parser()
        result = parser.parse("print X=4;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testPrintVariableAssignmentSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("print Y=4;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
            parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintVariableAssignmentSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("print Y=4;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VAR_AS],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testPrintVariableAssignmentSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("print x=1;4;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
            parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def print_exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def testInvalidWhileParenthesis(self):
        self.print_exception_runner("print )")

    def testInvalidWhileFor(self):
        self.print_exception_runner("print (for)")

    def testInvalidWhileEndWhile(self):
        self.print_exception_runner("print endwhile")
