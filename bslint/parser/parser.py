from bslint.tokenizer import Tokenizer
import bslint.parser.statements_grammar as grammar
import bslint.parser.valid_token_associations as vta
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const


class Parser(Tokenizer):

    def __init__(self):
        Tokenizer.__init__(self)
        self.expected_statement = None
        self.statements_stack = []
        self.open_statements_table = {
            'function': 'endfunction',
            'while': 'endwhile',
            'for': 'endfor',
            'if': 'endif',
            'sub': 'endsub',
            'foreach': 'endfor'
        }

    def parse(self, characters):
        return Tokenizer.tokenize(self, characters)

    def check_valid_token(self, preceding_token, current_token):
        is_valid_token = current_token in vta.valid_token_associations[preceding_token]
        self.preceding_token = current_token
        return is_valid_token

    def check_valid_statement(self):
        possible_production_rules = self.find_production_with_corresponding_last_token(self.tokens[-1].token_type)
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
        return [token.token_type for token in last_tokens]

    def check_operation_stack(self, current_token):
        lowercase_token_value = current_token[0].lower().replace(" ", "")
        if lowercase_token_value in self.open_statements_table:
            self.statements_stack.append(lowercase_token_value)
        elif lowercase_token_value in self.open_statements_table.values():
            if len(self.statements_stack) == 0 or not self._statement_matches(lowercase_token_value):
                raise ValueError(err_const.UNMATCHED_TOKEN, {"expected": self.expected_statement, "actual": current_token[0]})

    def _statement_matches(self, lowercase_token_value):
        last_statement = self.statements_stack.pop()
        self.expected_statement = self.open_statements_table[last_statement]
        return self.expected_statement == lowercase_token_value
