# pylint: disable=too-few-public-methods
from bslint import constants as const
from bslint.lexer.token import Token

VALUE = "value"
TYPE = "type"

class MatchHandler:
    def __init__(self):
        self._match = None
        self._token_lexer_type = None
        self._token_parser_type = None
        self._type = None

    def match_handler(self, regex_match):
        self._type = None
        self._match = regex_match[const.MATCH]
        self._token_lexer_type = regex_match[const.TOKEN_LEXER_TYPE]
        self._token_parser_type = regex_match[const.TOKEN_PARSER_TYPE]
        if self._token_lexer_type != const.COMMENT:
            return self._build_token()

    def _build_token(self):
        if self._token_lexer_type == const.ID:
            self._build_id_token()
        elif self._token_lexer_type == const.STRING:
            self._match = self._match.group(VALUE)
        else:
            self._match = self._match.group()
        return Token(self._match, self._token_lexer_type, self._token_parser_type,
                     token_type=self._type)

    def _build_id_token(self):
        if self._match.group(TYPE) is not '':
            self._type = self._match.group(TYPE)
        self._match = self._match.group(VALUE)
