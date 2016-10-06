from bslint.tokenizer import Tokenizer
import bslint.parser.reduction_rules as grammar
import bslint.error_messages_builder.error_builder.error_messages_constants as err_const


class Parser(Tokenizer):

    def __init__(self):
        Tokenizer.__init__(self)
        self.expected_statement = None
        self.statement = None
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

    def check_statement_validity(self, statement):
        self.statement = statement
        return self.reduce_statement()

    @staticmethod
    def find_production_with_corresponding_last_token(current_token):
        corresponding_rules = []
        for rule in grammar.rules:
            if rule.rule[len(rule.rule) - 1] == current_token:
                corresponding_rules.append(rule)
        return corresponding_rules

    @staticmethod
    def get_last_token_types(last_tokens):
        return [token.parser_type for token in last_tokens]

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

    def reduce_statement(self):
        possible_production_rules = self.find_production_with_corresponding_last_token(self.statement[-1].parser_type)
        is_valid_statement = False
        for rule in possible_production_rules:
            last_tokens = self.statement[:len(rule.rule)]
            last_token_types = self.get_last_token_types(last_tokens)
            if rule.rule == last_token_types:
                del self.statement[:len(rule.rule)]
                self.statement.insert(len(self.statement), rule.result)
                is_valid_statement = True
                break
        if is_valid_statement is False:
            raise ValueError(err_const.PARSING_FAILED)
