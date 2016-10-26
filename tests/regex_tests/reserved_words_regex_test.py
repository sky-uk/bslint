import unittest

import bslint.constants as const
import bslint.lexer.handlers.regex_handler as regex_handler


class TestReservedWordsRegex(unittest.TestCase):

    def _match(self, identifier, lexer_type, parser_type):
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(1), identifier)
        self.assertEqual(result["token_lexer_type"], lexer_type)
        self.assertEqual(result["token_parser_type"], parser_type)

    def test_if(self):
        self._match("IF", const.KEYWORD, const.IF)

    def test_then(self):
        self._match("THEN", const.KEYWORD, const.THEN)

    def test_else_if(self):
        self._match("ELSE IF", const.KEYWORD, const.ELSE_IF)

    def test_else(self):
        self._match("else", const.KEYWORD, const.ELSE)

    def test_end_if(self):
        self._match("END IF", const.KEYWORD, const.END_IF_TOKEN)

    def test_for(self):
        self._match("FOR", const.KEYWORD, const.FOR)

    def test_to(self):
        self._match("TO", const.KEYWORD, const.TO)

    def test_end(self):
        self._match("END", const.KEYWORD, const.END_TOKEN)

    def test_step(self):
        self._match("STEP", const.KEYWORD, const.STEP)

    def test_exit_for(self):
        self._match("EXIT FOR", const.KEYWORD, const.KEYWORD)

    def test_for_each(self):
        self._match("FOR EACH", const.KEYWORD, const.FOR_EACH)

    def test_in(self):
        self._match("IN", const.KEYWORD, const.IN)

    def test_end_for(self):
        self._match("END FOR", const.KEYWORD, const.END_FOR_TOKEN)

    def test_while(self):
        self._match("WHILE", const.KEYWORD, const.WHILE)

    def test_end_while(self):
        self._match("END WHILE", const.KEYWORD, const.END_WHILE_TOKEN)

    def test_exit_while(self):
        self._match("EXIT WHILE", const.KEYWORD, const.KEYWORD)

    def test_function(self):
        self._match("FUNCTION", const.KEYWORD, const.FUNCTION)

    def test_end_function(self):
        self._match("END FUNCTION", const.KEYWORD, const.END_FUNCTION_TOKEN)

    def test_as(self):
        self._match("AS", const.KEYWORD, const.AS)

    def test_return(self):
        self._match("RETURN", const.KEYWORD, const.RETURN)

    def test_print(self):
        self._match("PRINT", const.PRINT_KEYWORD, const.PRINT_KEYWORD)

    def test_goto(self):
        self._match("GOTO", const.KEYWORD, const.GOTO)

    def test_dim(self):
        self._match("DIM", const.KEYWORD, const.KEYWORD)

    def test_stop(self):
        self._match("STOP", const.KEYWORD, const.STOP)

    def test_and(self):
        self._match("AND", const.KEYWORD, const.AND)

    def test_box(self):
        self._match("BOX", const.KEYWORD, const.KEYWORD)

    def test_createobject(self):
        self._match("CREATEOBJECT", const.KEYWORD, const.KEYWORD)

    def test_each(self):
        self._match("EACH", const.KEYWORD, const.KEYWORD)

    def test_endif(self):
        self._match("ENDIF", const.KEYWORD, const.END_IF_TOKEN)

    def test_endsub(self):
        self._match("ENDSUB", const.KEYWORD, const.END_SUB_TOKEN)

    def test_endwhile(self):
        self._match("ENDWHILE", const.KEYWORD, const.END_WHILE_TOKEN)

    def test_eval(self):
        self._match("EVAL", const.KEYWORD, const.KEYWORD)

    def test_exit(self):
        self._match("EXIT", const.KEYWORD, const.KEYWORD)

    def test_exitwhile(self):
        self._match("EXITWHILE", const.KEYWORD, const.KEYWORD)

    def test_false(self):
        self._match("FALSE", const.KEYWORD, const.VALUE)

    def test_getglobalaa(self):
        self._match("GETGLOBALAA", const.KEYWORD, const.KEYWORD)

    def test_getlastruncompileerror(self):
        self._match("GETLASTRUNCOMPILEERROR", const.KEYWORD, const.KEYWORD)

    def test_getlastrunruntimeerror(self):
        self._match("GETLASTRUNRUNTIMEERROR", const.KEYWORD, const.KEYWORD)

    def test_invalid(self):
        self._match("INVALID", const.KEYWORD, const.INVALID)

    def test_let(self):
        self._match("LET", const.KEYWORD, const.KEYWORD)

    def test_line_num(self):
        self._match("LINE_NUM", const.KEYWORD, const.KEYWORD)

    def test_next(self):
        self._match("NEXT", const.KEYWORD, const.KEYWORD)

    def test_not(self):
        self._match("NOT", const.KEYWORD, const.NOT)

    def test_objfun(self):
        self._match("OBJFUN", const.KEYWORD, const.KEYWORD)

    def test_or(self):
        self._match("OR", const.KEYWORD, const.OR)

    def test_pos(self):
        self._match("POS", const.KEYWORD, const.KEYWORD)

    def test_rem(self):
        self._match("REM", const.COMMENT, const.COMMENT)
        identifier = "REM\n"
        exp_result = "REM"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), exp_result)
        self.assertEqual(result["token_lexer_type"], const.COMMENT)
        self.assertEqual(result["token_parser_type"], const.COMMENT)

    def test_run_uppercase(self):
        self._match("RUN", const.KEYWORD, const.KEYWORD)

    def test_sub(self):
        self._match("SUB", const.KEYWORD, const.SUB)

    def test_tab(self):
        self._match("TAB", const.KEYWORD, const.KEYWORD)

    def test_true(self):
        self._match("TRUE", const.KEYWORD, const.VALUE)

    def test_type_uppercase(self):
        self._match("TYPE", const.KEYWORD, const.KEYWORD)

    def test_main(self):
        self._match("MAIN", const.KEYWORD, const.KEYWORD)

    def test_question_mark(self):
        identifier = "?"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_lexer_type"], const.PRINT_KEYWORD)
        self.assertEqual(result["token_parser_type"], const.PRINT_KEYWORD)

    def test_space_end_sub(self):
        self._match("end sub", const.KEYWORD, const.END_SUB_TOKEN)

    def test_end_function_no_space(self):
        self._match("endfunction", const.KEYWORD, const.END_FUNCTION_TOKEN)

    def test_tan(self):
        self._match("Tan", const.KEYWORD, const.KEYWORD)

    def test_sqr(self):
        self._match("Sqr", const.KEYWORD, const.KEYWORD)

    def test_sin(self):
        self._match("Sin", const.KEYWORD, const.KEYWORD)

    def test_sgn(self):
        self._match("Sgn", const.KEYWORD, const.KEYWORD)

    def test_log(self):
        self._match("Log", const.KEYWORD, const.KEYWORD)

    def test_int(self):
        self._match("Int", const.KEYWORD, const.KEYWORD)

    def test_fix(self):
        self._match("Fix", const.KEYWORD, const.KEYWORD)

    def test_exp(self):
        self._match("Exp", const.KEYWORD, const.KEYWORD)

    def test_cint(self):
        self._match("Cint", const.KEYWORD, const.KEYWORD)

    def test_cdbl(self):
        self._match("Cdbl", const.KEYWORD, const.KEYWORD)

    def test_csng(self):
        self._match("Csng", const.KEYWORD, const.KEYWORD)

    def test_cos(self):
        self._match("Cos", const.KEYWORD, const.KEYWORD)

    def test_atn(self):
        self._match("Atn", const.KEYWORD, const.KEYWORD)

    def test_abs(self):
        self._match("Abs", const.KEYWORD, const.KEYWORD)

    def test_substitute(self):
        self._match("Substitute", const.KEYWORD, const.KEYWORD)

    def test_tr(self):
        self._match("Tr", const.KEYWORD, const.KEYWORD)

    def test_val(self):
        self._match("Val", const.KEYWORD, const.KEYWORD)

    def test_stringi(self):
        self._match("Stringi", const.KEYWORD, const.KEYWORD)

    def test_stri(self):
        self._match("Stri", const.KEYWORD, const.KEYWORD)

    def test_str(self):
        self._match("Str", const.KEYWORD, const.KEYWORD)

    def test_right(self):
        self._match("Right", const.KEYWORD, const.KEYWORD)

    def test_len(self):
        self._match("Len", const.KEYWORD, const.KEYWORD)

    def test_left(self):
        self._match("Left", const.KEYWORD, const.KEYWORD)

    def test_instr(self):
        self._match("Instr", const.KEYWORD, const.KEYWORD)

    def test_chr(self):
        self._match("Chr", const.KEYWORD, const.KEYWORD)

    def test_asc(self):
        self._match("Asc", const.KEYWORD, const.KEYWORD)

    def test_lcase(self):
        self._match("Lcase", const.KEYWORD, const.KEYWORD)

    def test_ucase(self):
        self._match("Ucase", const.KEYWORD, const.KEYWORD)

    def test_format_json(self):
        self._match("FormatJson", const.KEYWORD, const.KEYWORD)

    def test_parse_json(self):
        self._match("ParseJson", const.KEYWORD, const.KEYWORD)

    def test_run_garbage_collector(self):
        self._match("RunGarbageCollector", const.KEYWORD, const.KEYWORD)

    def test_strtoi(self):
        self._match("strtoi", const.KEYWORD, const.KEYWORD)

    def test_format_drive(self):
        self._match("FormatDrive", const.KEYWORD, const.KEYWORD)

    def test_create_directory(self):
        self._match("CreateDirectory", const.KEYWORD, const.KEYWORD)

    def test_delete_directory(self):
        self._match("DeleteDirectory", const.KEYWORD, const.KEYWORD)

    def test_delete_file(self):
        self._match("DeleteFile", const.KEYWORD, const.KEYWORD)

    def test__match_files(self):
        self._match("matchFiles", const.KEYWORD, const.KEYWORD)

    def test_move_file(self):
        self._match("MoveFile", const.KEYWORD, const.KEYWORD)

    def test_copy_file(self):
        self._match("CopyFile", const.KEYWORD, const.KEYWORD)

    def test_write_ascii_file(self):
        self._match("WriteAsciiFile", const.KEYWORD, const.KEYWORD)

    def test_read_ascii_file(self):
        self._match("ReadAsciiFile", const.KEYWORD, const.KEYWORD)

    def test_up_time(self):
        self._match("UpTime", const.KEYWORD, const.KEYWORD)

    def test_get_interface(self):
        self._match("GetInterface", const.KEYWORD, const.KEYWORD)

    def test_wait(self):
        self._match("Wait", const.KEYWORD, const.KEYWORD)

    def test_sleep(self):
        self._match("Sleep", const.KEYWORD, const.KEYWORD)

    def test_eval_lowercase(self):
        self._match("Eval", const.KEYWORD, const.KEYWORD)

    def test_run(self):
        self._match("Run", const.KEYWORD, const.KEYWORD)

    def test_find_member_function(self):
        self._match("FindMemberFunction", const.KEYWORD, const.KEYWORD)

    def test_rnd(self):
        self._match("Rnd", const.KEYWORD, const.KEYWORD)

    def test_type(self):
        self._match("Type", const.KEYWORD, const.KEYWORD)

    def test_void(self):
        self._match("Void", const.KEYWORD, const.KEYWORD)

    def test_dynamic(self):
        self._match("Dynamic", const.KEYWORD, const.KEYWORD)

    def test_float(self):
        self._match("Float", const.KEYWORD, const.TYPE)

    def test_double(self):
        self._match("Double", const.KEYWORD, const.TYPE)

    def test_long_integer(self):
        self._match("LongInteger", const.KEYWORD, const.TYPE)

    def test_integer(self):
        self._match("Integer", const.KEYWORD, const.TYPE)

    def test_string(self):
        self._match("String", const.KEYWORD, const.TYPE)

    def test_boolean(self):
        self._match("Boolean", const.KEYWORD, const.TYPE)

    def test_object(self):
        self._match("Object", const.KEYWORD, const.TYPE)

    def test_until(self):
        self._match("Until", const.KEYWORD, const.KEYWORD)

    def test_on(self):
        self._match("On", const.KEYWORD, const.KEYWORD)

    def test_library(self):
        self._match("Library", const.KEYWORD, const.KEYWORD)

    def test_generate(self):
        self._match("Generates", const.KEYWORD, const.KEYWORD)

    def test_implements(self):
        self._match("Implements", const.KEYWORD, const.KEYWORD)

    def test_event(self):
        self._match("Event", const.KEYWORD, const.KEYWORD)

    def test_component(self):
        self._match("Component", const.KEYWORD, const.KEYWORD)