from bslint.parser import statement_reduction_rules as statement_grammar
from bslint.parser import program_reduction_rules as program_grammar
from bslint.error_messages import constants as err_const
from bslint import constants as const
from bslint.lexer.lexer import Lexer
from bslint.error_messages import handler as err

MAX_FINAL_STATEMENT_LENGTH = 1
INVALID_STATEMENT = [const.CONDITION]


class Parser(Lexer):
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        Lexer.__init__(self)
        self.expected_statement = None
        self.all_statements = []
        self.current_tokens = None
        self.program = []
        self.line_reductions = []
        self.current_output_list = self.all_statements
        self.current_grammar = statement_grammar
        self.number_of_priorities = None
        self.current_priority_level = 0

    def parse(self, characters):
        self.set_number_of_priorities_level()
        return Lexer.lex(self, characters)

    def set_number_of_priorities_level(self):
        self.number_of_priorities = len(self.current_grammar.RULES.keys())

    def check_statement_validity(self, statement):
        self.current_tokens = self._get_token_types(statement)
        if len(self.current_tokens) > 0:
            self.iterate_over_statement()
            if self.current_tokens[0] in INVALID_STATEMENT:
                raise ValueError(err_const.STMT_PARSING_FAILED)
            else:
                self.program.append(self.current_tokens[0])

    @staticmethod
    def _get_token_types(tokens):
        return [token.parser_type for token in tokens]

    def iterate_over_statement(self):
        self.current_priority_level = 0
        while self.current_priority_level < self.number_of_priorities:
            self.reduce_and_handle_error()
            self.current_priority_level += 1
            if len(self.current_tokens) == MAX_FINAL_STATEMENT_LENGTH:
                break

    def reduce_and_handle_error(self):
        is_valid_statement = False
        index = 0
        while index < len(self.current_tokens):
            possible_production_rules = self._get_possible_production_rules(
                self.current_tokens[-(index + 1)])
            matching_production = self._find_matching_production(index, possible_production_rules)
            if matching_production is not None:
                self._replace_current_tokens(index, matching_production)
                self.current_priority_level = 0
                if len(self.current_tokens) > MAX_FINAL_STATEMENT_LENGTH:
                    self.reduce_and_handle_error()
                is_valid_statement = True
            index += 1
        if is_valid_statement is False and self.current_priority_level == self.number_of_priorities - 1:
            raise ValueError(err_const.STMT_PARSING_FAILED)

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
        self.current_tokens[
            len(self.current_tokens) - index:len(self.current_tokens) - index] = [rule.result]
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
        if current_token not in self.current_grammar.RULES[self.current_priority_level]:
            return []
        else:
            return self.current_grammar.RULES[self.current_priority_level][current_token]

    def check_program_validity(self):
        self.current_grammar = program_grammar
        self.current_tokens = self.program
        self.current_output_list = self.line_reductions
        self.set_number_of_priorities_level()
        try:
            self.iterate_over_statement()
        except ValueError:
            raise ValueError(err_const.PROGRAM_PARSING_FAILED)

    def handle_parsing_error(self, err_code):
        self.errors.append(err.get_message(err_code, [self.handle_style.line_number]))
