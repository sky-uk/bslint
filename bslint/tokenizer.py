import re

import bslint.error_messages_builder.error_message_handler as err
import bslint.error_messages_builder.error_messages_constants as err_const
import bslint.lexer.match_handler as match_handler
import bslint.lexer.regex_handler as regex_handler
import bslint.lexer.styling_handler as styling_handler
from bslint import constants as const


class Tokenizer:
    def __init__(self):
        self.tokens = []
        self.errors = []
        self.handle_match = match_handler.MatchHandler()
        self.characters = ""
        self.handle_style = None
        self.preceding_token = None
        self.is_valid_token = True
        self.parsing_failed = False
        self.current_token_index = 0

    def tokenize(self, characters):
        self.characters = characters
        self.handle_style = styling_handler.StylingHandler(characters)
        while self.handle_style.current_char_index < len(self.characters):
            try:
                self.create_token_and_handle_styling()
            except ValueError as e:
                if e == err_const.PARSING_FAILED:
                    self.parsing_failed = True
                else:
                    self.handle_unexpected_token()
        self.handle_style.apply_new_line_styling()
        self.check_statement_validity(self.tokens[self.current_token_index:])
        if len(self.errors) is not 0 or self.parsing_failed:
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
            if self.handle_style.end_of_statement is True:
                self.check_statement_validity(self.tokens[self.current_token_index:])
                self.handle_style.end_of_statement = False
                self.current_token_index = len(self.tokens)

    def handle_unexpected_token(self):
        end_of_line = re.match(r"(.*)\n", self.characters[self.handle_style.current_char_index:])
        if end_of_line is None:
            end_of_line = re.match(r"(.*)$", self.characters[self.handle_style.current_char_index:])
        self.errors.append(err.get_message(err_const.UNMATCHED_QUOTATION_MARK,
                                           [(end_of_line.group()[:const.PENULTIMATE_CHARACTER]),
                                            self.handle_style.line_number]))
        self.handle_style.line_number += 1
        self.handle_style.current_char_index += len(end_of_line.group())

    def check_statement_validity(self, statement):
        return

