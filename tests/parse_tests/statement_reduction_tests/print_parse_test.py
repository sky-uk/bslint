import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestPrintParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def testPrintValue(self):
        self.common.match_statement("print 4", const.PRINT_STATEMENT)

    def testPrintID(self):
        self.common.match_statement("print x", const.PRINT_STATEMENT)

    def testPrintVarAs(self):
        self.common.match_statement("print x = 3", const.PRINT_STATEMENT)

    def testPrintFunctionCall(self):
        self.common.match_statement("print x()", const.PRINT_STATEMENT)

    def testPrintEmptyAssociativeArray(self):
        self.common.match_statement("print {}", const.PRINT_STATEMENT)

    def testPrintAssociativeArray(self):
        self.common.match_statement("print {a:1}", const.PRINT_STATEMENT)

    def testPrintEmptyArray(self):
        self.common.match_statement("print []", const.PRINT_STATEMENT)

    def testPrintArray(self):
        self.common.match_statement("print [5]", const.PRINT_STATEMENT)

    def testPrintIDOperatorValue(self):
        self.common.match_statement("print x^5", const.PRINT_STATEMENT)

    def testPrintValueCommaValue(self):
        self.common.match_statement("print 3,4", const.PRINT_STATEMENT)

    def testPrintValueCommaID(self):
        self.common.match_statement("print 3,d", const.PRINT_STATEMENT)

    def testPrintValueCommaFunctionCall(self):
        self.common.match_statement("print 3,x()", const.PRINT_STATEMENT)

    def testPrintValueCommaVariableAssignment(self):
        self.common.match_statement("print 3,x=4", const.PRINT_STATEMENT)

    def testPrintValueCommaArgument(self):
        self.common.match_statement("print 3,3,4", const.PRINT_STATEMENT)

    def testPrintValueCommaEnumerableObject(self):
        self.common.match_statement("print 3, {}", const.PRINT_STATEMENT)

    def testPrintIDCommaValue(self):
        self.common.match_statement("print X,4", const.PRINT_STATEMENT)

    def testPrintIDCommaID(self):
        self.common.match_statement("print X,d", const.PRINT_STATEMENT)

    def testPrintIDCommaFunctionCall(self):
        self.common.match_statement("print Y,x()", const.PRINT_STATEMENT)

    def testPrintIDCommaVariableAssignment(self):
        self.common.match_statement("print Y,x=4", const.PRINT_STATEMENT)

    def testPrintIDCommaArgument(self):
        self.common.match_statement("print x,3,4", const.PRINT_STATEMENT)

    def testPrintIDCommaEnumerableObject(self):
        self.common.match_statement("print a, []", const.PRINT_STATEMENT)

    def testPrintFunctionCallCommaValue(self):
        self.common.match_statement("print X(),4", const.PRINT_STATEMENT)

    def testPrintFunctionCallCommaID(self):
        self.common.match_statement("print X(),d", const.PRINT_STATEMENT)

    def testPrintFunctionCallCommaFunctionCall(self):
        self.common.match_statement("print Y(),x()", const.PRINT_STATEMENT)

    def testPrintFunctionCallCommaVariableAssignment(self):
        self.common.match_statement("print Y(),x=4", const.PRINT_STATEMENT)

    def testPrintFunctionCallCommaArgument(self):
        self.common.match_statement("print x(),3,4", const.PRINT_STATEMENT)

    def testPrintFunctionCallCommaEnumerableObject(self):
        self.common.match_statement("print y(), {a:2}", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentCommaValue(self):
        self.common.match_statement("print X=3,4", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentCommaID(self):
        self.common.match_statement("print X=4,d", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentCommaFunctionCall(self):
        self.common.match_statement("print Y=4,x()", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentCommaVariableAssignment(self):
        self.common.match_statement("print Y=4,x=4", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentCommaArgument(self):
        self.common.match_statement("print x=1,4,4", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentCommaEnumerableObject(self):
        self.common.match_statement("print a = 3, {d:6}", const.PRINT_STATEMENT)

    def testPrintValueSemiColonValue(self):
        self.common.match_statement("print 3;4", const.PRINT_STATEMENT)

    def testPrintValueSemiColonID(self):
        self.common.match_statement("print d.c();x", const.PRINT_STATEMENT)

    def testPrintValueSemiColonFunctionCall(self):
        self.common.match_statement("print 3;x()", const.PRINT_STATEMENT)

    def testPrintValueSemiColonVariableAssignment(self):
        self.common.match_statement("print 3;x=4", const.PRINT_STATEMENT)

    def testPrintValueSemiColonArgument(self):
        self.common.match_statement("print 4;4,4", const.PRINT_STATEMENT)

    def testPrintValueSemiColonEnumerableObject(self):
        self.common.match_statement("print 3; [a]", const.PRINT_STATEMENT)

    def testPrintIDSemiColonValue(self):
        self.common.match_statement("print X;4", const.PRINT_STATEMENT)

    def testPrintIDSemiColonID(self):
        self.common.match_statement("print X;d", const.PRINT_STATEMENT)

    def testPrintIDSemiColonFunctionCall(self):
        self.common.match_statement("print Y;x()", const.PRINT_STATEMENT)

    def testPrintIDSemiColonVariableAssignment(self):
        self.common.match_statement("print Y;x=4", const.PRINT_STATEMENT)

    def testPrintIDSemiColonArgument(self):
        self.common.match_statement("print x;4;4", const.PRINT_STATEMENT)

    def testPrintIDSemiColonEnumerableObject(self):
        self.common.match_statement("print f; {}", const.PRINT_STATEMENT)

    def testPrintFunctionCallSemiColonValue(self):
        self.common.match_statement("print X();4", const.PRINT_STATEMENT)

    def testPrintFunctionCallSemiColonID(self):
        self.common.match_statement("print X();d", const.PRINT_STATEMENT)

    def testPrintFunctionCallSemiColonFunctionCall(self):
        self.common.match_statement("print Y();x()", const.PRINT_STATEMENT)

    def testPrintFunctionCallSemiColonVariableAssignment(self):
        self.common.match_statement("print Y();x=4", const.PRINT_STATEMENT)

    def testPrintFunctionCallSemiColonArgument(self):
        self.common.match_statement("print x();4,4", const.PRINT_STATEMENT)

    def testPrintFunctionCallSemiColonEnumerableObject(self):
        self.common.match_statement("print p(); []", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentSemiColonValue(self):
        self.common.match_statement("print X=3;4", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentSemiColonID(self):
        self.common.match_statement("print X=4;d", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentSemiColonFunctionCall(self):
        self.common.match_statement("print Y=4;x()", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentSemiColonVariableAssignment(self):
        self.common.match_statement("print Y=4;x=4", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentSemiColonArgument(self):
        self.common.match_statement("print x=1;4;4", const.PRINT_STATEMENT)

    def testPrintVariableAssignmentSemiColonEnumerableObject(self):
        self.common.match_statement("print x=b; {}", const.PRINT_STATEMENT)

    def testInvalidWhileParenthesis(self):
        self.common.exception_runner("print )")

    def testInvalidWhileFor(self):
        self.common.exception_runner("print (for)")

    def testInvalidWhileEndWhile(self):
        self.common.exception_runner("print endwhile")
