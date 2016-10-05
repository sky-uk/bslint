from bslint.tokenizer import Tokenizer
import bslint.parser.valid_token_associations as vta


class Parser(Tokenizer):

    def __init__(self, characters):
        Tokenizer.__init__(self, characters)
        self.statements_stack = []
        self.open_statements_table = {
            'function': 'endfunction',
            'while': 'endwhile',
            'for': 'endfor',
            'if': 'endif',
            'sub': 'endsub',
            'foreach': 'endfor'
        }
        self.closing_statements_table = {
            'endfunction': 'function',
            'endwhile': 'while',
            'endfor': ['for', 'foreach'],
            'endif': 'if',
            'endsub': 'sub',
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
        elif lowercase_token_value in self.closing_statements_table:
            if len(self.statements_stack) == 0 or self._statement_matches(lowercase_token_value):
                raise ValueError

    def _statement_matches(self, lowercase_token_value):
        last_statement = self.statements_stack.pop()
        expected_statement = self.closing_statements_table[lowercase_token_value]
        has_expected = False
        if expected_statement is list:
            for expected in expected_statement:
                if last_statement == expected:
                    has_expected = True
        else:
            if last_statement == expected_statement:
                has_expected = True
        return has_expected