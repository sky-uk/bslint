from bslint.tokenizer import Tokenizer
import bslint.parser.valid_token_associations as vta


class Parser(Tokenizer):

    def __init__(self):
        Tokenizer.__init__(self)

    def parse(self, characters):
        return Tokenizer.tokenize(self, characters)

    def check_valid_token(self, preceding_token, current_token):
        is_valid_token = current_token in vta.valid_token_associations[preceding_token]
        self.preceding_token = current_token
        return is_valid_token

