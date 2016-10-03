from bslint.tokenizer import Tokenizer
import bslint.parser.parser as parser


class Parser(Tokenizer):

    def __init__(self, characters):
        Tokenizer.__init__(self, characters)

    def parse(self):
        return Tokenizer.tokenize(self)

    def check_valid_token(self, preceding_token, current_token):
        parser.is_valid_token(preceding_token, current_token)
