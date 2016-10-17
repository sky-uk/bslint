import bslint.error_messages.constants as err_const
import bslint.parser.reduction_rules as grammar
from bslint.lexer.lexer import Lexer

MAX_FINAL_STATEMENT_LENGTH = 1


class Parser(Lexer):

    def __init__(self):
        Lexer.__init__(self)
        self.expected_statement = None
        self.all_statements = []
        self.statement = None

    def parse(self, characters):
        return Lexer.lex(self, characters)

    def check_statement_validity(self, statement):
        self.statements_counter += 1
        self.statement = self._get_token_types(statement)
        self._reduce_statement_and_handle_error()

    @staticmethod
    def _get_possible_production_rules(current_token):
        corresponding_rules = []
        for rule in grammar.rules:
            if rule.rule[len(rule.rule) - 1] == current_token:
                corresponding_rules.append(rule)
        return corresponding_rules

    @staticmethod
    def _get_token_types(tokens):
        return [token.parser_type for token in tokens]

    def _reduce_statement_and_handle_error(self):
        is_valid_statement = False
        for index, token in enumerate(self.statement):
            possible_production_rules = self._get_possible_production_rules(self.statement[-(index + 1)])
            matching_production = self._find_matching_production(index, possible_production_rules)
            if matching_production is not None:
                self._replace_current_tokens(index, matching_production)
                if len(self.statement) > MAX_FINAL_STATEMENT_LENGTH:
                    self._reduce_statement_and_handle_error()
                is_valid_statement = True
        if is_valid_statement is False:
            raise ValueError(err_const.PARSING_FAILED)

    def _find_matching_production(self, index, possible_production_rules):
        matching_production = None
        for production in possible_production_rules:
            number_of_tokens_from_end = self._get_number_of_tokens_from_end(production, index)
            current_tokens = self._get_current_tokens(index, number_of_tokens_from_end)
            if production.rule == current_tokens:
                matching_production = production
                break
        return matching_production

    def _replace_current_tokens(self, index, rule):
        tokens_from_end = self._get_number_of_tokens_from_end(rule, index)
        if index == 0:
            del self.statement[-tokens_from_end:]
        else:
            del self.statement[-tokens_from_end: -index]
        self.statement[len(self.statement) - index:len(self.statement) - index] = rule.result
        self.all_statements.append(self.statement[:])

    def _get_current_tokens(self, index, tokens_from_end):
        if index == 0:
            current_tokens = self.statement[-tokens_from_end:]
        else:
            current_tokens = self.statement[-tokens_from_end: -index]
        return current_tokens

    @staticmethod
    def _get_number_of_tokens_from_end(production, index):
        return len(production.rule) + index
