import unittest
import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestQuestionMarkParse(unittest.TestCase):
    def testQuestionMarkValue(self):
        parser = Parser()
        result = parser.parse("? 4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[0])

    def testQuestionMarkID(self):
        parser = Parser()
        result = parser.parse("? x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[0])

    def testQuestionMarkVarAs(self):
        parser = Parser()
        result = parser.parse("? x = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkFunctionCall(self):
        parser = Parser()
        result = parser.parse("? x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkIDOperatorValue(self):
        parser = Parser()
        result = parser.parse("? x^5")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkValueCommaValue(self):
        parser = Parser()
        result = parser.parse("? 3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkValueCommaID(self):
        parser = Parser()
        result = parser.parse("? 3,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkValueCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("? 3,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkValueCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? 3,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkValueCommaArgument(self):
        parser = Parser()
        result = parser.parse("? 3,3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkIDCommaValue(self):
        parser = Parser()
        result = parser.parse("? X,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkIDCommaID(self):
        parser = Parser()
        result = parser.parse("? X,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkIDCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("? Y,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkIDCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? Y,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkIDCommaArgument(self):
        parser = Parser()
        result = parser.parse("? x,3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkFunctionCallCommaValue(self):
        parser = Parser()
        result = parser.parse("? X(),4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkFunctionCallCommaID(self):
        parser = Parser()
        result = parser.parse("? X(),d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.ID], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkFunctionCallCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("? Y(),x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA,
                          const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL],
                         parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testQuestionMarkFunctionCallCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? Y(),x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA, const.VAR_AS],
            parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.VAR_AS], parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testQuestionMarkFunctionCallCommaArgument(self):
        parser = Parser()
        result = parser.parse("? x(),3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA,
                          const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testQuestionMarkVariableAssignmentCommaValue(self):
        parser = Parser()
        result = parser.parse("? X=3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkVariableAssignmentCommaID(self):
        parser = Parser()
        result = parser.parse("? X=4,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkVariableAssignmentCommaFunctionCall(self):
        parser = Parser()
        result = parser.parse("? Y=4,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkVariableAssignmentCommaVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? Y=4,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VAR_AS],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkVariableAssignmentCommaArgument(self):
        parser = Parser()
        result = parser.parse("? x=1,4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkValueSemiColonValue(self):
        parser = Parser()
        result = parser.parse("? 3;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkValueSemiColonID(self):
        parser = Parser()
        result = parser.parse("? 3;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkValueSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("? 3;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkValueSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? 3;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkValueSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("? 4;4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkIDSemiColonValue(self):
        parser = Parser()
        result = parser.parse("? X;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkIDSemiColonID(self):
        parser = Parser()
        result = parser.parse("? X;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkIDSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("? Y;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkIDSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? Y;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkIDSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("? x;4;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkFunctionCallSemiColonValue(self):
        parser = Parser()
        result = parser.parse("? X();4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkFunctionCallSemiColonID(self):
        parser = Parser()
        result = parser.parse("? X();d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.ID],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkFunctionCallSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("? Y();x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.SEMI_COLON,
             const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testQuestionMarkFunctionCallSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? Y();x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.SEMI_COLON,
             const.VAR_AS], parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS], parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testQuestionMarkFunctionCallSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("? x();4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.SEMI_COLON,
             const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT],
            parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def testQuestionMarkVariableAssignmentSemiColonValue(self):
        parser = Parser()
        result = parser.parse("? X=3;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkVariableAssignmentSemiColonID(self):
        parser = Parser()
        result = parser.parse("? X=4;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def testQuestionMarkVariableAssignmentSemiColonFunctionCall(self):
        parser = Parser()
        result = parser.parse("? Y=4;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
            parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkVariableAssignmentSemiColonVariableAssignment(self):
        parser = Parser()
        result = parser.parse("? Y=4;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VAR_AS],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def testQuestionMarkVariableAssignmentSemiColonArgument(self):
        parser = Parser()
        result = parser.parse("? x=1;4;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
            parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def question_mark_exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def testInvalidWhileParenthesis(self):
        self.question_mark_exception_runner("? )")

    def testInvalidWhileFor(self):
        self.question_mark_exception_runner("? (for)")

    def testInvalidWhileEndWhile(self):
        self.question_mark_exception_runner("? endwhile")
