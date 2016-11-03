import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestPrintParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def testPrintValue(self):
        self.common.match_statement("print 4", const.PRINT_STMT)

    def testPrintID(self):
        self.common.match_statement("print x", const.PRINT_STMT)

    def testPrintVarAs(self):
        self.common.match_statement("print x = 3", const.PRINT_STMT)

    def testPrintFunctionCall(self):
        self.common.match_statement("print x()", const.PRINT_STMT)

    def testPrintEmptyAssociativeArray(self):
        self.common.match_statement("print {}", const.PRINT_STMT)

    def testPrintAssociativeArray(self):
        self.common.match_statement("print {a:1}", const.PRINT_STMT)

    def testPrintEmptyArray(self):
        self.common.match_statement("print []", const.PRINT_STMT)

    def testPrintArray(self):
        self.common.match_statement("print [5]", const.PRINT_STMT)

    def testPrintIDOperatorValue(self):
        self.common.match_statement("print x^5", const.PRINT_STMT)

    def testPrintValueCommaValue(self):
        self.common.match_statement("print 3,4", const.PRINT_STMT)

    def testPrintValueCommaID(self):
        self.common.match_statement("print 3,d", const.PRINT_STMT)

    def testPrintValueCommaFunctionCall(self):
        self.common.match_statement("print 3,x()", const.PRINT_STMT)

    def testPrintValueCommaVariableAssignment(self):
        self.common.match_statement("print 3,x=4", const.PRINT_STMT)

    def testPrintValueCommaArgument(self):
        self.common.match_statement("print 3,3,4", const.PRINT_STMT)

    def testPrintValueCommaEnumerableObject(self):
        self.common.match_statement("print 3, {}", const.PRINT_STMT)

    def testPrintIDCommaValue(self):
        self.common.match_statement("print X,4", const.PRINT_STMT)

    def testPrintIDCommaID(self):
        self.common.match_statement("print X,d", const.PRINT_STMT)

    def testPrintIDCommaFunctionCall(self):
        self.common.match_statement("print Y,x()", const.PRINT_STMT)

    def testPrintIDCommaVariableAssignment(self):
        self.common.match_statement("print Y,x=4", const.PRINT_STMT)

    def testPrintIDCommaArgument(self):
        self.common.match_statement("print x,3,4", const.PRINT_STMT)

    def testPrintIDCommaEnumerableObject(self):
        self.common.match_statement("print a, []", const.PRINT_STMT)

    def testPrintFunctionCallCommaValue(self):
        self.common.match_statement("print X(),4", const.PRINT_STMT)

    def testPrintFunctionCallCommaID(self):
        self.common.match_statement("print X(),d", const.PRINT_STMT)

    def testPrintFunctionCallCommaFunctionCall(self):
        self.common.match_statement("print Y(),x()", const.PRINT_STMT)

    def testPrintFunctionCallCommaVariableAssignment(self):
        self.common.match_statement("print Y(),x=4", const.PRINT_STMT)

    def testPrintFunctionCallCommaArgument(self):
        self.common.match_statement("print x(),3,4", const.PRINT_STMT)

    def testPrintFunctionCallCommaEnumerableObject(self):
        self.common.match_statement("print y(), {a:2}", const.PRINT_STMT)

    def testPrintVariableAssignmentCommaValue(self):
        self.common.match_statement("print X=3,4", const.PRINT_STMT)

    def testPrintVariableAssignmentCommaID(self):
        self.common.match_statement("print X=4,d", const.PRINT_STMT)

    def testPrintVariableAssignmentCommaFunctionCall(self):
        self.common.match_statement("print Y=4,x()", const.PRINT_STMT)

    def testPrintVariableAssignmentCommaVariableAssignment(self):
        self.common.match_statement("print Y=4,x=4", const.PRINT_STMT)

    def testPrintVariableAssignmentCommaArgument(self):
        self.common.match_statement("print x=1,4,4", const.PRINT_STMT)

    def testPrintVariableAssignmentCommaEnumerableObject(self):
        self.common.match_statement("print a = 3, {d:6}", const.PRINT_STMT)

    def testPrintValueSemiColonValue(self):
        self.common.match_statement("print 3;4", const.PRINT_STMT)

    def testPrintValueSemiColonID(self):
        self.common.match_statement("print d.c();x", const.PRINT_STMT)

    def testPrintValueSemiColonFunctionCall(self):
        self.common.match_statement("print 3;x()", const.PRINT_STMT)

    def testPrintValueSemiColonVariableAssignment(self):
        self.common.match_statement("print 3;x=4", const.PRINT_STMT)

    def testPrintValueSemiColonArgument(self):
        self.common.match_statement("print 4;4,4", const.PRINT_STMT)

    def testPrintValueSemiColonEnumerableObject(self):
        self.common.match_statement("print 3; [a]", const.PRINT_STMT)

    def testPrintIDSemiColonValue(self):
        self.common.match_statement("print X;4", const.PRINT_STMT)

    def testPrintIDSemiColonID(self):
        self.common.match_statement("print X;d", const.PRINT_STMT)

    def testPrintIDSemiColonFunctionCall(self):
        self.common.match_statement("print Y;x()", const.PRINT_STMT)

    def testPrintIDSemiColonVariableAssignment(self):
        self.common.match_statement("print Y;x=4", const.PRINT_STMT)

    def testPrintIDSemiColonArgument(self):
        self.common.match_statement("print x;4;4", const.PRINT_STMT)

    def testPrintIDSemiColonEnumerableObject(self):
        self.common.match_statement("print f; {}", const.PRINT_STMT)

    def testPrintFunctionCallSemiColonValue(self):
        self.common.match_statement("print X();4", const.PRINT_STMT)

    def testPrintFunctionCallSemiColonID(self):
        self.common.match_statement("print X();d", const.PRINT_STMT)

    def testPrintFunctionCallSemiColonFunctionCall(self):
        self.common.match_statement("print Y();x()", const.PRINT_STMT)

    def testPrintFunctionCallSemiColonVariableAssignment(self):
        self.common.match_statement("print Y();x=4", const.PRINT_STMT)

    def testPrintFunctionCallSemiColonArgument(self):
        self.common.match_statement("print x();4,4", const.PRINT_STMT)

    def testPrintFunctionCallSemiColonEnumerableObject(self):
        self.common.match_statement("print p(); []", const.PRINT_STMT)

    def testPrintVariableAssignmentSemiColonValue(self):
        self.common.match_statement("print X=3;4", const.PRINT_STMT)

    def testPrintVariableAssignmentSemiColonID(self):
        self.common.match_statement("print X=4;d", const.PRINT_STMT)

    def testPrintVariableAssignmentSemiColonFunctionCall(self):
        self.common.match_statement("print Y=4;x()", const.PRINT_STMT)

    def testPrintVariableAssignmentSemiColonVariableAssignment(self):
        self.common.match_statement("print Y=4;x=4", const.PRINT_STMT)

    def testPrintVariableAssignmentSemiColonArgument(self):
        self.common.match_statement("print x=1;4;4", const.PRINT_STMT)

    def testPrintVariableAssignmentSemiColonEnumerableObject(self):
        self.common.match_statement("print x=b; {}", const.PRINT_STMT)

    def testInvalidWhileParenthesis(self):
        self.common.status_error("print )")

    def testInvalidWhileFor(self):
        self.common.status_error("print (for)")

    def testInvalidWhileEndWhile(self):
        self.common.status_error("print endwhile")
