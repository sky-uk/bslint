import src.regexs as regexs
import re


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
                        try:
                            tokens.append((match.group(1), regex[1]))
                        except IndexError:
                            tokens.append((match.group(), regex[1]))
                    try:
                        i += len(match.group(1))
                    except IndexError:
                        i += len(match.group())
                    regex_matches = True
                    break
                else:
                    regex_matches = False
        else:
            print("not match found")
            break

    return tokens
