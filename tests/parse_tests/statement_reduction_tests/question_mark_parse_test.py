import unittest
import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestQuestionMarkParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_question_mark_value(self):
        self.common.match_statement("print 4", const.PRINT_STATEMENT)

    def test_question_mark_id(self):
        self.common.match_statement("? x", const.PRINT_STATEMENT)

    def test_question_mark_var_as(self):
        self.common.match_statement("? x = 3", const.PRINT_STATEMENT)

    def test_question_mark_function_call(self):
        self.common.match_statement("? x()", const.PRINT_STATEMENT)

    def test_question_mark_idoperator_value(self):
        self.common.match_statement("? x^5", const.PRINT_STATEMENT)

    def test_question_mark_value_comma_value(self):
        self.common.match_statement("? 3,4", const.PRINT_STATEMENT)

    def test_question_mark_value_comma_id(self):
        self.common.match_statement("? 3,d", const.PRINT_STATEMENT)

    def test_question_mark_value_comma_function_call(self):
        self.common.match_statement("? 3,x()", const.PRINT_STATEMENT)

    def test_question_mark_value_comma_variable_assignment(self):
        self.common.match_statement("? 3,x=4", const.PRINT_STATEMENT)

    def test_question_mark_value_comma_argument(self):
        self.common.match_statement("? 3,3,4", const.PRINT_STATEMENT)

    def test_question_mark_variable_assignment_comma_function_call(self):
        self.common.match_statement("? Y=4,x()", const.PRINT_STATEMENT)

    def test_question_mark_variable_assignment_comma_variable_assignment(self):
        self.common.match_statement("? Y=4,x=4", const.PRINT_STATEMENT)

    def test_question_mark_variable_assignment_comma_argument(self):
        self.common.match_statement("? x=1,4,4", const.PRINT_STATEMENT)

    def test_question_mark_value_semi_colon_value(self):
        self.common.match_statement("? 3;4", const.PRINT_STATEMENT)

    def test_question_mark_value_semi_colon_id(self):
        self.common.match_statement("? 3;d", const.PRINT_STATEMENT)

    def test_question_mark_value_semi_colon_function_call(self):
        self.common.match_statement("? 3;x()", const.PRINT_STATEMENT)

    def test_question_mark_value_semi_colon_variable_assignment(self):
        self.common.match_statement("? 3;x=4", const.PRINT_STATEMENT)

    def test_question_mark_value_semi_colon_argument(self):
        self.common.match_statement("? 4;4,4", const.PRINT_STATEMENT)

    def test_question_mark_idsemi_colon_value(self):
        self.common.match_statement("? X;4", const.PRINT_STATEMENT)

    def test_question_mark_idsemi_colon_id(self):
        self.common.match_statement("? X;d", const.PRINT_STATEMENT)

    def test_question_mark_idsemi_colon_function_call(self):
        self.common.match_statement("? Y;x()", const.PRINT_STATEMENT)

    def test_question_mark_idsemi_colon_variable_assignment(self):
        self.common.match_statement("? Y;x=4", const.PRINT_STATEMENT)

    def test_question_mark_idsemi_colon_argument(self):
        self.common.match_statement("? x;4;4", const.PRINT_STATEMENT)

    def test_question_mark_variable_assignment_semi_colon_variable_assignment(self):
        self.common.match_statement("? Y=4;x=4", const.PRINT_STATEMENT)

    def test_question_mark_variable_assignment_semi_colon_argument(self):
        self.common.match_statement("? x=1;4;4", const.PRINT_STATEMENT)

    def test_invalid_while_parenthesis(self):
        self.common.exception_runner("? )")

    def test_invalid_while_for(self):
        self.common.exception_runner("? (for)")

    def test_invalid_while_end_while(self):
        self.common.exception_runner("? endwhile")
