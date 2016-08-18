import unittest
import src

class TestReservedWords(unittest.TestCase):

    def testIF(self):
        identifier = "IF"
        exp_result = [('IF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTHEN(self):
        identifier = "THEN"
        exp_result = [('THEN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testELSE_IF(self):
        identifier = "ELSE IF"
        exp_result = [('ELSE IF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testELSE(self):
        identifier = "ELSE"
        exp_result = [('ELSE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEND_IF(self):
        identifier = "END IF"
        exp_result = [('END IF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testFOR(self):
        identifier = "FOR"
        exp_result = [('FOR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTO(self):
        identifier = "TO"
        exp_result = [('TO', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSTEP(self):
        identifier = "STEP"
        exp_result = [('STEP', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR"
        exp_result = [('EXIT FOR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testFOR_EACH(self):
        identifier = "FOR EACH"
        exp_result = [('FOR EACH', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testIN(self):
        identifier = "IN"
        exp_result = [('IN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEND_FOR(self):
        identifier = "END FOR"
        exp_result = [('END FOR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testWHILE(self):
        identifier = "WHILE"
        exp_result = [('WHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEND_WHILE(self):
        identifier = "END WHILE"
        exp_result = [('END WHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE"
        exp_result = [('EXIT WHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testFUNCTION(self):
        identifier = "FUNCTION"
        exp_result = [('FUNCTION', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEND_FUNCTION(self):
        identifier = "END FUNCTION"
        exp_result = [('END FUNCTION', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testAS(self):
        identifier = "AS"
        exp_result = [('AS', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testRETURN(self):
        identifier = "RETURN"
        exp_result = [('RETURN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testPRINT(self):
        identifier = "PRINT"
        exp_result = [('PRINT', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testGOTO(self):
        identifier = "GOTO"
        exp_result = [('GOTO', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testDIM(self):
        identifier = "DIM"
        exp_result = [('DIM', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEND(self):
        identifier = "END"
        exp_result = [('END', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSTOP(self):
        identifier = "STOP"
        exp_result = [('STOP', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testAND(self):
        identifier = "AND"
        exp_result = [('AND', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testBOX(self):
        identifier = "BOX"
        exp_result = [('BOX', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testCREATEOBJECT(self):
        identifier = "CREATEOBJECT"
        exp_result = [('CREATEOBJECT', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEACH(self):
        identifier = "EACH"
        exp_result = [('EACH', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testENDIF(self):
        identifier = "ENDIF"
        exp_result = [('ENDIF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testENDSUB(self):
        identifier = "ENDSUB"
        exp_result = [('ENDSUB', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testENDWHILE(self):
        identifier = "ENDWHILE"
        exp_result = [('ENDWHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEVAL(self):
        identifier = "EVAL"
        exp_result = [('EVAL', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT(self):
        identifier = "EXIT"
        exp_result = [('EXIT', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEXITWHILE(self):
        identifier = "EXITWHILE"
        exp_result = [('EXITWHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testFALSE(self):
        identifier = "FALSE"
        exp_result = [('FALSE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testGETGLOBALAA(self):
        identifier = "GETGLOBALAA"
        exp_result = [('GETGLOBALAA', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testGETLASTRUNCOMPILEERROR(self):
        identifier = "GETLASTRUNCOMPILEERROR"
        exp_result = [('GETLASTRUNCOMPILEERROR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testGETLASTRUNRUNTIMEERROR(self):
        identifier = "GETLASTRUNRUNTIMEERROR"
        exp_result = [('GETLASTRUNRUNTIMEERROR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testINVALID(self):
        identifier = "INVALID"
        exp_result = [('INVALID', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testLET(self):
        identifier = "LET"
        exp_result = [('LET', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testLINE_NUM(self):
        identifier = "LINE_NUM"
        exp_result = [('LINE_NUM', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testNEXT(self):
        identifier = "NEXT"
        exp_result = [('NEXT', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testNOT(self):
        identifier = "NOT"
        exp_result = [('NOT', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testOBJFUN(self):
        identifier = "OBJFUN"
        exp_result = [('OBJFUN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testOR(self):
        identifier = "OR"
        exp_result = [('OR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testPOS(self):
        identifier = "POS"
        exp_result = [('POS', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testREM(self):
        identifier = "REM"
        exp_result = [('REM', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testRUN(self):
        identifier = "RUN"
        exp_result = [('RUN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSUB(self):
        identifier = "SUB"
        exp_result = [('SUB', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTAB(self):
        identifier = "TAB"
        exp_result = [('TAB', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTRUE(self):
        identifier = "TRUE"
        exp_result = [('TRUE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTYPE(self):
        identifier = "TYPE"
        exp_result = [('TYPE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testMAIN(self):
        identifier = "MAIN"
        exp_result = [('MAIN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)