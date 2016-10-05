import re

import bslint.error_messages_builder.error_builder.error_messages_constants as err_const
import bslint.error_messages_builder.error_message_handler as err
import bslint.utilities.match_handler as match_handler
import bslint.utilities.regex_handler as regex_handler
import bslint.utilities.styling_handler as styling_handler
from bslint import constants as const


class Tokenizer:
    def __init__(self, characters):
        self.tokens = []
        self.errors = []
        self.handle_match = match_handler.MatchHandler()
        self.characters = characters
        self.handle_style = styling_handler.StylingHandler(characters)
        self.preceding_token = None

    def tokenize(self):
        while self.handle_style.current_char_index < len(self.characters):
            try:
                self.create_token_and_handle_styling()
            except ValueError as e:
                if e == err_const.UNMATCHED_TOKEN:
                    self.handle_unmatched_closing_token(e)
                else:
                    self.handle_unexpected_token()
        self.handle_style.apply_new_line_styling()
        if len(self.errors) is not 0:
            return {"Status": "Error", "Tokens": self.errors, "Warnings": self.handle_style.warnings}
        else:
            return {"Status": "Success", "Tokens": self.tokens, "Warnings": self.handle_style.warnings}

    def create_token_and_handle_styling(self):
        regex_match = regex_handler.find_match(self.characters[self.handle_style.current_char_index:])
        self.handle_style.line_length += len(regex_match["match"].group())
        self.handle_style.current_char_index += len(regex_match["match"].group())
        if regex_match["token_lexer_type"] is not None:
            applied_common_styling = self.handle_style.apply_styling(regex_match)

            if applied_common_styling:
                token = self.handle_match.match_handler(regex_match)
                if token is not None:
                    token.line_number = self.handle_style.line_number
                    self.tokens.append(token)
                    self.is_valid_token(self.preceding_token, self.tokens[-1])
                    self.preceding_token = self.tokens[-1]

    def handle_unexpected_token(self):
        end_of_line = re.match(r"(.*)\n", self.characters[self.handle_style.current_char_index:])
        self.errors.append(err.get_message(err_const.UNMATCHED_QUOTATION_MARK,
                                           [(end_of_line.group()[:const.PENULTIMATE_CHARACTER]),
                                            self.handle_style.line_number]))
        self.handle_style.line_number += 1
        self.handle_style.current_char_index += len(end_of_line.group())

    def handle_unmatched_closing_token(self, message):
        self.error.append(err.get_message(err_const.UNMATCHED_TOKEN))

    @staticmethod
    def is_valid_token(preceding_token, current_token):
        return
