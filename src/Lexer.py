import re

import Constants as const
import src.regexs as regexs
import src
import string


class Lexer:
    def __init__(self):
        self.line_number = 1
        self.warnings = []

    def lex(self, characters):

        i = 0
        tokens = []
        errors = []

        while i < len(characters):
            try:
                match, token_type = self.regex_handler(characters[i:])
                i += len(match.group())
                tokens = self.match_handler(match, token_type, tokens)
            except ValueError:
                end_of_line = re.match(r"(.*)\n", characters[i:])
                errors.append(("Syntax error at: " + end_of_line.group(), self.line_number))
                self.line_number += 1
                i += len(end_of_line.group())
        if len(errors) is not 0:
            return {"Status": "Error", "Tokens": errors, "Warnings": self.warnings}
        else:
            return {"Status": "Success", "Tokens": tokens, "Warnings": self.warnings}

    def spell_check(self, tokens):
        print(tokens)

    def match_handler(self, match, token_type, tokens):
        if token_type is const.NEW_LINE:
            self.line_number += 1
        elif token_type == const.BSLINT_COMMAND:
            self.execute_BSLINT_command(match.group('command'))
        elif token_type == const.COMMENT:
            self.warning_filter(self.execute_BSLINT_command('check_comment', {"token": match.group(),
                                                                              "line_number": self.line_number}))
            self.warning_filter(self.execute_BSLINT_command('spell_check', {"token": match.group(),
                                                                            "line_number": self.line_number,
                                                                            "type": token_type}))

        elif token_type is not None:
            token_tuple = self.build_token(match, token_type)
            tokens.append(token_tuple)

        return tokens

    @staticmethod
    def regex_handler(characters):
        for regex in regexs.List:
            match = re.match(regex[0], characters, re.IGNORECASE)
            if match:
                break
        if not match:
            raise ValueError('NO MATCH FOUND')
        return match, regex[1]

    def build_token(self, match, regex_type):
        group = match.group()
        if regex_type == const.STRING:
            tuple_token = self.build_string_tuple(match, regex_type)
        elif regex_type == const.ID:
            tuple_token = self.build_id_tuple(match, regex_type)
            self.warning_filter(
                self.execute_BSLINT_command('spell_check', {'token': match.group(), "line_number": self.line_number,
                                                            "type": regex_type}))
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

    @staticmethod
    def execute_BSLINT_command(command, params={}):
        class_name = string.capwords(command, "_").replace("_", "") + "Command"
        return getattr(src, class_name).execute(params)

    def warning_filter(self, result):
        self.warnings += filter(None, [result])
