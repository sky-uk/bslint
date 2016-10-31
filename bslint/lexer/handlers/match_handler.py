# pylint: disable=too-few-public-methods
from bslint import constants as const
from bslint.lexer.token import Token


class MatchHandler:
    def __init__(self):
        self._match = None
        self._token_lexer_type = None
        self._token_parser_type = None
        self._type = None

    def match_handler(self, regex_match):
        self._type = None
        self._match = regex_match["match"]
        self._token_lexer_type = regex_match["token_lexer_type"]
        self._token_parser_type = regex_match["token_parser_type"]
        if self._token_lexer_type != const.COMMENT:
            return self._build_token()

    def _build_token(self):
        if self._token_lexer_type == const.ID:
            self._build_id_token()
        elif self._token_lexer_type == const.STRING:
            self._match = self._match.group("value")
        else:
            self._match = self._match.group()
        return Token(self._match, self._token_lexer_type, self._token_parser_type,
                     token_type=self._type)

    def _build_id_token(self):
        if self._match.group('type') is not '':
            self._type = self._match.group('type')
        self._match = self._match.group('value')
