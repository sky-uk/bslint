from bslint.tokenizer import Tokenizer
import bslint.parser.valid_token_associations as vta
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const


class Parser(Tokenizer):

    def __init__(self, characters):
        Tokenizer.__init__(self, characters)
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

    def parse(self):
        return Tokenizer.tokenize(self)

    @staticmethod
    def is_valid_token(preceding_token, current_token):
        return current_token in vta.valid_token_associations[preceding_token]

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
