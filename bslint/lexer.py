import re

import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as err
import bslint.utilities.match_handler as match_handler
import bslint.utilities.regex_handler as regex_handler
from bslint import constants as const


def lex(characters):
    tokens = []
    errors = []
    handle_match = match_handler.MatchHandler(characters)
    while handle_match.current_char_index < len(characters):
        try:
            dividing_chars_in_tokens(characters, handle_match, tokens)
        except ValueError:
            handle_non_matching_token(characters, errors, handle_match)
    if handle_match._style_checking_is_active():
        handle_match._apply_new_line_styling()
    return build_return_dict(errors, handle_match, tokens)


def dividing_chars_in_tokens(characters, handle_match, tokens):
    result = regex_handler.find_match(characters[handle_match.current_char_index:])
    handle_match.line_length += len(result["match"].group())
    handle_match.current_char_index += len(result["match"].group())
    if result["token_type"] is not None:
        token_tuple = handle_match.match_handler(result)

        if token_tuple is not None:
            tokens.append(token_tuple)


def handle_non_matching_token(characters, errors, handle_match):
    end_of_line = re.match(r"(.*)\n", characters[handle_match.current_char_index:])
    errors.append(err.get_message(err_const.UNMATCHED_QUOTATION_MARK,
                                  [(end_of_line.group()[:const.PENULTIMATE_CHARACTER]),
                                   handle_match.line_number]))
    handle_match.line_number += 1
    handle_match.current_char_index += len(end_of_line.group())


def build_return_dict(errors, handle_match, tokens):
    if len(errors) is not 0:
        return {"Status": "Error", "Tokens": errors, "Warnings": handle_match.warnings}
    else:
        return {"Status": "Success", "Tokens": tokens, "Warnings": handle_match.warnings}

