from bslint.tokenizer import Tokenizer
import bslint.parser.valid_token_associations as vta


class Parser(Tokenizer):

    def __init__(self, characters):
        Tokenizer.__init__(self, characters)

    def parse(self):
        return Tokenizer.tokenize(self)

    @staticmethod
    def is_valid_token(preceding_token, current_token):
        return current_token in vta.valid_token_associations[preceding_token]
