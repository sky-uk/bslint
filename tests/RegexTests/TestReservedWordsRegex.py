import unittest
import src.Constants as const
import src


class TestReservedWordsRegex(unittest.TestCase):

    def setUp(self):
        self.regex_handler = src.RegexHandler()
        
    def testIF(self):
        identifier = "IF"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTHEN(self):
        identifier = "THEN"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testELSE_IF(self):
        identifier = "ELSE IF"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testELSE(self):
        identifier = "ELSE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_IF(self):
        identifier = "END IF"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFOR(self):
        identifier = "FOR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTO(self):
        identifier = "TO"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND(self):
        identifier = "END"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testSTEP(self):
        identifier = "STEP"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFOR_EACH(self):
        identifier = "FOR EACH"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testIN(self):
        identifier = "IN"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_FOR(self):
        identifier = "END FOR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testWHILE(self):
        identifier = "WHILE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_WHILE(self):
        identifier = "END WHILE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFUNCTION(self):
        identifier = "FUNCTION"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_FUNCTION(self):
        identifier = "END FUNCTION"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testAS(self):
        identifier = "AS"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testRETURN(self):
        identifier = "RETURN"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testPRINT(self):
        identifier = "PRINT"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.PRINT_KEYWORD)

    def testGOTO(self):
        identifier = "GOTO"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testDIM(self):
        identifier = "DIM"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND(self):
        identifier = "END"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testSTOP(self):
        identifier = "STOP"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testAND(self):
        identifier = "AND"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testBOX(self):
        identifier = "BOX"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testCREATEOBJECT(self):
        identifier = "CREATEOBJECT"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEACH(self):
        identifier = "EACH"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testENDIF(self):
        identifier = "ENDIF"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testENDSUB(self):
        identifier = "ENDSUB"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testENDWHILE(self):
        identifier = "ENDWHILE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEVAL(self):
        identifier = "EVAL"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXIT(self):
        identifier = "EXIT"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXITWHILE(self):
        identifier = "EXITWHILE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFALSE(self):
        identifier = "FALSE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testGETGLOBALAA(self):
        identifier = "GETGLOBALAA"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testGETLASTRUNCOMPILEERROR(self):
        identifier = "GETLASTRUNCOMPILEERROR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testGETLASTRUNRUNTIMEERROR(self):
        identifier = "GETLASTRUNRUNTIMEERROR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testINVALID(self):
        identifier = "INVALID"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testLET(self):
        identifier = "LET"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testLINE_NUM(self):
        identifier = "LINE_NUM"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testNEXT(self):
        identifier = "NEXT"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testNOT(self):
        identifier = "NOT"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testOBJFUN(self):
        identifier = "OBJFUN"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testOR(self):
        identifier = "OR"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testPOS(self):
        identifier = "POS"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testREM(self):
        identifier = "REM\n"
        exp_result = "REM"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), exp_result)
        self.assertEqual(result["token_type"], const.COMMENT)

    def testRUN(self):
        identifier = "RUN"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testSUB(self):
        identifier = "SUB"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTAB(self):
        identifier = "TAB"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTRUE(self):
        identifier = "TRUE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTYPE(self):
        identifier = "TYPE"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testMAIN(self):
        identifier = "MAIN"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testQuestionMark(self):
        identifier = "?"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.PRINT_KEYWORD)

    def testSpaceEndSub(self):
        identifier = "end sub"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEndFunction(self):
        identifier = "endfunction"
        result = self.regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.KEYWORD)
