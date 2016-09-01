import re
import Constants as const
import src.regexs as regexs
import src
import string


class Lexer:

    def __init__(self, config):
        self.line_number = 1
        self.warnings = []
        self.config_json = config
        self.line_length = 0
        self.indentation_level = 0
        self.current_indentation_level = 0
        self.consecutive_empty_lines = 0
        self.is_empty_line = True
        self.skip_styling = False
        self.skip_line_command_number = -1

    def lex(self, characters):

        i = 0
        tokens = []
        errors = []

        while i < len(characters):
            try:
                match, token_type = self.regex_handler(characters[i:])
                i += len(match.group())
                last_line = re.findall("(?<=^).*", characters[:i], re.MULTILINE)
                if len(last_line) == 1:
                    last_line = last_line[-1]
                else:
                    last_line = last_line[-2]
                tokens = self.match_handler(match, token_type, tokens, last_line)

            except ValueError:
                end_of_line = re.match(r"(.*)\n", characters[i:])
                errors.append(("Syntax error at: " + end_of_line.group(), self.line_number))
                self.line_number += 1
                i += len(end_of_line.group())

        if not self.skip_styling:
            self.warning_filter(self.execute_BSLINT_command('max_line_length',
                                                            {"line_length": self.line_length,
                                                             "line_number": self.line_number}))

        if len(errors) is not 0:
            return {"Status": "Error", "Tokens": errors, "Warnings": self.warnings}
        else:
            return {"Status": "Success", "Tokens": tokens, "Warnings": self.warnings}

    def match_handler(self, match, token_type, tokens, characters):
        self.line_length += len(match.group())

        if token_type == const.BSLINT_COMMAND:
            command_type = match.group('command')
            if command_type == "skip_line":
                self.skip_styling = self.execute_BSLINT_command(command_type)
                self.skip_line_command_number = self.line_number

        if self.skip_styling and self.skip_line_command_number + 2 == self.line_number:
            self.skip_styling = False
            self.skip_line_command_number = -1

        if not self.skip_styling:
            self.apply_styling(match, token_type, characters)

        if token_type == const.NEW_LINE:
            self.line_number += 1

        elif token_type is not None:
            if token_type != const.BSLINT_COMMAND and token_type != const.COMMENT:
                token_tuple = self.build_token(match, token_type)
                tokens.append(token_tuple)
        return tokens

    def apply_styling(self, match, token_type, characters):
        if token_type is const.NEW_LINE:
            if self.is_empty_line is True:
                self.consecutive_empty_lines += 1
            else:
                self.is_empty_line = True
                self.consecutive_empty_lines = 0
            self.warning_filter(
                self.execute_BSLINT_command('max_line_length',
                                            {"line_length": self.line_length, "line_number": self.line_number}))
            self.line_length = 0
            result = self.execute_BSLINT_command('check_indentation',
                                                 {"current_indentation_level": self.current_indentation_level,
                                                  "line_number": self.line_number,
                                                  "characters": characters,
                                                  "indentation_level": self.indentation_level})
            self.warning_filter(result[0])
            self.current_indentation_level = result[1]
            self.indentation_level = 0
            self.warning_filter(self.execute_BSLINT_command('consecutive_empty_lines',
                                                            {"empty_lines": self.consecutive_empty_lines,
                                                             "line_number": self.line_number}))

        elif token_type is not None:
            self.is_empty_line = False
            if token_type == const.BSLINT_COMMAND:
                self.execute_BSLINT_command(match.group('command'))
            elif token_type == const.COMMENT:
                self.warning_filter(self.execute_BSLINT_command('check_comment', {"token": match.group(),
                                                                                  "line_number": self.line_number}))
                self.warning_filter(self.execute_BSLINT_command('spell_check', {"token": match.group(),
                                                                                "line_number": self.line_number,
                                                                                "type": token_type}))

            elif token_type == const.ID:
                self.warning_filter(self.execute_BSLINT_command('spell_check', {'token': match.group(), "line_number": self.line_number,
                                                        "type": token_type}))
            elif token_type == const.PRINT_KEYWORD:
                self.warning_filter(self.execute_BSLINT_command('check_trace_free', {"line_number": self.line_number}))

    def regex_handler(self, characters):
        for regex in regexs.List:
            match = re.match(regex[0], characters, re.IGNORECASE)
            if match:
                break
        if not match:
            raise ValueError('NO MATCH FOUND')
        if not regex[2] == const.NO_INDENTATION:
            self.indentation_level = regex[2]
        return match, regex[1]

    def build_token(self, match, regex_type):
        group = match.group()
        if regex_type == const.STRING:
            tuple_token = self.build_string_tuple(match, regex_type)
        elif regex_type == const.ID:
            tuple_token = self.build_id_tuple(match, regex_type)
        else:
            tuple_token = (group, regex_type)
        return tuple_token + (self.line_number,)

    @staticmethod
    def build_string_tuple(match, regex_type):
        group = match.group()
        return group[1:-1], regex_type

    @staticmethod
    def build_id_tuple(match, regex_type):
        group = match.group('value')
        tuple_token = (group, regex_type)
        if match.group('type') is not '':
            tuple_token = (group, regex_type, match.group('type'))
        return tuple_token

    def execute_BSLINT_command(self, command, params={}):
        class_name = string.capwords(command, "_").replace("_", "") + "Command"
        if self.config_json[command]['active'] is True:
            return getattr(src, class_name).execute({**params, **self.config_json[command]['params']})

    def warning_filter(self, result):
        self.warnings += filter(None, [result])