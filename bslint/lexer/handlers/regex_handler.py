import bslint.error_messages.constants as err_const
import bslint.lexer.regexs as regexs


def find_match(characters):
    token = None
    for token in regexs.REGEXS:
        match = token.regex.match(characters)
        if match:
            break
    if not match:
        raise ValueError(err_const.NO_MATCH_FOUND)
    else:
        return {"match": match, "token_lexer_type": token.lexer_type,
                "token_parser_type": token.parser_type, "indentation_level": token.indentation}
