import bslint.regexs as regexs
import re


def find_match(characters):
    for token in regexs.List:
        match = re.match(token.regex, characters, re.IGNORECASE)
        if match:
            break
    if not match:
        raise ValueError('NO MATCH FOUND')
    return {"match": match, "token_lexer_type": token.lexer_type, "token_parser_type": token.parser_type, "indentation_level": token.indentation}
