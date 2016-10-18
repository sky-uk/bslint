import unittest

import bslint.constants as const
import bslint.error_messages.constants as err_const
from bslint.parser.parser import Parser


class TestQuestionMarkParse(unittest.TestCase):
    def test_question_mark_value(self):
        parser = Parser()
        result = parser.parse("? 4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[0])

    def test_question_mark_id(self):
        parser = Parser()
        result = parser.parse("? x")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[0])

    def test_question_mark_var_as(self):
        parser = Parser()
        result = parser.parse("? x = 3")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_function_call(self):
        parser = Parser()
        result = parser.parse("? x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_idoperator_value(self):
        parser = Parser()
        result = parser.parse("? x^5")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_value_comma_value(self):
        parser = Parser()
        result = parser.parse("? 3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_value_comma_id(self):
        parser = Parser()
        result = parser.parse("? 3,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_value_comma_function_call(self):
        parser = Parser()
        result = parser.parse("? 3,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_value_comma_variable_assignment(self):
        parser = Parser()
        result = parser.parse("? 3,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_value_comma_argument(self):
        parser = Parser()
        result = parser.parse("? 3,3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_idcomma_value(self):
        parser = Parser()
        result = parser.parse("? X,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_idcomma_id(self):
        parser = Parser()
        result = parser.parse("? X,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_idcomma_function_call(self):
        parser = Parser()
        result = parser.parse("? Y,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_idcomma_variable_assignment(self):
        parser = Parser()
        result = parser.parse("? Y,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_idcomma_argument(self):
        parser = Parser()
        result = parser.parse("? x,3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.COMMA, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_function_call_comma_value(self):
        parser = Parser()
        result = parser.parse("? X(),4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.VALUE], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_function_call_comma_id(self):
        parser = Parser()
        result = parser.parse("? X(),d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.ID], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_function_call_comma_function_call(self):
        parser = Parser()
        result = parser.parse("? Y(),x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA,
                          const.FUNCTION_CALL], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL],
                         parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def test_question_mark_function_call_comma_variable_assignment(self):
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

    def test_question_mark_function_call_comma_argument(self):
        parser = Parser()
        result = parser.parse("? x(),3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS, const.COMMA,
                          const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[1])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[2])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[3])

    def test_question_mark_variable_assignment_comma_value(self):
        parser = Parser()
        result = parser.parse("? X=3,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_variable_assignment_comma_id(self):
        parser = Parser()
        result = parser.parse("? X=4,d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_variable_assignment_comma_function_call(self):
        parser = Parser()
        result = parser.parse("? Y=4,x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_variable_assignment_comma_variable_assignment(self):
        parser = Parser()
        result = parser.parse("? Y=4,x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VAR_AS],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_variable_assignment_comma_argument(self):
        parser = Parser()
        result = parser.parse("? x=1,4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_value_semi_colon_value(self):
        parser = Parser()
        result = parser.parse("? 3;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_value_semi_colon_id(self):
        parser = Parser()
        result = parser.parse("? 3;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_value_semi_colon_function_call(self):
        parser = Parser()
        result = parser.parse("? 3;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_value_semi_colon_variable_assignment(self):
        parser = Parser()
        result = parser.parse("? 3;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_value_semi_colon_argument(self):
        parser = Parser()
        result = parser.parse("? 4;4,4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_idsemi_colon_value(self):
        parser = Parser()
        result = parser.parse("? X;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_idsemi_colon_id(self):
        parser = Parser()
        result = parser.parse("? X;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_idsemi_colon_function_call(self):
        parser = Parser()
        result = parser.parse("? Y;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.FUNCTION_CALL],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_idsemi_colon_variable_assignment(self):
        parser = Parser()
        result = parser.parse("? Y;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.VAR_AS], parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_idsemi_colon_argument(self):
        parser = Parser()
        result = parser.parse("? x;4;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_function_call_semi_colon_value(self):
        parser = Parser()
        result = parser.parse("? X();4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_function_call_semi_colon_id(self):
        parser = Parser()
        result = parser.parse("? X();d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.FUNCTION_CALL, const.SEMI_COLON, const.ID],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_function_call_semi_colon_function_call(self):
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

    def test_question_mark_function_call_semi_colon_variable_assignment(self):
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

    def test_question_mark_function_call_semi_colon_argument(self):
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

    def test_question_mark_variable_assignment_semi_colon_value(self):
        parser = Parser()
        result = parser.parse("? X=3;4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_variable_assignment_semi_colon_id(self):
        parser = Parser()
        result = parser.parse("? X=4;d")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[0])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[1])

    def test_question_mark_variable_assignment_semi_colon_function_call(self):
        parser = Parser()
        result = parser.parse("? Y=4;x()")
        self.assertEqual("Success", result["Status"])
        self.assertEqual(
            [const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
            parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_variable_assignment_semi_colon_variable_assignment(self):
        parser = Parser()
        result = parser.parse("? Y=4;x=4")
        self.assertEqual("Success", result["Status"])
        self.assertEqual([const.PRINT_KEYWORD, const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VAR_AS],
                         parser.all_statements[0])
        self.assertEqual([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], parser.all_statements[1])
        self.assertEqual([const.PRINT_STATEMENT], parser.all_statements[2])

    def test_question_mark_variable_assignment_semi_colon_argument(self):
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

    def test_invalid_while_parenthesis(self):
        self.question_mark_exception_runner("? )")

    def test_invalid_while_for(self):
        self.question_mark_exception_runner("? (for)")

    def test_invalid_while_end_while(self):
        self.question_mark_exception_runner("? endwhile")
