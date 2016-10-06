import unittest

import bslint.constants as const
import bslint.lexer.regex_handler as regex_handler


class TestReservedWordsRegex(unittest.TestCase):

    def testIF(self):
        identifier = "IF "
        exp_result = "IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.IF_STATEMENT)

    def testTHEN(self):
        identifier = "THEN "
        exp_result = "THEN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.THEN)

    def testELSE_IF(self):
        identifier = "ELSE IF "
        exp_result = "ELSE IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.IF_STATEMENT)

    def testELSE(self):
        identifier = "else "
        exp_result = "else"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEND_IF(self):
        identifier = "END IF "
        exp_result = "END IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFOR(self):
        identifier = "FOR "
        exp_result = "FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.FOR)

    def testTO(self):
        identifier = "TO "
        exp_result = "TO"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TO)

    def testEND(self):
        identifier = "END "
        exp_result = "END"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSTEP(self):
        identifier = "STEP "
        exp_result = "STEP"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.STEP)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR "
        exp_result = "EXIT FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFOR_EACH(self):
        identifier = "FOR EACH "
        exp_result = "FOR EACH"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.FOR_EACH)

    def testIN(self):
        identifier = "IN "
        exp_result = "IN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEND_FOR(self):
        identifier = "END FOR "
        exp_result = "END FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testWHILE(self):
        identifier = "WHILE "
        exp_result = "WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.WHILE)

    def testEND_WHILE(self):
        identifier = "END WHILE "
        exp_result = "END WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE "
        exp_result = "EXIT WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFUNCTION(self):
        identifier = "FUNCTION "
        exp_result = "FUNCTION"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.FUNCTION)

    def testEND_FUNCTION(self):
        identifier = "END FUNCTION "
        exp_result = "END FUNCTION"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testAS(self):
        identifier = "AS "
        exp_result = "AS"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.AS)

    def testRETURN(self):
        identifier = "RETURN "
        exp_result = "RETURN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.RETURN)

    def testPRINT(self):
        identifier = "PRINT "
        exp_result = "PRINT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.PRINT_KEYWORD)
        self.assertEqual(result["token_parser_type"], const.PRINT_KEYWORD)

    def testGOTO(self):
        identifier = "GOTO "
        exp_result = "GOTO"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.GOTO)

    def testDIM(self):
        identifier = "DIM "
        exp_result = "DIM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSTOP(self):
        identifier = "STOP "
        exp_result = "STOP"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.STOP)

    def testAND(self):
        identifier = "AND "
        exp_result = "AND"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.AND)

    def testBOX(self):
        identifier = "BOX "
        exp_result = "BOX"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCREATEOBJECT(self):
        identifier = "CREATEOBJECT "
        exp_result = "CREATEOBJECT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEACH(self):
        identifier = "EACH "
        exp_result = "EACH"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testENDIF(self):
        identifier = "ENDIF "
        exp_result = "ENDIF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testENDSUB(self):
        identifier = "ENDSUB "
        exp_result = "ENDSUB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testENDWHILE(self):
        identifier = "ENDWHILE "
        exp_result = "ENDWHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEVAL(self):
        identifier = "EVAL "
        exp_result = "EVAL"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEXIT(self):
        identifier = "EXIT "
        exp_result = "EXIT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEXITWHILE(self):
        identifier = "EXITWHILE "
        exp_result = "EXITWHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFALSE(self):
        identifier = "FALSE "
        exp_result = "FALSE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testGETGLOBALAA(self):
        identifier = "GETGLOBALAA "
        exp_result = "GETGLOBALAA"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testGETLASTRUNCOMPILEERROR(self):
        identifier = "GETLASTRUNCOMPILEERROR "
        exp_result = "GETLASTRUNCOMPILEERROR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testGETLASTRUNRUNTIMEERROR(self):
        identifier = "GETLASTRUNRUNTIMEERROR "
        exp_result = "GETLASTRUNRUNTIMEERROR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testINVALID(self):
        identifier = "INVALID "
        exp_result = "INVALID"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.INVALID)

    def testLET(self):
        identifier = "LET "
        exp_result = "LET"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLINE_NUM(self):
        identifier = "LINE_NUM "
        exp_result = "LINE_NUM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testNEXT(self):
        identifier = "NEXT "
        exp_result = "NEXT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testNOT(self):
        identifier = "NOT "
        exp_result = "NOT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.NOT)

    def testOBJFUN(self):
        identifier = "OBJFUN "
        exp_result = "OBJFUN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testOR(self):
        identifier = "OR "
        exp_result = "OR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.OR)

    def testPOS(self):
        identifier = "POS "
        exp_result = "POS"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testREM(self):
        identifier = "REM\n"
        exp_result = "REM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), exp_result)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def testRUN(self):
        identifier = "RUN "
        exp_result = "RUN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSUB(self):
        identifier = "SUB "
        exp_result = "SUB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.SUB)

    def testTAB(self):
        identifier = "TAB "
        exp_result = "TAB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testTRUE(self):
        identifier = "TRUE "
        exp_result = "TRUE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testTYPE(self):
        identifier = "TYPE "
        exp_result = "TYPE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testMAIN(self):
        identifier = "MAIN "
        exp_result = "MAIN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testQuestionMark(self):
        identifier = "?"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.PRINT_KEYWORD)
        self.assertEqual(result["token_parser_type"], const.PRINT_KEYWORD)

    def testSpaceEndSub(self):
        identifier = "end sub "
        exp_result = "end sub"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEndFunction(self):
        identifier = "endfunction "
        exp_result = "endfunction"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testTan(self):
        identifier = "Tan "
        exp_result = "Tan"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testTan(self):
        identifier = "Tan"
        exp_result = "Tan"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSqr(self):
        identifier = "Sqr"
        exp_result = "Sqr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSin(self):
        identifier = "Sin"
        exp_result = "Sin"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSgn(self):
        identifier = "Sgn"
        exp_result = "Sgn"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLog(self):
        identifier = "Log"
        exp_result = "Log"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testInt(self):
        identifier = "Int"
        exp_result = "Int"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFix(self):
        identifier = "Fix"
        exp_result = "Fix"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testExp(self):
        identifier = "Exp"
        exp_result = "Exp"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCint(self):
        identifier = "Cint"
        exp_result = "Cint"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCdbl(self):
        identifier = "Cdbl"
        exp_result = "Cdbl"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCsng(self):
        identifier = "Csng"
        exp_result = "Csng"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCos(self):
        identifier = "Cos"
        exp_result = "Cos"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testAtn(self):
        identifier = "Atn"
        exp_result = "Atn"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testAbs(self):
        identifier = "Abs"
        exp_result = "Abs"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSubstitute(self):
        identifier = "Substitute"
        exp_result = "Substitute"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testTr(self):
        identifier = "Tr"
        exp_result = "Tr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testVal(self):
        identifier = "Val"
        exp_result = "Val"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testStringi(self):
        identifier = "Stringi"
        exp_result = "Stringi"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testStri(self):
        identifier = "Stri"
        exp_result = "Stri"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testStr(self):
        identifier = "Str"
        exp_result = "Str"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testRight(self):
        identifier = "Right"
        exp_result = "Right"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLen(self):
        identifier = "Len"
        exp_result = "Len"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLeft(self):
        identifier = "Left"
        exp_result = "Left"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testInstr(self):
        identifier = "Instr"
        exp_result = "Instr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testChr(self):
        identifier = "Chr"
        exp_result = "Chr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testAsc(self):
        identifier = "Asc"
        exp_result = "Asc"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLcase(self):
        identifier = "Lcase"
        exp_result = "Lcase"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testUcase(self):
        identifier = "Ucase"
        exp_result = "Ucase"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFormatJson(self):
        identifier = "FormatJson"
        exp_result = "FormatJson"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testParseJson(self):
        identifier = "ParseJson"
        exp_result = "ParseJson"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testRunGarbageCollector(self):
        identifier = "RunGarbageCollector"
        exp_result = "RunGarbageCollector"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testStrtoi(self):
        identifier = "strtoi"
        exp_result = "strtoi"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFormatDrive(self):
        identifier = "FormatDrive"
        exp_result = "FormatDrive"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCreateDirectory(self):
        identifier = "CreateDirectory"
        exp_result = "CreateDirectory"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testDeleteDirectory(self):
        identifier = "DeleteDirectory"
        exp_result = "DeleteDirectory"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testDeleteFile(self):
        identifier = "DeleteFile"
        exp_result = "DeleteFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testMatchFiles(self):
        identifier = "MatchFiles"
        exp_result = "MatchFiles"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testMoveFile(self):
        identifier = "MoveFile"
        exp_result = "MoveFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testCopyFile(self):
        identifier = "CopyFile"
        exp_result = "CopyFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testWriteAsciiFile(self):
        identifier = "WriteAsciiFile"
        exp_result = "WriteAsciiFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testReadAsciiFile(self):
        identifier = "ReadAsciiFile"
        exp_result = "ReadAsciiFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testUpTime(self):
        identifier = "UpTime"
        exp_result = "UpTime"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testGetInterface(self):
        identifier = "GetInterface"
        exp_result = "GetInterface"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testWait(self):
        identifier = "Wait"
        exp_result = "Wait"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testSleep(self):
        identifier = "Sleep"
        exp_result = "Sleep"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEval(self):
        identifier = "Eval"
        exp_result = "Eval"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testRun(self):
        identifier = "Run"
        exp_result = "Run"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFindMemberFunction(self):
        identifier = "FindMemberFunction"
        exp_result = "FindMemberFunction"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testRnd(self):
        identifier = "Rnd"
        exp_result = "Rnd"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testType(self):
        identifier = "Type"
        exp_result = "Type"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testVoid(self):
        identifier = "Void"
        exp_result = "Void"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testDynamic(self):
        identifier = "Dynamic"
        exp_result = "Dynamic"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testFloat(self):
        identifier = "Float"
        exp_result = "Float"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testDouble(self):
        identifier = "Double"
        exp_result = "Double"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLongInteger(self):
        identifier = "LongInteger"
        exp_result = "LongInteger"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testInteger(self):
        identifier = "Integer"
        exp_result = "Integer"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testString(self):
        identifier = "String"
        exp_result = "String"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testBoolean(self):
        identifier = "Boolean"
        exp_result = "Boolean"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testObject(self):
        identifier = "Object"
        exp_result = "Object"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testUntil(self):
        identifier = "Until"
        exp_result = "Until"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testOn(self):
        identifier = "On"
        exp_result = "On"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testLibrary(self):
        identifier = "Library"
        exp_result = "Library"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testGenerate(self):
        identifier = "Generates"
        exp_result = "Generates"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testImplements(self):
        identifier = "Implements"
        exp_result = "Implements"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testEvent(self):
        identifier = "Event"
        exp_result = "Event"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def testComponent(self):
        identifier = "Component"
        exp_result = "Component"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)
