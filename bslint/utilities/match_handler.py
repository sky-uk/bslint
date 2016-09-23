from bslint.utilities.styling_handler import *


class MatchHandler:
    def __init__(self):
        self._match = None
        self._token_type = None

    def match_handler(self, regex_match):
        self._match = regex_match["match"]
        self._token_type = regex_match["token_type"]
        token_tuple = None
        if self._token_type != const.COMMENT:
            token_tuple = self._build_token()
        return token_tuple

    def _build_token(self):
        if self._token_type == const.STRING:
            tuple_token = self._build_string_tuple()
        elif self._token_type == const.ID:
            tuple_token = self._build_id_tuple()
        else:
            tuple_token = (self._match.group(), self._token_type)
        return tuple_token

    def _build_string_tuple(self):
        group = self._match.group()
        return group[1:-1], self._token_type

    def _build_id_tuple(self):
        group = self._match.group('value')
        tuple_token = (group, self._token_type)
        if self._match.group('type') is not '':
            tuple_token = (group, self._token_type, self._match.group('type'))
        return tuple_token
