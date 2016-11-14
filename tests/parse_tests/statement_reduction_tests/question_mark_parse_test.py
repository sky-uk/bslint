import unittest
import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestQuestionMarkParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_question_mark_value(self):
        self.common.match_statement(const.PRINT_STMT, "print 4")

    def test_question_mark_id(self):
        self.common.match_statement(const.PRINT_STMT, "? x")

    def test_question_mark_var_as(self):
        self.common.match_statement(const.PRINT_STMT, "? x = 3")

    def test_question_mark_function_call(self):
        self.common.match_statement(const.PRINT_STMT, "? x()")

    def test_question_mark_idoperator_value(self):
        self.common.match_statement(const.PRINT_STMT, "? x^5")

    def test_question_mark_value_comma_value(self):
        self.common.match_statement(const.PRINT_STMT, "? 3,4")

    def test_question_mark_value_comma_id(self):
        self.common.match_statement(const.PRINT_STMT, "? 3,d")

    def test_question_mark_value_comma_function_call(self):
        self.common.match_statement(const.PRINT_STMT, "? 3,x()")

    def test_question_mark_value_comma_variable_assignment(self):
        self.common.match_statement(const.PRINT_STMT, "? 3,x=4")

    def test_question_mark_value_comma_argument(self):
        self.common.match_statement(const.PRINT_STMT, "? 3,3,4")

    def test_question_mark_variable_assignment_comma_function_call(self):
        self.common.match_statement(const.PRINT_STMT, "? Y=4,x()")

    def test_question_mark_variable_assignment_comma_variable_assignment(self):
        self.common.match_statement(const.PRINT_STMT, "? Y=4,x=4")

    def test_question_mark_variable_assignment_comma_argument(self):
        self.common.match_statement(const.PRINT_STMT, "? x=1,4,4")

    def test_question_mark_value_semi_colon_value(self):
        self.common.match_statement(const.PRINT_STMT, "? 3;4")

    def test_question_mark_value_semi_colon_id(self):
        self.common.match_statement(const.PRINT_STMT, "? 3;d")

    def test_question_mark_value_semi_colon_function_call(self):
        self.common.match_statement(const.PRINT_STMT, "? 3;x()")

    def test_question_mark_value_semi_colon_variable_assignment(self):
        self.common.match_statement(const.PRINT_STMT, "? 3;x=4")

    def test_question_mark_value_semi_colon_argument(self):
        self.common.match_statement(const.PRINT_STMT, "? 4;4,4")

    def test_question_mark_idsemi_colon_value(self):
        self.common.match_statement(const.PRINT_STMT, "? X;4")

    def test_question_mark_idsemi_colon_id(self):
        self.common.match_statement(const.PRINT_STMT, "? X;d")

    def test_question_mark_idsemi_colon_function_call(self):
        self.common.match_statement(const.PRINT_STMT, "? Y;x()")

    def test_question_mark_idsemi_colon_variable_assignment(self):
        self.common.match_statement(const.PRINT_STMT, "? Y;x=4")

    def test_question_mark_idsemi_colon_argument(self):
        self.common.match_statement(const.PRINT_STMT, "? x;4;4")

    def test_question_mark_variable_assignment_semi_colon_variable_assignment(self):
        self.common.match_statement(const.PRINT_STMT, "? Y=4;x=4")

    def test_question_mark_variable_assignment_semi_colon_argument(self):
        self.common.match_statement(const.PRINT_STMT, "? x=1;4;4")

    def test_invalid_while_parenthesis(self):
        self.common.status_error("? )")

    def test_invalid_while_for(self):
        self.common.status_error("? (for)")

    def test_invalid_while_end_while(self):
        self.common.status_error("? endwhile")
