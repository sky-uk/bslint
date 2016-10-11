import unittest

import bslint.constants as const
import bslint.error_messages_builder.error_messages_constants as err_const
from bslint.parser.parser import Parser


class TestForParse(unittest.TestCase):

    def for_runner(self, str_to_parse):
        parser = Parser()
        result = parser.parse(str_to_parse)
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR_STATEMENT], parser.statement)

    def testForValueNoStep(self):
        self.for_runner("for x=10 To 3")

    def testForIDNoStep(self):
        self.for_runner("for x=10 To y")

    def testForFunctionCallNoStep(self):
        self.for_runner("for x=10 To y()")

    def testForValueStepValue(self):
        self.for_runner("for x=10 To 3 Step 2")

    def testForIDStepValue(self):
        self.for_runner("for x=10 To y Step 2")

    def testForFunctionCallStepValue(self):
        self.for_runner("for x=10 To y Step 2")

    def testForValueStepID(self):
        self.for_runner("for x=10 To 3 Step zz")

    def testForIDStepID(self):
        self.for_runner("for x=10 To y Step zz")

    def testForFunctionCallStepID(self):
        self.for_runner("for x=10 To y Step zz")

    def testForValueStepFunctionCall(self):
        self.for_runner("for x=10 To 3 Step zz()")

    def testForIDStepFunctionCall(self):
        self.for_runner("for x=10 To y Step zz()")

    def testForFunctionCallStepFunctionCall(self):
        self.for_runner("for x=10 To y Step zz()")

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

