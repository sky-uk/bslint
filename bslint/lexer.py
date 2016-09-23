import re

import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as err
import bslint.utilities.match_handler as match_handler
import bslint.utilities.regex_handler as regex_handler
import bslint.utilities.styling_handler as styling_handler
from bslint import constants as const


def lex(characters):
    tokens = []
    errors = []
    handle_match = match_handler.MatchHandler()
    handle_style = styling_handler.StylingHandler(characters)
    while handle_style.current_char_index < len(characters):
        try:
            create_token_and_handle_styling(characters, handle_match, handle_style, tokens)
        except ValueError:
            handle_unexpected_token(characters, errors, handle_style)

    handle_style.apply_new_line_styling()
    if len(errors) is not 0:
        return {"Status": "Error", "Tokens": errors, "Warnings": handle_style.warnings}
    else:
        return {"Status": "Success", "Tokens": tokens, "Warnings": handle_style.warnings}


def create_token_and_handle_styling(characters, handle_match, handle_style, tokens):
    regex_match = regex_handler.find_match(characters[handle_style.current_char_index:])

    handle_style.line_length += len(regex_match["match"].group())
    handle_style.current_char_index += len(regex_match["match"].group())

    if regex_match["token_type"] is not None:
        applied_common_styling = handle_style.apply_styling(regex_match)

        if applied_common_styling:
            token_tuple = handle_match.match_handler(regex_match)
            if token_tuple is not None:
                tokens.append(token_tuple + (handle_style.line_number,))


def handle_unexpected_token(characters, errors, handle_style):
    end_of_line = re.match(r"(.*)\n", characters[handle_style.current_char_index:])
    errors.append(err.get_message(err_const.UNMATCHED_QUOTATION_MARK,
                                  [(end_of_line.group()[:const.PENULTIMATE_CHARACTER]),
                                   handle_style.line_number]))
    handle_style.line_number += 1
    handle_style.current_char_index += len(end_of_line.group())




