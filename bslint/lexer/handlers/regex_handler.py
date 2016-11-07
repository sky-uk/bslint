import bslint.lexer.regexs as regexs
import bslint.utilities.custom_exceptions as custom_exception
from bslint import constants as const


def find_match(characters):
    token = None
    for token in regexs.REGEXS:
        match = token.regex.match(characters)
        if match:
            break
    if not match:
        raise custom_exception.UnexpectedTokenException()
    else:
        return {const.MATCH: match, const.TOKEN_LEXER_TYPE: token.lexer_type,
                const.TOKEN_PARSER_TYPE: token.parser_type,
                const.INDENTATION_LEVEL: token.indentation}
