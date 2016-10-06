import bslint.regexs as regexs
import re
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const


def find_match(characters):
    for token in regexs.List:
        match = re.match(token.regex, characters, re.IGNORECASE)
        if match:
            break
    if not match:
        raise ValueError(err_const.NO_MATCH_FOUND)
    return {"match": match, "token_lexer_type": token.lexer_type, "token_parser_type": token.parser_type, "indentation_level": token.indentation}
