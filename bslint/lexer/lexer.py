from bslint.tokenizer import Tokenizer as Tokenizer


class Lexer(Tokenizer):

    def __init__(self):
        Tokenizer.__init__(self)

    def lex(self, characters):
        return Tokenizer.tokenize(self, characters)