import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler
from tests.resources.common.test_methods import CommonMethods as Common


class TestReservedWordsRegex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_if(self):
        self.common.match_regex("IF", 1, const.KEYWORD, const.IF)

    def test_then(self):
        self.common.match_regex("THEN", 1, const.KEYWORD, const.THEN)

    def test_else_if(self):
        self.common.match_regex("ELSE IF", 1, const.KEYWORD, const.ELSE_IF)

    def test_else(self):
        self.common.match_regex("else", 1, const.KEYWORD, const.ELSE)

    def test_end_if(self):
        self.common.match_regex("END IF", 1, const.KEYWORD, const.END_IF_TOKEN)

    def test_for(self):
        self.common.match_regex("FOR", 1, const.KEYWORD, const.FOR)

    def test_to(self):
        self.common.match_regex("TO", 1, const.KEYWORD, const.TO)

    def test_end(self):
        self.common.match_regex("END", 1, const.KEYWORD, const.END_TOKEN)

    def test_step(self):
        self.common.match_regex("STEP", 1, const.KEYWORD, const.STEP)

    def test_exit_for(self):
        self.common.match_regex("EXIT FOR", 1, const.KEYWORD, const.EXIT)

    def test_for_each(self):
        self.common.match_regex("FOR EACH", 1, const.KEYWORD, const.FOR_EACH)

    def test_in(self):
        self.common.match_regex("IN", 1, const.KEYWORD, const.IN)

    def test_end_for(self):
        self.common.match_regex("END FOR", 1, const.KEYWORD, const.END_FOR_TOKEN)

    def test_while(self):
        self.common.match_regex("WHILE", 1, const.KEYWORD, const.WHILE)

    def test_end_while(self):
        self.common.match_regex("END WHILE", 1, const.KEYWORD, const.END_WHILE_TOKEN)

    def test_exit_while(self):
        self.common.match_regex("EXIT WHILE", 1, const.KEYWORD, const.EXIT)

    def test_function(self):
        self.common.match_regex("FUNCTION", 1, const.FUNCTION, const.FUNCTION)

    def test_end_function(self):
        self.common.match_regex("END FUNCTION", 1, const.END_FUNCTION_TOKEN, const.END_FUNCTION_TOKEN)

    def test_as(self):
        self.common.match_regex("AS", 1, const.KEYWORD, const.AS)

    def test_return(self):
        self.common.match_regex("RETURN", 1, const.KEYWORD, const.RETURN)

    def test_print(self):
        self.common.match_regex("PRINT", 1, const.PRINT_KEYWORD, const.PRINT_KEYWORD)

    def test_goto(self):
        self.common.match_regex("GOTO", 1, const.KEYWORD, const.GOTO)

    def test_dim(self):
        self.common.match_regex("DIM", 1, const.KEYWORD, const.KEYWORD)

    def test_stop(self):
        self.common.match_regex("STOP", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_and(self):
        self.common.match_regex("AND", 1, const.KEYWORD, const.AND)

    def test_box(self):
        self.common.match_regex("BOX", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_createobject(self):
        self.common.match_regex("CREATEOBJECT", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_each(self):
        self.common.match_regex("EACH", 1, const.KEYWORD, const.KEYWORD)

    def test_endif(self):
        self.common.match_regex("ENDIF", 1, const.KEYWORD, const.END_IF_TOKEN)

    def test_endsub(self):
        self.common.match_regex("ENDSUB", 1, const.KEYWORD, const.END_SUB_TOKEN)

    def test_endwhile(self):
        self.common.match_regex("ENDWHILE", 1, const.KEYWORD, const.END_WHILE_TOKEN)

    def test_eval(self):
        self.common.match_regex("EVAL", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_exit(self):
        self.common.match_regex("EXIT", 1, const.KEYWORD, const.EXIT)

    def test_exitwhile(self):
        self.common.match_regex("EXITWHILE", 1, const.KEYWORD, const.EXIT)

    def test_false(self):
        self.common.match_regex("FALSE", 1, const.KEYWORD, const.VALUE)

    def test_getglobalaa(self):
        self.common.match_regex("GETGLOBALAA", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_getlastruncompileerror(self):
        self.common.match_regex("GETLASTRUNCOMPILEERROR", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_getlastrunruntimeerror(self):
        self.common.match_regex("GETLASTRUNRUNTIMEERROR", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_invalid(self):
        self.common.match_regex("INVALID", 1, const.KEYWORD, const.VALUE)

    def test_let(self):
        self.common.match_regex("LET", 1, const.KEYWORD, const.KEYWORD)

    def test_line_num(self):
        self.common.match_regex("LINE_NUM", 1, const.KEYWORD, const.KEYWORD)

    def test_next(self):
        self.common.match_regex("NEXT", 1, const.KEYWORD, const.KEYWORD)

    def test_not(self):
        self.common.match_regex("NOT", 1, const.KEYWORD, const.NOT)

    def test_objfun(self):
        self.common.match_regex("OBJFUN", 1, const.KEYWORD, const.KEYWORD)

    def test_or(self):
        self.common.match_regex("OR", 1, const.KEYWORD, const.OR)

    def test_pos(self):
        self.common.match_regex("POS", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_rem(self):
        self.common.match_regex("REM", 1, const.COMMENT, const.COMMENT)
        identifier = "REM\n"
        expected = "REM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(expected, result["match"].group())
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def test_run_uppercase(self):
        self.common.match_regex("RUN", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_sub(self):
        self.common.match_regex("SUB", 1, const.SUB, const.SUB)

    def test_tab(self):
        self.common.match_regex("TAB", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_true(self):
        self.common.match_regex("TRUE", 1, const.KEYWORD, const.VALUE)

    def test_type_uppercase(self):
        self.common.match_regex("TYPE", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_main(self):
        self.common.match_regex("MAIN", 1, const.ID, const.ID)

    def test_question_mark(self):
        self.common.match_regex("?", 0, const.PRINT_KEYWORD, const.PRINT_KEYWORD)

    def test_space_end_sub(self):
        self.common.match_regex("end sub", 1, const.KEYWORD, const.END_SUB_TOKEN)

    def test_end_function_no_space(self):
        self.common.match_regex("endfunction", 1, const.END_FUNCTION_TOKEN, const.END_FUNCTION_TOKEN)

    def test_tan(self):
        self.common.match_regex("Tan", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_sqr(self):
        self.common.match_regex("Sqr", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_sin(self):
        self.common.match_regex("Sin", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_sgn(self):
        self.common.match_regex("Sgn", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_log(self):
        self.common.match_regex("Log", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_int(self):
        self.common.match_regex("Int", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_fix(self):
        self.common.match_regex("Fix", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_exp(self):
        self.common.match_regex("Exp", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_cint(self):
        self.common.match_regex("Cint", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_cdbl(self):
        self.common.match_regex("Cdbl", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_csng(self):
        self.common.match_regex("Csng", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_cos(self):
        self.common.match_regex("Cos", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_atn(self):
        self.common.match_regex("Atn", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_abs(self):
        self.common.match_regex("Abs", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_substitute(self):
        self.common.match_regex("Substitute", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_tr(self):
        self.common.match_regex("Tr", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_val(self):
        self.common.match_regex("Val", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_stringi(self):
        self.common.match_regex("Stringi", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_stri(self):
        self.common.match_regex("Stri", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_str(self):
        self.common.match_regex("Str", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_right(self):
        self.common.match_regex("Right", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_len(self):
        self.common.match_regex("Len", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_left(self):
        self.common.match_regex("Left", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_instr(self):
        self.common.match_regex("Instr", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_chr(self):
        self.common.match_regex("Chr", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_asc(self):
        self.common.match_regex("Asc", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_lcase(self):
        self.common.match_regex("Lcase", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_ucase(self):
        self.common.match_regex("Ucase", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_format_json(self):
        self.common.match_regex("FormatJson", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_parse_json(self):
        self.common.match_regex("ParseJson", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_run_garbage_collector(self):
        self.common.match_regex("RunGarbageCollector", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_strtoi(self):
        self.common.match_regex("strtoi", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_format_drive(self):
        self.common.match_regex("FormatDrive", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_create_directory(self):
        self.common.match_regex("CreateDirectory", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_delete_directory(self):
        self.common.match_regex("DeleteDirectory", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_delete_file(self):
        self.common.match_regex("DeleteFile", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test__match_files(self):
        self.common.match_regex("matchFiles", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_move_file(self):
        self.common.match_regex("MoveFile", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_copy_file(self):
        self.common.match_regex("CopyFile", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_write_ascii_file(self):
        self.common.match_regex("WriteAsciiFile", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_read_ascii_file(self):
        self.common.match_regex("ReadAsciiFile", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_up_time(self):
        self.common.match_regex("UpTime", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_get_interface(self):
        self.common.match_regex("GetInterface", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_wait(self):
        self.common.match_regex("Wait", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_sleep(self):
        self.common.match_regex("Sleep", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_eval_lowercase(self):
        self.common.match_regex("Eval", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_run(self):
        self.common.match_regex("Run", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_find_member_function(self):
        self.common.match_regex("FindMemberFunction", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_rnd(self):
        self.common.match_regex("Rnd", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_mid(self):
        self.common.match_regex("Mid", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_type(self):
        self.common.match_regex("Type", 1, const.KEYWORD, const.BUILT_IN_FUNCTION)

    def test_void(self):
        self.common.match_regex("Void", 1, const.KEYWORD, const.TYPE)

    def test_dynamic(self):
        self.common.match_regex("Dynamic", 1, const.KEYWORD, const.TYPE)

    def test_float(self):
        self.common.match_regex("Float", 1, const.KEYWORD, const.TYPE)

    def test_double(self):
        self.common.match_regex("Double", 1, const.KEYWORD, const.TYPE)

    def test_long_integer(self):
        self.common.match_regex("LongInteger", 1, const.KEYWORD, const.TYPE)

    def test_integer(self):
        self.common.match_regex("Integer", 1, const.KEYWORD, const.TYPE)

    def test_string(self):
        self.common.match_regex("String", 1, const.KEYWORD, const.TYPE)

    def test_boolean(self):
        self.common.match_regex("Boolean", 1, const.KEYWORD, const.TYPE)

    def test_object(self):
        self.common.match_regex("Object", 1, const.KEYWORD, const.TYPE)

    def test_until(self):
        self.common.match_regex("Until", 1, const.KEYWORD, const.KEYWORD)

    def test_on(self):
        self.common.match_regex("On", 1, const.KEYWORD, const.KEYWORD)

    def test_library(self):
        self.common.match_regex("Library", 1, const.KEYWORD, const.KEYWORD)

    def test_generate(self):
        self.common.match_regex("Generates", 1, const.KEYWORD, const.KEYWORD)

    def test_implements(self):
        self.common.match_regex("Implements", 1, const.KEYWORD, const.KEYWORD)

    def test_component(self):
        self.common.match_regex("Component", 1, const.KEYWORD, const.KEYWORD)

    def test_assertTrue(self):
        self.common.match_regex("assertTrue", 1, const.ASSERT, const.ASSERT)

    def test_assertFalse(self):
        self.common.match_regex("assertFalse", 1, const.ASSERT, const.ASSERT)

    def test_assertEqual(self):
        self.common.match_regex("assertEqual", 1, const.ASSERT, const.ASSERT)
