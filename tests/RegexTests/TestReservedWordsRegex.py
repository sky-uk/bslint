import unittest

import Constants as const
import src


class TestReservedWordsRegex(unittest.TestCase):

    def setUp(self):
        config = src.load_config_file()
        self.lexer = src.Lexer(config)
        
    def testIF(self):
        identifier = "IF"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testTHEN(self):
        identifier = "THEN"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testELSE_IF(self):
        identifier = "ELSE IF"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testELSE(self):
        identifier = "ELSE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEND_IF(self):
        identifier = "END IF"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testFOR(self):
        identifier = "FOR"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testTO(self):
        identifier = "TO"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEND(self):
        identifier = "END"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testSTEP(self):
        identifier = "STEP"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testFOR_EACH(self):
        identifier = "FOR EACH"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testIN(self):
        identifier = "IN"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEND_FOR(self):
        identifier = "END FOR"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testWHILE(self):
        identifier = "WHILE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEND_WHILE(self):
        identifier = "END WHILE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testFUNCTION(self):
        identifier = "FUNCTION"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEND_FUNCTION(self):
        identifier = "END FUNCTION"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testAS(self):
        identifier = "AS"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testRETURN(self):
        identifier = "RETURN"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testPRINT(self):
        identifier = "PRINT"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testGOTO(self):
        identifier = "GOTO"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testDIM(self):
        identifier = "DIM"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEND(self):
        identifier = "END"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testSTOP(self):
        identifier = "STOP"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testAND(self):
        identifier = "AND"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testBOX(self):
        identifier = "BOX"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testCREATEOBJECT(self):
        identifier = "CREATEOBJECT"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEACH(self):
        identifier = "EACH"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testENDIF(self):
        identifier = "ENDIF"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testENDSUB(self):
        identifier = "ENDSUB"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testENDWHILE(self):
        identifier = "ENDWHILE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEVAL(self):
        identifier = "EVAL"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEXIT(self):
        identifier = "EXIT"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEXITWHILE(self):
        identifier = "EXITWHILE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testFALSE(self):
        identifier = "FALSE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testGETGLOBALAA(self):
        identifier = "GETGLOBALAA"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testGETLASTRUNCOMPILEERROR(self):
        identifier = "GETLASTRUNCOMPILEERROR"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testGETLASTRUNRUNTIMEERROR(self):
        identifier = "GETLASTRUNRUNTIMEERROR"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testINVALID(self):
        identifier = "INVALID"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testLET(self):
        identifier = "LET"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testLINE_NUM(self):
        identifier = "LINE_NUM"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testNEXT(self):
        identifier = "NEXT"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testNOT(self):
        identifier = "NOT"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testOBJFUN(self):
        identifier = "OBJFUN"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testOR(self):
        identifier = "OR"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testPOS(self):
        identifier = "POS"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testREM(self):
        identifier = "REM\n"
        exp_result = "REM"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(exp_result, result.group())
        self.assertEqual(regex_type, const.COMMENT)

    def testRUN(self):
        identifier = "RUN"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testSUB(self):
        identifier = "SUB"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testTAB(self):
        identifier = "TAB"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testTRUE(self):
        identifier = "TRUE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testTYPE(self):
        identifier = "TYPE"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testMAIN(self):
        identifier = "MAIN"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testQuestionMark(self):
        identifier = "?"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testSpaceEndSub(self):
        identifier = "end sub"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)

    def testEndFunction(self):
        identifier = "endfunction"
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEqual(identifier, result.group())
        self.assertEqual(regex_type, const.KEYWORD)
