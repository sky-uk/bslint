import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestForParse(unittest.TestCase):

    def test_for_value_no_step(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def test_for_id_no_step(self):
        parser = Parser()
        result = parser.parse("for x=10 To y")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.ID], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def test_for_function_call_no_step(self):
        parser = Parser()
        result = parser.parse("for x=10 To y()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def test_for_value_step_value(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3 Step 2")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def test_for_id_step_value(self):
        parser = Parser()
        result = parser.parse("for x=10 To y Step 2")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def test_for_function_call_step_value(self):
        parser = Parser()
        result = parser.parse("for x=10 To y() Step 2")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def test_for_value_step_id(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3 Step zz")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.ID], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def test_for_id_step_id(self):
        parser = Parser()
        result = parser.parse("for x=10 To y Step zz")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.ID], parser.all_statements[0])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[1])

    def test_for_function_call_step_id(self):
        parser = Parser()
        result = parser.parse("for x=10 To y() Step zz")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.FUNCTION_CALL, const.STEP, const.ID],
            parser.all_statements[0])
        self.assertEqual([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.ID], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def test_for_value_step_function_call(self):
        parser = Parser()
        result = parser.parse("for x=10 To 3 Step zz()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def test_for_id_step_function_call(self):
        parser = Parser()
        result = parser.parse("for x=10 To y Step zz()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.FOR, const.ID, const.EQUALS, const.VALUE, const.TO, const.ID, const.STEP, const.FUNCTION_CALL],
            parser.all_statements[0])
        self.assertEqual(
            [const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.FUNCTION_CALL], parser.all_statements[1])
        self.assertEqual([const.FOR_STATEMENT], parser.all_statements[2])

    def test_for_function_call_step_function_call(self):
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

    def test_invalid_for_statement_at_var_as(self):
        self.for_exception_runner("for ) To 3")

    def test_invalid_for_statement_at_to(self):
        self.for_exception_runner("for x=10 To ) Step 4")

    def test_invalid_for_statement_at_step(self):
        self.for_exception_runner("for x=1 To 3 Step )")

