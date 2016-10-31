# pylint: disable=too-few-public-methods
class Token:
    # pylint: disable=too-many-arguments
    def __init__(self, group, lex_type, parse_type, line_number=None, token_type=None):
        self.group = group
        self.lexer_type = lex_type
        self.parser_type = parse_type
        self.token_type = token_type
        self.line_number = line_number

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
