import unittest
import bslint.constants as const
import bslint
import bslint.utilities.regex_handler as regex_handler


class TestReservedWordsRegex(unittest.TestCase):

    def testIF(self):
        identifier = "IF "
        exp_result = "IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTHEN(self):
        identifier = "THEN "
        exp_result = "THEN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testELSE_IF(self):
        identifier = "ELSE IF "
        exp_result = "ELSE IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testELSE(self):
        identifier = "else "
        exp_result = "else"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_IF(self):
        identifier = "END IF "
        exp_result = "END IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFOR(self):
        identifier = "FOR "
        exp_result = "FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTO(self):
        identifier = "TO "
        exp_result = "TO"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND(self):
        identifier = "END "
        exp_result = "END"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testSTEP(self):
        identifier = "STEP "
        exp_result = "STEP"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR "
        exp_result = "EXIT FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFOR_EACH(self):
        identifier = "FOR EACH "
        exp_result = "FOR EACH"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testIN(self):
        identifier = "IN "
        exp_result = "IN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_FOR(self):
        identifier = "END FOR "
        exp_result = "END FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testWHILE(self):
        identifier = "WHILE "
        exp_result = "WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_WHILE(self):
        identifier = "END WHILE "
        exp_result = "END WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE "
        exp_result = "EXIT WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFUNCTION(self):
        identifier = "FUNCTION "
        exp_result = "FUNCTION"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEND_FUNCTION(self):
        identifier = "END FUNCTION "
        exp_result = "END FUNCTION"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testAS(self):
        identifier = "AS "
        exp_result = "AS"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testRETURN(self):
        identifier = "RETURN "
        exp_result = "RETURN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testPRINT(self):
        identifier = "PRINT "
        exp_result = "PRINT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.PRINT_KEYWORD)

    def testGOTO(self):
        identifier = "GOTO "
        exp_result = "GOTO"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testDIM(self):
        identifier = "DIM "
        exp_result = "DIM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testSTOP(self):
        identifier = "STOP "
        exp_result = "STOP"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testAND(self):
        identifier = "AND "
        exp_result = "AND"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testBOX(self):
        identifier = "BOX "
        exp_result = "BOX"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testCREATEOBJECT(self):
        identifier = "CREATEOBJECT "
        exp_result = "CREATEOBJECT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEACH(self):
        identifier = "EACH "
        exp_result = "EACH"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testENDIF(self):
        identifier = "ENDIF "
        exp_result = "ENDIF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testENDSUB(self):
        identifier = "ENDSUB "
        exp_result = "ENDSUB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testENDWHILE(self):
        identifier = "ENDWHILE "
        exp_result = "ENDWHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEVAL(self):
        identifier = "EVAL "
        exp_result = "EVAL"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXIT(self):
        identifier = "EXIT "
        exp_result = "EXIT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEXITWHILE(self):
        identifier = "EXITWHILE "
        exp_result = "EXITWHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testFALSE(self):
        identifier = "FALSE "
        exp_result = "FALSE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testGETGLOBALAA(self):
        identifier = "GETGLOBALAA "
        exp_result = "GETGLOBALAA"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testGETLASTRUNCOMPILEERROR(self):
        identifier = "GETLASTRUNCOMPILEERROR "
        exp_result = "GETLASTRUNCOMPILEERROR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testGETLASTRUNRUNTIMEERROR(self):
        identifier = "GETLASTRUNRUNTIMEERROR "
        exp_result = "GETLASTRUNRUNTIMEERROR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testINVALID(self):
        identifier = "INVALID "
        exp_result = "INVALID"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testLET(self):
        identifier = "LET "
        exp_result = "LET"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testLINE_NUM(self):
        identifier = "LINE_NUM "
        exp_result = "LINE_NUM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testNEXT(self):
        identifier = "NEXT "
        exp_result = "NEXT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testNOT(self):
        identifier = "NOT "
        exp_result = "NOT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testOBJFUN(self):
        identifier = "OBJFUN "
        exp_result = "OBJFUN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testOR(self):
        identifier = "OR "
        exp_result = "OR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testPOS(self):
        identifier = "POS "
        exp_result = "POS"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testREM(self):
        identifier = "REM\n"
        exp_result = "REM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), exp_result)
        self.assertEqual(result["token_type"], const.COMMENT)

    def testRUN(self):
        identifier = "RUN "
        exp_result = "RUN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testSUB(self):
        identifier = "SUB "
        exp_result = "SUB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTAB(self):
        identifier = "TAB "
        exp_result = "TAB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTRUE(self):
        identifier = "TRUE "
        exp_result = "TRUE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testTYPE(self):
        identifier = "TYPE "
        exp_result = "TYPE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testMAIN(self):
        identifier = "MAIN "
        exp_result = "MAIN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testQuestionMark(self):
        identifier = "?"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.PRINT_KEYWORD)

    def testSpaceEndSub(self):
        identifier = "end sub "
        exp_result = "end sub"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)

    def testEndFunction(self):
        identifier = "endfunction "
        exp_result = "endfunction"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_type"], const.KEYWORD)
