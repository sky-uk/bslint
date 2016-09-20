import bslint.error_messages_builder.error_message_handler as err
import re
from bslint import constants as const
import bslint.utilities.commands as commands


class MatchHandler:
    def __init__(self, characters):
        self.is_empty_line = True
        self.line_not_to_style_check = -1
        self.line_number = 1
        self.characters = characters
        self.consecutive_empty_lines = 0
        self.indentation_level = 0
        self.line_length = 0
        self.current_char_index = 0
        self.current_indentation_level = 0
        self.skip_styling_on_file = False
        self.match = None
        self.token_type = None
        self.warnings = []

    def get_last_line(self):
        last_line = re.findall("(?:(?<=^)|(?<=\n))(.*)", self.characters[:self.current_char_index - 1], re.MULTILINE)
        return last_line[-1]

    def match_handler(self, regex_match):
        self.match = regex_match["match"]
        self.token_type = regex_match["token_type"]

        if regex_match["indentation_level"] != const.NO_INDENTATION:
            self.indentation_level = regex_match["indentation_level"]

        self.apply_styling()
        token_tuple = None
        if self.token_type == const.NEW_LINE:
            self.line_number += 1
        elif self.token_type == const.BSLINT_COMMAND:
            self.apply_bslint_command()
        elif self.token_type != const.COMMENT:
            token_tuple = self.build_token()
        return token_tuple

    def apply_bslint_command(self):
        command_type = self.match.group('command')
        if command_type == "skip_line":
            self.line_not_to_style_check = commands.check_skip_line(self.line_number)
        elif command_type == "skip_file":
            self.skip_styling_on_file = commands.check_skip_file()

    def apply_styling(self):
        if self.style_checking_is_active():
            if self.token_type is const.NEW_LINE:
                self.apply_new_line_styling()
            else:
                self.apply_common_styling()

    def style_checking_is_active(self):
        return self.line_number != self.line_not_to_style_check and not self.skip_styling_on_file

    def check_trace_free(self):
        is_trace_free = commands.check_trace_free()
        self.warning_filter(is_trace_free)

    def apply_common_styling(self):
        self.is_empty_line = False
        if self.token_type == const.COMMENT:
            self.check_comment_styling()
        elif self.token_type == const.OPERATOR:
            self.check_operator_spacing()
        elif self.token_type == const.ID:
            self.check_spelling()
        elif self.token_type == const.PRINT_KEYWORD:
            self.check_trace_free()

    def check_spelling(self):
        is_spelt_correctly = commands.check_spelling(self.match.group(), self.token_type)
        self.warning_filter(is_spelt_correctly)

    def check_operator_spacing(self):
        correct_spacing = commands.check_spaces_around_operators(self.characters, self.current_char_index)
        self.warning_filter(correct_spacing)

    def check_comment_styling(self):
        is_correct_comment = commands.check_comment(self.match.group())
        self.warning_filter(is_correct_comment)
        self.check_spelling()

    def apply_new_line_styling(self):
        self.count_consecutive_new_lines()
        is_correct_line_length = commands.check_max_line_length(self.line_length)
        self.warning_filter(is_correct_line_length)

        is_consecutive_empty_lines = commands.check_consecutive_empty_lines(self.consecutive_empty_lines)
        self.warning_filter(is_consecutive_empty_lines)

        last_read_line = self.get_last_line()
        self.apply_indentation_styling(last_read_line)
        is_correct_method_declaration_spacing = commands.check_method_declaration_spacing(last_read_line)
        self.warning_filter(is_correct_method_declaration_spacing)
        self.line_length = 0

    def apply_indentation_styling(self, last_read_line):
        is_correct_indentation = commands.check_indentation(self.current_indentation_level, last_read_line,
                                                            self.indentation_level)
        if is_correct_indentation:
            self.warning_filter(is_correct_indentation[0])
            self.current_indentation_level = is_correct_indentation[1]
            self.indentation_level = 0

    def count_consecutive_new_lines(self):
        if self.is_empty_line is True:
            self.consecutive_empty_lines += 1
        else:
            self.is_empty_line = True
            self.consecutive_empty_lines = 0

    def build_token(self):
        if self.token_type == const.STRING:
            tuple_token = self.build_string_tuple()
        elif self.token_type == const.ID:
            tuple_token = self.build_id_tuple()
        else:
            tuple_token = (self.match.group(), self.token_type)
        return tuple_token + (self.line_number,)

    def build_string_tuple(self):
        group = self.match.group()
        return group[1:-1], self.token_type

    def build_id_tuple(self):
        group = self.match.group('value')
        tuple_token = (group, self.token_type)
        if self.match.group('type') is not '':
            tuple_token = (group, self.token_type, self.match.group('type'))
        return tuple_token

    def warning_filter(self, result):
        if result is not None:
            result["error_params"].append(str(self.line_number))
            warning = err.get_message(result["error_key"], result["error_params"])
            self.warnings += [warning]