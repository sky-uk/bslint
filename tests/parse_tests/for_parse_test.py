import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestForParse(unittest.TestCase):

    def testForValueNoStep(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def testForIDNoStep(self):
        parser = Parser()
        result = parser.parse("for x=10 To y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.ID], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def testForFunctionCallNoStep(self):
        parser = Parser()
        result = parser.parse("for x=10 To y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def testForValueStepValue(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3 Step 2")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def testForIDStepValue(self):
        parser = Parser()
        result = parser.parse("for x=10 To y Step 2")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def testForFunctionCallStepValue(self):
        parser = Parser()
        result = parser.parse("for x=10 To y() Step 2")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def testForValueStepID(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3 Step zz")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.ID], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def testForIDStepID(self):
        parser = Parser()
        result = parser.parse("for x=10 To y Step zz")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.ID], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def testForFunctionCallStepID(self):
        parser = Parser()
        result = parser.parse("for x=10 To y() Step zz")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL, const.STEP, const.ID],
            parser.all_statements[0])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.ID], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def testForValueStepFunctionCall(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3 Step zz()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def testForIDStepFunctionCall(self):
        parser = Parser()
        result = parser.parse("for x=10 To y Step zz()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.ID, const.STEP, const.FUNCTION_CALL],
            parser.all_statements[0])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def testForFunctionCallStepFunctionCall(self):
        parser = Parser()
        result = parser.parse("for x=10 To y() Step zz()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.STEP, const.FUNCTION_CALL],
            parser.all_statements[0])
        self.assertEqual(
            [const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL, const.STEP, const.FUNCTION_CALL],
            parser.all_statements[1])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP,
             const.FUNCTION_CALL],
            parser.all_statements[2])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[3])

    def for_exception_runner(self, str_to_parse):
        parser = Parser()
        with self.assertRaises(ValueError) as ve:
            parser.parse(str_to_parse)
        self.assertEqual(ve.exception.args[0], err_const.PARSING_FAILED)

    def testInvalidForStatementAtVarAs(self):
        self.for_exception_runner("for ) To 3")

    def testInvalidForStatementAtTo(self):
        self.for_exception_runner("for x=10 To ) Step 4")

    def testInvalidForStatementAtStep(self):
        self.for_exception_runner("for x=1 To 3 Step )")

