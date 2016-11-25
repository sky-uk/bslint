from bslint import constants as const
from bslint.messages import handler as msg_handler
from bslint.lexer import commands as commands
from bslint.lexer.token import Token


class StylingHandler:
    # pylint: disable=too-many-instance-attributes
    def __init__(self, lexer, characters):
        self._lexer = lexer
        self._is_empty_line = True
        self.line_number = 1
        self.line_length = 0
        self._current_indentation_level = 0
        self._indentation_level = 0
        self._token_lexer_type = None
        self._match = None
        self._consecutive_empty_lines = 0
        self.characters = characters
        self.current_char_index = 0
        self.warnings = []
        self._skip_styling_on_file = False
        self.end_of_statement = False
        self.open_curly_braces = 0
        self._line_not_to_style_check = -1
        self.function_in_object = 0

    def apply_styling(self, regex_match):
        self._match = regex_match[const.MATCH]
        self._token_lexer_type = regex_match[const.TOKEN_LEXER_TYPE]
        if regex_match[const.INDENTATION_LEVEL] != const.NO_INDENTATION:
            self._indentation_level += regex_match[const.INDENTATION_LEVEL]
        if self._token_lexer_type == const.NEW_LINE:
            self._check_new_line()
        elif self._token_lexer_type == const.BSLINT_COMMAND:
            self._check_bslint_command()
        else:
            self._apply_common_styling()
            return True
        return False

    def apply_new_line_styling(self):
        if not self._style_checking_is_active():
            return
        self._count_consecutive_new_lines()
        self._warning_filter(commands.check_max_line_length(self.line_length))
        self._warning_filter(commands.check_consecutive_empty_lines(self._consecutive_empty_lines))
        self._apply_indentation_styling(self._get_last_line())

    def check_end_of_statement(self):
        self._check_end_of_statement()
        if self.open_curly_braces != 0:
            self.end_of_statement = False

    def check_trace_free(self):
        self._warning_filter(commands.check_trace_free())

    def _set_end_of_statement(self):
        self.end_of_statement = True

    def _set_open_curly_brackets_flag(self):
        self.open_curly_braces += 1

    def _style_checking_is_active(self):
        return self.line_number != self._line_not_to_style_check and not self._skip_styling_on_file

    def _apply_common_styling(self):
        self._check_function_in_object()
        if not self._style_checking_is_active():
            return
        self._is_empty_line = False
        self._check_style_function()

    def _check_new_line(self):
        self.end_of_statement = True
        self.apply_new_line_styling()
        self.add_object_commas()
        self.line_number += 1
        self.line_length = 0

    def _check_skip_file(self):
        self._skip_styling_on_file = commands.check_skip_file()

    def _check_method_dec_spacing(self):
        self._warning_filter(commands.check_method_dec_spacing(self.characters))

    def _check_spelling(self):
        self._warning_filter(commands.check_spelling(self._match.group(), self._token_lexer_type))

    def _check_operator_spacing(self):
        self._warning_filter(commands.check_spaces_around_operators(self.characters, self.current_char_index))

    def _check_comment_styling(self):
        self._warning_filter(commands.check_comment(self._match.group()))
        self._check_spelling()

    def _get_last_line(self):
        return self.characters[:self.current_char_index].splitlines()[-1]

    def _check_skip_line(self):
        self._line_not_to_style_check = commands.check_skip_line(self.line_number)

    def _check_bslint_command(self):
        self._token_lexer_type = self._match.group(const.COMMAND)
        self._check_style_function()

    def _check_close_curly_bracket(self):
        if self._lexer.tokens[-2].parser_type == const.COMMA:
            has_trailing_comma = commands.check_trailing_comma_in_objects()
            self._warning_filter(has_trailing_comma)
            self._lexer.tokens.pop(-2)
        self.open_curly_braces -= 1

    def _apply_indentation_styling(self, last_read_line):
        self._warning_filter(commands.check_trailing_white_space(last_read_line))
        is_correct_indentation = commands.check_indentation(self._current_indentation_level,
                                                            last_read_line,
                                                            self._indentation_level)
        if is_correct_indentation:
            self._warning_filter(is_correct_indentation[0])
            self._current_indentation_level = is_correct_indentation[1]
            self._indentation_level = 0

    def _count_consecutive_new_lines(self):
        if self._is_empty_line:
            self._consecutive_empty_lines += 1
        else:
            self._is_empty_line = True
            self._consecutive_empty_lines = 0

    def _warning_filter(self, result):
        if result:
            result[const.ERROR_PARAMS].append(str(self.line_number))
            warning = msg_handler.get_error_msg(result[const.ERROR_KEY], result[const.ERROR_PARAMS])
            self.warnings += [warning]

    def add_object_commas(self, ):
        if self.open_curly_braces != 0 and self.function_in_object == 0:
            if self._lexer.tokens[-1].lexer_type != const.OPEN_CURLY_BRACKET \
                    and self._lexer.tokens[-1].parser_type != const.COMMA:
                comma_token = Token(",", const.SPECIAL_OPERATOR, const.COMMA, None)
                comma_token.line_number = self._lexer.handle_style.line_number
                self._lexer.tokens.append(comma_token)
                has_no_commas = commands.check_commas_in_objects()
                self._warning_filter(has_no_commas)

    def _check_function_in_object(self):
        if self.open_curly_braces != 0:
            if self._token_lexer_type == const.FUNCTION:
                self.function_in_object += 1
            elif self._token_lexer_type == const.END_FUNCTION_TOKEN:
                self.function_in_object -= 1

    def _check_style_function(self, *args):
        lexer_checks = {
            const.COMMENT: self._check_comment_styling,
            const.OPERATOR: self._check_operator_spacing,
            const.ID: self._check_spelling,
            const.PRINT_KEYWORD: self.check_trace_free,
            const.FUNCTION: self._check_method_dec_spacing,
            const.SUB: self._check_method_dec_spacing,
            const.SKIP_LINE: self._check_skip_line,
            const.SKIP_FILE: self. _check_skip_file,
        }
        try:
            lexer_checks[self._token_lexer_type](*args)
        except KeyError:
            pass

    def _check_end_of_statement(self):
        end_of_statement_checks = {
            const.COLON: self._set_end_of_statement,
            const.OPEN_CURLY_BRACKET: self._set_open_curly_brackets_flag,
            const.CLOSE_CURLY_BRACKET: self._check_close_curly_bracket
        }
        try:
            end_of_statement_checks[self._token_lexer_type]()
        except KeyError:
            pass
