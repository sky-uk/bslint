from bslint.tokenizer import Tokenizer
import bslint.parser.statements_grammar as grammar
#import bslint.parser.valid_token_associations as vta


class Parser(Tokenizer):

    def __init__(self):
        Tokenizer.__init__(self)

    def parse(self, characters):
        return Tokenizer.tokenize(self, characters)

    def check_valid_token(self, preceding_token, current_token):
        is_valid_token = current_token in grammar.rules[preceding_token]
        self.preceding_token = current_token
        return is_valid_token

    def check_valid_statement(self):
        possible_production_rules = self.find_production_with_corresponding_last_token(self.tokens[-1][2])
        is_valid_statement = False
        for rule in possible_production_rules:
            last_tokens = self.tokens[:len(rule)]
            last_token_types = self.get_last_token_types(last_tokens)
            if rule == last_token_types:
                is_valid_statement = True
        return is_valid_statement

    def find_production_with_corresponding_last_token(self, current_token):
        corresponding_rules = []
        for rule in grammar.rules:
            if rule[len(rule) - 1] == current_token:
                corresponding_rules.append(rule)
        return corresponding_rules

    def get_last_token_types(self, last_tokens):
        return [token[2] for token in last_tokens]





