import src.regexs as regexs
import re
import resources.Constants as const


class Lexer:

    def lex(self, characters):
        i = 0
        tokens = []
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
                print("not match found")
                break
        return tokens

    @staticmethod
    def build_token(match, regex):
        group = match.group()
        if regex[1] == const.STRING:
            group = match.group(1)  # If string then strip quotation marks from start
        return group, regex[1]




