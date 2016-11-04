class ParsingException(Exception):
    def __init__(self, message):
        super(ParsingException, self).__init__(message)


class UnexpectedTokenException(Exception):
    pass
