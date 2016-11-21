from bslint.parser import statement_reduction_rules as statement_grammar
from bslint.parser import program_reduction_rules as program_grammar
from bslint.messages import error_constants as err_const
from bslint import constants as const
from bslint.lexer.lexer import Lexer
from bslint.messages import handler as err
import bslint.utilities.custom_exceptions as custom_exception

MAX_FINAL_STATEMENT_LENGTH = 1
CLOSING_STMT = [const.CLOSE_CURLY_BRACKET, const.CLOSE_PARENTHESIS, const.CLOSE_SQUARE_BRACKET]
OPENING_STMT = [const.OPEN_CURLY_BRACKET, const.OPEN_PARENTHESIS, const.OPEN_SQUARE_BRACKET]


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
        self.statement_already_recalled = False
        self.program_already_recalled = False
        self.opening_stmt_indexes = [0]
        self.token_index = 0
        self.current_statement = []
        self.closing_stmt_index = 0
        self.current_index = 0

    def parse(self, characters):
        self.set_number_of_priorities_level()
        try:
            lexing_result = Lexer.lex(self, characters)
            if lexing_result[const.STATUS] == const.SUCCESS:
                self.check_statement_validity(self.tokens[self.current_token_index:])
                self.set_check_program_values()
                self.check_program_validity()
        except custom_exception.ParsingException as exception:
            self.handle_parsing_error(exception.args[0])
        return self.build_return_message()

    def set_number_of_priorities_level(self):
        self.number_of_priorities = len(self.current_grammar.RULES.keys())

    def check_statement_validity(self, statement):
        self.current_tokens = self._get_token_types(statement)
        if len(self.current_tokens) > 0:
            self.handle_statement()
            self.iterate_over_statement()
            self.program.append(self.current_tokens[0])

    @staticmethod
    def _get_token_types(tokens):
        return [token.parser_type for token in tokens]

    def handle_statement(self):
        self.token_index = 0
        while self.token_index < len(self.current_tokens):
            try:
                self.token_is_opening_stmt()
                self.token_index += 1
            except custom_exception.ParsingException:
                self.handle_failed_stmt_reduction()
        try:
            self.iterate_over_inner_statement()
        except custom_exception.ParsingException:
            self.handle_failed_stmt_reduction()

    def token_is_opening_stmt(self):
        if self.current_tokens[self.token_index] in OPENING_STMT:
            try:
                if self.current_tokens[self.token_index + 1] not in CLOSING_STMT:
                    self.opening_stmt_indexes.append(self.token_index + 1)
                else:
                    self.token_index += 1
            except IndexError:
                raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)
        elif self.current_tokens[self.token_index] in CLOSING_STMT:
            self.closing_stmt_index = self.token_index
            self.iterate_over_inner_statement()

    def iterate_over_inner_statement(self):
        self.current_index = self.get_index()
        if self.current_index == 0:
            self.closing_stmt_index = len(self.current_tokens)
        self.current_statement = self.current_tokens[self.current_index:self.closing_stmt_index]
        self.iterate_over_statement()
        self.token_index -= len(self.current_tokens[self.current_index + 1:self.closing_stmt_index])
        self.current_tokens[self.current_index] = self.current_statement[0]
        del self.current_tokens[self.current_index + 1:self.closing_stmt_index]

    def handle_failed_stmt_reduction(self):
        if self.statement_already_recalled:
            raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)
        self.current_grammar = program_grammar
        self.set_number_of_priorities_level()
        try:
            self.iterate_over_statement()
        except custom_exception.ParsingException:
            self.statement_already_recalled = True
            self.current_grammar = statement_grammar
            self.set_number_of_priorities_level()
            self.current_tokens[self.current_index:self.closing_stmt_index] = self.current_statement
            self.token_index -= len(self.current_tokens[self.current_index + 1:self.closing_stmt_index])

    def iterate_over_statement(self):
        self.current_priority_level = 0
        while self.current_priority_level < self.number_of_priorities:
            self.reduce_and_handle_error()
            self.current_priority_level += 1
            if len(self.current_statement) == MAX_FINAL_STATEMENT_LENGTH:
                break

    def reduce_and_handle_error(self):
        is_valid_statement = False
        index = 0
        while index < len(self.current_statement):
            possible_production_rules = self._get_possible_production_rules(
                self.current_statement[-(index + 1)])
            matching_production = self._find_matching_production(index, possible_production_rules)
            if matching_production is not None:
                self._replace_current_tokens(index, matching_production)
                self.current_priority_level = 0
                if len(self.current_statement) > MAX_FINAL_STATEMENT_LENGTH:
                    self.reduce_and_handle_error()
                is_valid_statement = True
            index += 1
        if not is_valid_statement and self.current_priority_level == (self.number_of_priorities - 1):
            raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)

    def get_index(self):
        try:
            return self.opening_stmt_indexes.pop()
        except IndexError:
            return 0

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
            del self.current_statement[-tokens_from_end:]
        else:
            del self.current_statement[-tokens_from_end: -index]
        self.current_statement[
            len(self.current_statement) - index:len(self.current_statement) - index] = [rule.result]
        self.current_output_list.append(self.current_statement[:])

    def _get_current_tokens(self, index, tokens_from_end):
        if index == 0:
            current_tokens = self.current_statement[-tokens_from_end:]
        else:
            current_tokens = self.current_statement[-tokens_from_end: -index]
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
        self.set_number_of_priorities_level()
        try:
            self.iterate_over_statement()
        except custom_exception.ParsingException:
            raise custom_exception.ParsingException(err_const.PROGRAM_PARSING_FAILED)

    def set_check_program_values(self):
        self.token_index = 0
        del self.opening_stmt_indexes[:]
        self.opening_stmt_indexes.append(0)
        self.current_statement = self.program
        self.current_output_list = self.line_reductions

    def handle_parsing_error(self, err_code):
        self.errors.append(err.get_error_msg(err_code, [self.handle_style.line_number - 1]))
