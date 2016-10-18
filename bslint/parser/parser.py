import bslint.parser.statement_reduction_rules as statement_grammar
import bslint.parser.program_reduction_rules as program_grammar
import bslint.error_messages.constants as err_const
from bslint.lexer.lexer import Lexer

MAX_FINAL_STATEMENT_LENGTH = 1


class Parser(Lexer):

    def __init__(self):
        Lexer.__init__(self)
        self.expected_statement = None
        self.all_statements = []
        self.current_tokens = None
        self.program = []
        self.line_reductions = []
        self.current_output_list = self.all_statements
        self.current_grammar = statement_grammar

    def parse(self, characters):
        return Lexer.lex(self, characters)

    def check_statement_validity(self, statement):
        self.current_tokens = self._get_token_types(statement)
        self._reduce_and_handle_error()
        self.program.append(self.current_tokens[0])

    @staticmethod
    def _get_token_types(tokens):
        return [token.parser_type for token in tokens]

    def _reduce_and_handle_error(self):
        is_valid_statement = False
        for index, token in enumerate(self.current_tokens):
            possible_production_rules = self._get_possible_production_rules(self.current_tokens[-(index + 1)])
            matching_production = self._find_matching_production(index, possible_production_rules)
            if matching_production is not None:
                self._replace_current_tokens(index, matching_production)
                if len(self.current_tokens) > MAX_FINAL_STATEMENT_LENGTH:
                    self._reduce_and_handle_error()
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
            del self.current_tokens[-tokens_from_end:]
        else:
            del self.current_tokens[-tokens_from_end: -index]
        self.current_tokens[len(self.current_tokens) - index:len(self.current_tokens) - index] = rule.result
        self.current_output_list.append(self.current_tokens[:])

    def _get_current_tokens(self, index, tokens_from_end):
        if index == 0:
            current_tokens = self.current_tokens[-tokens_from_end:]
        else:
            current_tokens = self.current_tokens[-tokens_from_end: -index]
        return current_tokens

    @staticmethod
    def _get_number_of_tokens_from_end(production, index):
        return len(production.rule) + index

    def _get_possible_production_rules(self, current_token):
        corresponding_rules = []
        for rule in self.current_grammar.rules:
            if rule.rule[len(rule.rule) - 1] == current_token:
                corresponding_rules.append(rule)
        return corresponding_rules

    def check_program_validity(self):
        self.current_grammar = program_grammar
        self.current_tokens = self.program
        self.current_output_list = self.line_reductions
        if len(self.current_tokens) > 1:
            self._reduce_and_handle_error()

