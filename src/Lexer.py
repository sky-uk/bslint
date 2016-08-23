import src.regexs as regexs
import re
import resources.Constants as const


class Lexer:

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
                        if regex[1] is not None:
                            token_tuple = self.build_token(match, regex)
                            tokens.append(token_tuple)
                        i += len(match.group())
                        regex_matches = True
                        break
                    else:
                        regex_matches = False
            else:
                errors.append("Syntax error at: " + characters[i:i+5])
                break
        if len(errors) is not 0:
            return "Errors", errors
        else:
            return tokens

    @staticmethod
    def build_token(match, regex):
        group = match.group()
        tuple_token = (group, regex[1])
        if regex[1] == const.STRING:
            group = match.group()
            tuple_token = (group[1:-1], regex[1])
        if regex[1] == const.BSLINT_COMMAND:
            group = match.group(1)
            tuple_token = (group, regex[1])
        if regex[1] == const.ID:
            group = match.group('value')
            tuple_token = (group, regex[1])
            if match.group('type') is not '':
                tuple_token = (group, regex[1], match.group('type'))
        return tuple_token




