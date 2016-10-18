import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestReservedWordsRegex(unittest.TestCase):

    def test_if(self):
        identifier = "IF "
        exp_result = "IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.IF_STATEMENT)

    def test_then(self):
        identifier = "THEN "
        exp_result = "THEN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.THEN)

    def test_else_if(self):
        identifier = "ELSE IF "
        exp_result = "ELSE IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.IF_STATEMENT)

    def test_else(self):
        identifier = "else "
        exp_result = "else"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_end_if(self):
        identifier = "END IF "
        exp_result = "END IF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_IF_TOKEN)

    def test_for(self):
        identifier = "FOR "
        exp_result = "FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.FOR)

    def test_to(self):
        identifier = "TO "
        exp_result = "TO"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TO)

    def test_end(self):
        identifier = "END "
        exp_result = "END"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_TOKEN)

    def test_step(self):
        identifier = "STEP "
        exp_result = "STEP"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.STEP)

    def test_exit_for(self):
        identifier = "EXIT FOR "
        exp_result = "EXIT FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_for_each(self):
        identifier = "FOR EACH "
        exp_result = "FOR EACH"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.FOR_EACH)

    def test_in(self):
        identifier = "IN "
        exp_result = "IN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.IN)

    def test_end_for(self):
        identifier = "END FOR "
        exp_result = "END FOR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_FOR_TOKEN)

    def test_while(self):
        identifier = "WHILE "
        exp_result = "WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.WHILE)

    def test_end_while(self):
        identifier = "END WHILE "
        exp_result = "END WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_WHILE_TOKEN)

    def test_exit_while(self):
        identifier = "EXIT WHILE "
        exp_result = "EXIT WHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_function(self):
        identifier = "FUNCTION "
        exp_result = "FUNCTION"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.FUNCTION)

    def test_end_function(self):
        identifier = "END FUNCTION "
        exp_result = "END FUNCTION"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_FUNCTION_TOKEN)

    def test_as(self):
        identifier = "AS "
        exp_result = "AS"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.AS)

    def test_return(self):
        identifier = "RETURN "
        exp_result = "RETURN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.RETURN)

    def test_print(self):
        identifier = "PRINT "
        exp_result = "PRINT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.PRINT_KEYWORD)
        self.assertEqual(result["token_parser_type"], const.PRINT_KEYWORD)

    def test_goto(self):
        identifier = "GOTO "
        exp_result = "GOTO"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.GOTO)

    def test_dim(self):
        identifier = "DIM "
        exp_result = "DIM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_stop(self):
        identifier = "STOP "
        exp_result = "STOP"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.STOP)

    def test_and(self):
        identifier = "AND "
        exp_result = "AND"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.AND)

    def test_box(self):
        identifier = "BOX "
        exp_result = "BOX"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_createobject(self):
        identifier = "CREATEOBJECT "
        exp_result = "CREATEOBJECT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_each(self):
        identifier = "EACH "
        exp_result = "EACH"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_endif(self):
        identifier = "ENDIF "
        exp_result = "ENDIF"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_IF_TOKEN)

    def test_endsub(self):
        identifier = "ENDSUB "
        exp_result = "ENDSUB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_SUB_TOKEN)

    def test_endwhile(self):
        identifier = "ENDWHILE "
        exp_result = "ENDWHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_WHILE_TOKEN)

    def test_eval(self):
        identifier = "EVAL "
        exp_result = "EVAL"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_exit(self):
        identifier = "EXIT "
        exp_result = "EXIT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_exitwhile(self):
        identifier = "EXITWHILE "
        exp_result = "EXITWHILE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_false(self):
        identifier = "FALSE "
        exp_result = "FALSE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def test_getglobalaa(self):
        identifier = "GETGLOBALAA "
        exp_result = "GETGLOBALAA"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_getlastruncompileerror(self):
        identifier = "GETLASTRUNCOMPILEERROR "
        exp_result = "GETLASTRUNCOMPILEERROR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_getlastrunruntimeerror(self):
        identifier = "GETLASTRUNRUNTIMEERROR "
        exp_result = "GETLASTRUNRUNTIMEERROR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_invalid(self):
        identifier = "INVALID "
        exp_result = "INVALID"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.INVALID)

    def test_let(self):
        identifier = "LET "
        exp_result = "LET"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_line_num(self):
        identifier = "LINE_NUM "
        exp_result = "LINE_NUM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_next(self):
        identifier = "NEXT "
        exp_result = "NEXT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_not(self):
        identifier = "NOT "
        exp_result = "NOT"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.NOT)

    def test_objfun(self):
        identifier = "OBJFUN "
        exp_result = "OBJFUN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_or(self):
        identifier = "OR "
        exp_result = "OR"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.OR)

    def test_pos(self):
        identifier = "POS "
        exp_result = "POS"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_rem(self):
        identifier = "REM\n"
        exp_result = "REM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), exp_result)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def test_run_uppercase(self):
        identifier = "RUN "
        exp_result = "RUN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_sub(self):
        identifier = "SUB "
        exp_result = "SUB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.SUB)

    def test_tab(self):
        identifier = "TAB "
        exp_result = "TAB"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_true(self):
        identifier = "TRUE "
        exp_result = "TRUE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def test_type_uppercase(self):
        identifier = "TYPE "
        exp_result = "TYPE"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_main(self):
        identifier = "MAIN "
        exp_result = "MAIN"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_question_mark(self):
        identifier = "?"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.PRINT_KEYWORD)
        self.assertEqual(result["token_parser_type"], const.PRINT_KEYWORD)

    def test_space_end_sub(self):
        identifier = "end sub "
        exp_result = "end sub"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_SUB_TOKEN)

    def test_end_function_no_space(self):
        identifier = "endfunction "
        exp_result = "endfunction"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.END_FUNCTION_TOKEN)

    def test_tan(self):
        identifier = "Tan"
        exp_result = "Tan"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_sqr(self):
        identifier = "Sqr"
        exp_result = "Sqr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_sin(self):
        identifier = "Sin"
        exp_result = "Sin"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_sgn(self):
        identifier = "Sgn"
        exp_result = "Sgn"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_log(self):
        identifier = "Log"
        exp_result = "Log"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_int(self):
        identifier = "Int"
        exp_result = "Int"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_fix(self):
        identifier = "Fix"
        exp_result = "Fix"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_exp(self):
        identifier = "Exp"
        exp_result = "Exp"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_cint(self):
        identifier = "Cint"
        exp_result = "Cint"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_cdbl(self):
        identifier = "Cdbl"
        exp_result = "Cdbl"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_csng(self):
        identifier = "Csng"
        exp_result = "Csng"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_cos(self):
        identifier = "Cos"
        exp_result = "Cos"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_atn(self):
        identifier = "Atn"
        exp_result = "Atn"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_abs(self):
        identifier = "Abs"
        exp_result = "Abs"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_substitute(self):
        identifier = "Substitute"
        exp_result = "Substitute"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_tr(self):
        identifier = "Tr"
        exp_result = "Tr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_val(self):
        identifier = "Val"
        exp_result = "Val"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_stringi(self):
        identifier = "Stringi"
        exp_result = "Stringi"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_stri(self):
        identifier = "Stri"
        exp_result = "Stri"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_str(self):
        identifier = "Str"
        exp_result = "Str"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_right(self):
        identifier = "Right"
        exp_result = "Right"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_len(self):
        identifier = "Len"
        exp_result = "Len"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_left(self):
        identifier = "Left"
        exp_result = "Left"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_instr(self):
        identifier = "Instr"
        exp_result = "Instr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_chr(self):
        identifier = "Chr"
        exp_result = "Chr"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_asc(self):
        identifier = "Asc"
        exp_result = "Asc"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_lcase(self):
        identifier = "Lcase"
        exp_result = "Lcase"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_ucase(self):
        identifier = "Ucase"
        exp_result = "Ucase"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_format_json(self):
        identifier = "FormatJson"
        exp_result = "FormatJson"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_parse_json(self):
        identifier = "ParseJson"
        exp_result = "ParseJson"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_run_garbage_collector(self):
        identifier = "RunGarbageCollector"
        exp_result = "RunGarbageCollector"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_strtoi(self):
        identifier = "strtoi"
        exp_result = "strtoi"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_format_drive(self):
        identifier = "FormatDrive"
        exp_result = "FormatDrive"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_create_directory(self):
        identifier = "CreateDirectory"
        exp_result = "CreateDirectory"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_delete_directory(self):
        identifier = "DeleteDirectory"
        exp_result = "DeleteDirectory"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_delete_file(self):
        identifier = "DeleteFile"
        exp_result = "DeleteFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_match_files(self):
        identifier = "MatchFiles"
        exp_result = "MatchFiles"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_move_file(self):
        identifier = "MoveFile"
        exp_result = "MoveFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_copy_file(self):
        identifier = "CopyFile"
        exp_result = "CopyFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_write_ascii_file(self):
        identifier = "WriteAsciiFile"
        exp_result = "WriteAsciiFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_read_ascii_file(self):
        identifier = "ReadAsciiFile"
        exp_result = "ReadAsciiFile"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_up_time(self):
        identifier = "UpTime"
        exp_result = "UpTime"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_get_interface(self):
        identifier = "GetInterface"
        exp_result = "GetInterface"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_wait(self):
        identifier = "Wait"
        exp_result = "Wait"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_sleep(self):
        identifier = "Sleep"
        exp_result = "Sleep"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_eval_lowercase(self):
        identifier = "Eval"
        exp_result = "Eval"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_run(self):
        identifier = "Run"
        exp_result = "Run"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_find_member_function(self):
        identifier = "FindMemberFunction"
        exp_result = "FindMemberFunction"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_rnd(self):
        identifier = "Rnd"
        exp_result = "Rnd"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_type(self):
        identifier = "Type"
        exp_result = "Type"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_void(self):
        identifier = "Void"
        exp_result = "Void"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_dynamic(self):
        identifier = "Dynamic"
        exp_result = "Dynamic"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_float(self):
        identifier = "Float"
        exp_result = "Float"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_double(self):
        identifier = "Double"
        exp_result = "Double"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_long_integer(self):
        identifier = "LongInteger"
        exp_result = "LongInteger"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_integer(self):
        identifier = "Integer"
        exp_result = "Integer"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_string(self):
        identifier = "String"
        exp_result = "String"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_boolean(self):
        identifier = "Boolean"
        exp_result = "Boolean"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_object(self):
        identifier = "Object"
        exp_result = "Object"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.TYPE)

    def test_until(self):
        identifier = "Until"
        exp_result = "Until"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_on(self):
        identifier = "On"
        exp_result = "On"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_library(self):
        identifier = "Library"
        exp_result = "Library"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_generate(self):
        identifier = "Generates"
        exp_result = "Generates"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_implements(self):
        identifier = "Implements"
        exp_result = "Implements"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_event(self):
        identifier = "Event"
        exp_result = "Event"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)

    def test_component(self):
        identifier = "Component"
        exp_result = "Component"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.KEYWORD)
        self.assertEqual(result["token_parser_type"], const.KEYWORD)