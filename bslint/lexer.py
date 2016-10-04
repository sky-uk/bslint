from bslint.tokenizer import Tokenizer as Tokenizer


class Lexer(Tokenizer):

    def __init__(self, characters):
        Tokenizer.__init__(self, characters)

    def lex(self):
        return Tokenizer.tokenize(self)