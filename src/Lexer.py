import re
import src.Constants as const
import src
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class Lexer:

    def __init__(self, config):
        self.regex_handler = src.RegexHandler()
        self.error = Err.ErrorMessageHandler()
        self.line_number = 1
        self.warnings = []
        self.config_json = config
        self.line_length = 0
        self.indentation_level = 0
        self.current_indentation_level = 0
        self.consecutive_empty_lines = 0
        self.is_empty_line = True
        self.styling_rule_handler = src.StylingRulesHandler(config)
        self.line_not_to_style_check = -1
        self.skip_styling_on_file = False
        self.characters = ""
        self.error_message_handler = Err.ErrorMessageHandler()
        self.spaces_around_operators_config = config['spaces_around_operators']["params"]['spaces_around_operators']
        self.current_char_index = 0
        self.match = None
        self.token_type = None
        self.last_read_line = ''

    def lex(self, characters):
        self.characters = characters
        tokens = []
        errors = []
        self.skip_styling_on_file = False

        while self.current_char_index < len(self.characters):
            try:
                result = self.regex_handler.find_match(self.characters[self.current_char_index:])
                self.match = result["match"]
                self.token_type = result["token_type"]
                if result["indentation_level"] != const.NO_INDENTATION:
                    self.indentation_level = result["indentation_level"]

                self.current_char_index += len(self.match.group())
                self.line_length += len(self.match.group())
                if self.token_type is not None:
                    tokens = self.match_handler(tokens)

            except ValueError:
                end_of_line = re.match(r"(.*)\n", self.characters[self.current_char_index:])
                errors.append(self.error.get(ErrConst.UNMATCHED_QUOTATION_MARK,
                                             [(end_of_line.group()[:const.PENULTIMATE_CHARACTER]), self.line_number]))
                self.line_number += 1
                self.current_char_index += len(end_of_line.group())
        if self.style_checking_is_active():
            self.apply_new_line_styling()
        if len(errors) is not 0:
            return {"Status": "Error", "Tokens": errors, "Warnings": self.warnings}
        else:
            return {"Status": "Success", "Tokens": tokens, "Warnings": self.warnings}

    def get_last_line(self):
        last_line = re.findall("(?:(?<=^)|(?<=\n))(.*)", self.characters[:self.current_char_index - 1], re.MULTILINE)
        self.last_read_line = last_line[-1]

    def match_handler(self, tokens):
        self.apply_styling()
        if self.token_type == const.NEW_LINE:
            self.line_number += 1
        elif self.token_type == const.BSLINT_COMMAND:
            self.apply_bslint_command()
        elif self.token_type != const.COMMENT:
            token_tuple = self.build_token()
            tokens.append(token_tuple)
        return tokens

    def apply_bslint_command(self):
        command_type = self.match.group('command')
        if command_type == "skip_line":
            self.line_not_to_style_check = self.check_style_rule(command_type, {"line_number": self.line_number})
        elif command_type == "skip_file":
            self.skip_styling_on_file = self.check_style_rule(command_type)

    def apply_styling(self):
        if self.style_checking_is_active():
            if self.token_type is const.NEW_LINE:
                self.apply_new_line_styling()
            else:
                self.apply_common_styling()

    def style_checking_is_active(self):
        return self.line_number != self.line_not_to_style_check and not self.skip_styling_on_file

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

    def check_trace_free(self):
        is_trace_free = self.check_style_rule('check_trace_free')
        self.warning_filter(is_trace_free)

    def check_spelling(self):
        is_spelt_correctly = self.check_style_rule('spell_check',
                                                   {'token': self.match.group(), "type": self.token_type})
        self.warning_filter(is_spelt_correctly)

    def check_operator_spacing(self):
        before_index = self.current_char_index - self.spaces_around_operators_config - 2
        after_index = self.current_char_index + self.spaces_around_operators_config + 1
        characters_around_operator = self.characters[before_index:after_index]
        correct_spacing = self.check_style_rule('spaces_around_operators', {"characters": characters_around_operator})
        self.warning_filter(correct_spacing)

    def check_comment_styling(self):
        is_correct_comment = self.check_style_rule('check_comment', {"token": self.match.group()})
        self.warning_filter(is_correct_comment)
        self.check_spelling()

    def apply_new_line_styling(self):
        self.count_consecutive_new_lines()
        is_correct_line_length = self.check_style_rule('max_line_length',
                                                       {"line_length": self.line_length})
        self.warning_filter(is_correct_line_length)
        is_consecutive_empty_lines = self.check_style_rule('consecutive_empty_lines',
                                                           {"empty_lines": self.consecutive_empty_lines})
        self.warning_filter(is_consecutive_empty_lines)
        self.apply_indentation_styling()
        self.line_length = 0

    def apply_indentation_styling(self):
        self.get_last_line()
        is_correct_indentation = self.check_style_rule('check_indentation',
                                                       {"current_indentation_level": self.current_indentation_level,
                                                        "characters": self.last_read_line,
                                                        "indentation_level": self.indentation_level})
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

    def check_style_rule(self, command, params={}):
        return self.styling_rule_handler.apply(command, params)

    def warning_filter(self, result):
        if result is not None:
            result["error_params"].append(str(self.line_number))
            warning = self.error_message_handler.get(result["error_key"], result["error_params"])
            self.warnings += [warning]
