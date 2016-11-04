import bslint.lexer.regexs as regexs
import bslint.utilities.custom_exceptions as custom_exception


def find_match(characters):
    token = None
    for token in regexs.REGEXS:
        match = token.regex.match(characters)
        if match:
            break
    if not match:
        raise custom_exception.UnexpectedTokenException()
    else:
        return {"match": match, "token_lexer_type": token.lexer_type,
                "token_parser_type": token.parser_type, "indentation_level": token.indentation}
