import re

import Constants as const
import src.regexs as regexs


class Lexer:

    line_number = 1

    def lex(self, characters):
        i = 0
        tokens = []
        errors = []
        regex_matches = True
        while i < len(characters):
            if regex_matches:
                for regex in regexs.List:
                    match = re.match(regex[0], characters[i:], re.IGNORECASE)
                    if match:
                        if regex[1] is not None and regex[1] is not const.NEW_LINE:
                            token_tuple = self.build_token(match, regex)
                            tokens.append(token_tuple)
                        elif regex[1] is const.NEW_LINE:
                            self.line_number += 1
                        i += len(match.group())
                        regex_matches = True
                        break
                    else:
                        regex_matches = False
            else:
                end_of_line = re.match(r"(.*)\n", characters[i:])
                errors.append(("Syntax error at: " + end_of_line.group(), self.line_number))
                self.line_number += 1
                i += len(end_of_line.group())
                regex_matches = True
        if len(errors) is not 0:
            return "Errors", errors
        else:
            return tokens

    def build_token(self, match, regex):
        group = match.group()
        if regex[1] == const.STRING:
            tuple_token = self.build_string_tuple(match, regex)
        if regex[1] == const.BSLINT_COMMAND:
            group = match.group(1)
            tuple_token = (group, regex[1])
        elif regex[1] == const.ID:
            tuple_token = self.build_id_tuple(match, regex)
        else:
            tuple_token = (group, regex[1])
        return tuple_token + (self.line_number,)

    @staticmethod
    def build_string_tuple(match, regex):
        group = match.group()
        return group[1:-1], regex[1]

    @staticmethod
    def build_id_tuple(match, regex):
        group = match.group('value')
        tuple_token = (group, regex[1])
        if match.group('type') is not '':
            tuple_token = (group, regex[1], match.group('type'))
        return tuple_token





