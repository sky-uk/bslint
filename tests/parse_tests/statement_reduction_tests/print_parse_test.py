import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestPrintParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def testPrintValue(self):
        self.common.match_statement(const.PRINT_STMT, "print 4")

    def testPrintID(self):
        self.common.match_statement(const.PRINT_STMT, "print x")

    def testPrintVarAs(self):
        self.common.match_statement(const.PRINT_STMT, "print x = 3")

    def testPrintFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print x()")

    def testPrintEmptyAssociativeArray(self):
        self.common.match_statement(const.PRINT_STMT, "print {}")

    def testPrintAssociativeArray(self):
        self.common.match_statement(const.PRINT_STMT, "print {a:1}")

    def testPrintEmptyArray(self):
        self.common.match_statement(const.PRINT_STMT, "print []")

    def testPrintArray(self):
        self.common.match_statement(const.PRINT_STMT, "print [5]")

    def testPrintIDOperatorValue(self):
        self.common.match_statement(const.PRINT_STMT, "print x^5")

    def testPrintValueCommaValue(self):
        self.common.match_statement(const.PRINT_STMT, "print 3,4")

    def testPrintValueCommaID(self):
        self.common.match_statement(const.PRINT_STMT, "print 3,d")

    def testPrintValueCommaFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print 3,x()")

    def testPrintValueCommaVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print 3,x=4")

    def testPrintValueCommaArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print 3,3,4")

    def testPrintValueCommaEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print 3, {}")

    def testPrintIDCommaValue(self):
        self.common.match_statement(const.PRINT_STMT, "print X,4")

    def testPrintIDCommaID(self):
        self.common.match_statement(const.PRINT_STMT, "print X,d")

    def testPrintIDCommaFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print Y,x()")

    def testPrintIDCommaVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print Y,x=4")

    def testPrintIDCommaArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print x,3,4")

    def testPrintIDCommaEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print a, []")

    def testPrintFunctionCallCommaValue(self):
        self.common.match_statement(const.PRINT_STMT, "print X(),4")

    def testPrintFunctionCallCommaID(self):
        self.common.match_statement(const.PRINT_STMT, "print X(),d")

    def testPrintFunctionCallCommaFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print Y(),x()")

    def testPrintFunctionCallCommaVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print Y(a, b),x=4")

    def testPrintFunctionCallCommaArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print x(),3,4")

    def testPrintFunctionCallCommaEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print y(), {a:2}")

    def testPrintVariableAssignmentCommaValue(self):
        self.common.match_statement(const.PRINT_STMT, "print X=3,4")

    def testPrintVariableAssignmentCommaID(self):
        self.common.match_statement(const.PRINT_STMT, "print X=4,d")

    def testPrintVariableAssignmentCommaFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print Y=4,x()")

    def testPrintVariableAssignmentCommaVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print Y=4,x=4")

    def testPrintVariableAssignmentCommaArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print x=1,4,4")

    def testPrintVariableAssignmentCommaEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print a = 3, {d:6}")

    def testPrintValueSemiColonValue(self):
        self.common.match_statement(const.PRINT_STMT, "print 3;4")

    def testPrintValueSemiColonID(self):
        self.common.match_statement(const.PRINT_STMT, "print d.c();x")

    def testPrintValueSemiColonFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print 3;x()")

    def testPrintValueSemiColonVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print 3;x=4")

    def testPrintValueSemiColonArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print 4;4,4")

    def testPrintValueSemiColonEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print 3; [a]")

    def testPrintIDSemiColonValue(self):
        self.common.match_statement(const.PRINT_STMT, "print X;4")

    def testPrintIDSemiColonID(self):
        self.common.match_statement(const.PRINT_STMT, "print X;d")

    def testPrintIDSemiColonFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print Y;x()")

    def testPrintIDSemiColonVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print Y;x=4")

    def testPrintIDSemiColonArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print x;4;4")

    def testPrintIDSemiColonEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print f; {}")

    def testPrintFunctionCallSemiColonValue(self):
        self.common.match_statement(const.PRINT_STMT, "print X();4")

    def testPrintFunctionCallSemiColonID(self):
        self.common.match_statement(const.PRINT_STMT, "print X();d")

    def testPrintFunctionCallSemiColonFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print Y();x()")

    def testPrintFunctionCallSemiColonVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print Y();x=4")

    def testPrintFunctionCallSemiColonArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print x();4,4")

    def testPrintFunctionCallSemiColonEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print p(); []")

    def testPrintVariableAssignmentSemiColonValue(self):
        self.common.match_statement(const.PRINT_STMT, "print X=3;4")

    def testPrintVariableAssignmentSemiColonID(self):
        self.common.match_statement(const.PRINT_STMT, "print X=4;d")

    def testPrintVariableAssignmentSemiColonFunctionCall(self):
        self.common.match_statement(const.PRINT_STMT, "print Y=4;x()")

    def testPrintVariableAssignmentSemiColonVariableAssignment(self):
        self.common.match_statement(const.PRINT_STMT, "print Y=4;x=4")

    def testPrintVariableAssignmentSemiColonArgument(self):
        self.common.match_statement(const.PRINT_STMT, "print x=1;4;4")

    def testPrintVariableAssignmentSemiColonEnumerableObject(self):
        self.common.match_statement(const.PRINT_STMT, "print x=b; {}")

    def testInvalidWhileParenthesis(self):
        self.common.status_error("print )")

    def testInvalidWhileFor(self):
        self.common.status_error("print (for)")

    def testInvalidWhileEndWhile(self):
        self.common.status_error("print endwhile")
