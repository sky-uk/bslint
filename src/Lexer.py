import src.regexs as regexs
import re
import resources.Constants as const


def lexer(characters):
    i = 0
    tokens = []
    regex_matches = True
    while i < len(characters):
        if regex_matches:
            for regex in regexs.List:
                match = re.match(regex[0], characters[i:], re.IGNORECASE)
                if match:
                    if regex[1] is not None:
                        group = match.group()
                        if regex[1] == const.STRING:
                            group = match.group(1)  # If string then strip quotation marks from start
                        tokens.append((group, regex[1]))
                    i += len(match.group())  # -1 access last element in list
                    regex_matches = True
                    break
                else:
                    regex_matches = False
        else:
            print("not match found")
            break

    return tokens
