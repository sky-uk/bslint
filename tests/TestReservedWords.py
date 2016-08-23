import unittest
import src
import resources.Constants as const


class TestReservedWords(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()
        
    def testIF(self):
        identifier = "IF"
        exp_result = [('IF', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTHEN(self):
        identifier = "THEN"
        exp_result = [('THEN', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testELSE_IF(self):
        identifier = "ELSE IF"
        exp_result = [('ELSE IF', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testELSE(self):
        identifier = "ELSE"
        exp_result = [('ELSE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_IF(self):
        identifier = "END IF"
        exp_result = [('END IF', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testFOR(self):
        identifier = "FOR"
        exp_result = [('FOR', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTO(self):
        identifier = "TO"
        exp_result = [('TO', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND(self):
        identifier = "END"
        exp_result = [('END', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSTEP(self):
        identifier = "STEP"
        exp_result = [('STEP', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR"
        exp_result = [('EXIT FOR', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testFOR_EACH(self):
        identifier = "FOR EACH"
        exp_result = [('FOR EACH', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testIN(self):
        identifier = "IN"
        exp_result = [('IN', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_FOR(self):
        identifier = "END FOR"
        exp_result = [('END FOR', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testWHILE(self):
        identifier = "WHILE"
        exp_result = [('WHILE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_WHILE(self):
        identifier = "END WHILE"
        exp_result = [('END WHILE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE"
        exp_result = [('EXIT WHILE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testFUNCTION(self):
        identifier = "FUNCTION"
        exp_result = [('FUNCTION', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_FUNCTION(self):
        identifier = "END FUNCTION"
        exp_result = [('END FUNCTION', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testAS(self):
        identifier = "AS"
        exp_result = [('AS', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testRETURN(self):
        identifier = "RETURN"
        exp_result = [('RETURN', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testPRINT(self):
        identifier = "PRINT"
        exp_result = [('PRINT', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGOTO(self):
        identifier = "GOTO"
        exp_result = [('GOTO', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testDIM(self):
        identifier = "DIM"
        exp_result = [('DIM', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND(self):
        identifier = "END"
        exp_result = [('END', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSTOP(self):
        identifier = "STOP"
        exp_result = [('STOP', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testAND(self):
        identifier = "AND"
        exp_result = [('AND', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testBOX(self):
        identifier = "BOX"
        exp_result = [('BOX', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testCREATEOBJECT(self):
        identifier = "CREATEOBJECT"
        exp_result = [('CREATEOBJECT', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEACH(self):
        identifier = "EACH"
        exp_result = [('EACH', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testENDIF(self):
        identifier = "ENDIF"
        exp_result = [('ENDIF', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testENDSUB(self):
        identifier = "ENDSUB"
        exp_result = [('ENDSUB', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testENDWHILE(self):
        identifier = "ENDWHILE"
        exp_result = [('ENDWHILE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEVAL(self):
        identifier = "EVAL"
        exp_result = [('EVAL', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT(self):
        identifier = "EXIT"
        exp_result = [('EXIT', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEXITWHILE(self):
        identifier = "EXITWHILE"
        exp_result = [('EXITWHILE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testFALSE(self):
        identifier = "FALSE"
        exp_result = [('FALSE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGETGLOBALAA(self):
        identifier = "GETGLOBALAA"
        exp_result = [('GETGLOBALAA', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGETLASTRUNCOMPILEERROR(self):
        identifier = "GETLASTRUNCOMPILEERROR"
        exp_result = [('GETLASTRUNCOMPILEERROR', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testGETLASTRUNRUNTIMEERROR(self):
        identifier = "GETLASTRUNRUNTIMEERROR"
        exp_result = [('GETLASTRUNRUNTIMEERROR', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testINVALID(self):
        identifier = "INVALID"
        exp_result = [('INVALID', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testLET(self):
        identifier = "LET"
        exp_result = [('LET', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testLINE_NUM(self):
        identifier = "LINE_NUM"
        exp_result = [('LINE_NUM', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testNEXT(self):
        identifier = "NEXT"
        exp_result = [('NEXT', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testNOT(self):
        identifier = "NOT"
        exp_result = [('NOT', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testOBJFUN(self):
        identifier = "OBJFUN"
        exp_result = [('OBJFUN', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testOR(self):
        identifier = "OR"
        exp_result = [('OR', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testPOS(self):
        identifier = "POS"
        exp_result = [('POS', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testREM(self):
        identifier = "REM"
        exp_result = [('REM', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testRUN(self):
        identifier = "RUN"
        exp_result = [('RUN', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSUB(self):
        identifier = "SUB"
        exp_result = [('SUB', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTAB(self):
        identifier = "TAB"
        exp_result = [('TAB', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTRUE(self):
        identifier = "TRUE"
        exp_result = [('TRUE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTYPE(self):
        identifier = "TYPE"
        exp_result = [('TYPE', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testMAIN(self):
        identifier = "MAIN"
        exp_result = [('MAIN', const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testQuestionMark(self):
        identifier = "?"
        exp_result = [("?", const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testSpaceEndSub(self):
        identifier = "end sub"
        exp_result = [("end sub", const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)

    def testEndFunction(self):
        identifier = "endfunction"
        exp_result = [("endfunction", const.KEYWORD)]
        result = self.lexer.lex(identifier)
        self.assertEqual(result, exp_result)
