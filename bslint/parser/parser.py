from bslint.parser import statement_reduction_rules as statement_grammar
from bslint.parser import program_reduction_rules as program_grammar
from bslint.messages import error_constants as err_const
from bslint import constants as const
from bslint.lexer.lexer import Lexer
from bslint.messages import handler as err
import bslint.utilities.custom_exceptions as custom_exception

MAX_FINAL_STATEMENT_LENGTH = 1
STATEMENT_PAIRS = {
    const.OPEN_CURLY_BRACKET: const.CLOSE_CURLY_BRACKET,
    const.OPEN_PARENTHESIS: const.CLOSE_PARENTHESIS,
    const.OPEN_SQUARE_BRACKET: const.CLOSE_SQUARE_BRACKET
}


class Parser(Lexer):
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        Lexer.__init__(self)
        self.all_statements = []
        self.current_tokens = None
        self.program = []
        self.line_reductions = []
        self.current_output_list = self.all_statements
        self.current_grammar = statement_grammar
        self.number_of_priorities = None
        self.current_priority_level = 0
        self.opening_stmt_indexes = [0]
        self.token_index = 0
        self.current_statement = []
        self.closing_stmt_index = 0
        self.current_index = 0
        self.is_valid_stmt = False
        self.program_grammar_applied = False
        self.stmt_grammar_applied = False

    def parse(self, characters):
        self.set_number_of_priorities_level()
        try:
            lexing_result = Lexer.lex(self, characters)
            if lexing_result[const.STATUS] == const.SUCCESS:
                try:
                    self.check_statement_validity(self.tokens[self.current_token_index:])
                except custom_exception.ParsingException:
                    self.program.extend(self.current_statement)
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
            self.program.append(self.current_tokens[0])

    @staticmethod
    def _get_token_types(tokens):
        return [token.parser_type for token in tokens]

    def handle_statement(self):
        self.token_index = 0
        while self.token_index < len(self.current_tokens):
            self.token_is_opening_stmt()
            self.token_index += 1
        self.iterate_over_inner_statement()

    def token_is_opening_stmt(self):
        opening_stmt = STATEMENT_PAIRS.keys()
        if self.current_tokens[self.token_index] in opening_stmt:
            current_token = self.current_tokens[self.token_index]
            try:
                self.stmt_longer_than_two_tokens(current_token)
            except IndexError:
                raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)
        elif self.current_tokens[self.token_index] in STATEMENT_PAIRS.values():
            self.closing_stmt_index = self.token_index
            self.iterate_over_inner_statement()

    def stmt_longer_than_two_tokens(self, current_token):
        if self.current_tokens[self.token_index + 1] != STATEMENT_PAIRS[current_token]:
            if self.current_tokens[self.token_index + 2] != STATEMENT_PAIRS[current_token]:
                self.opening_stmt_indexes.append(self.token_index + 1)
            else:
                self.token_index += 2
        else:
            self.token_index += 1

    def iterate_over_inner_statement(self):
        self.current_index = self.get_index()
        if self.current_index == 0:
            self.closing_stmt_index = len(self.current_tokens)
        self.current_statement = self.current_tokens[self.current_index:self.closing_stmt_index]
        self.iterate_over_stmt()
        self.token_index -= len(self.current_tokens[self.current_index + 1:self.closing_stmt_index])
        self.current_tokens[self.current_index] = self.current_statement[0]
        del self.current_tokens[self.current_index + 1:self.closing_stmt_index]

    def iterate_over_stmt(self):
        self.program_grammar_applied = False
        self.stmt_grammar_applied = False
        self.is_valid_stmt = False
        try:
            while self.is_valid_stmt is False:
                self.current_priority_level = 0
                while self.current_priority_level < self.number_of_priorities:
                    self.reduce_and_handle_error()
                    self.current_priority_level += 1
                    if len(self.current_statement) == MAX_FINAL_STATEMENT_LENGTH:
                        break
                if self.no_math_in_last_two_reductions():
                    self.switch_grammar()
                elif not self.is_valid_stmt:
                    raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)
        except custom_exception.ParsingException:
            raise

    def no_math_in_last_two_reductions(self):
        return not self.is_valid_stmt and (self.program_grammar_applied is True or self.stmt_grammar_applied is True)

    def switch_grammar(self):
        if self.current_grammar.GRAMMAR_NAME == const.STATEMENT_GRAMMAR:
            self.current_grammar = program_grammar
            self.stmt_grammar_applied = False
        else:
            self.current_grammar = statement_grammar
            self.program_grammar_applied = False
        self.set_number_of_priorities_level()

    def reduce_and_handle_error(self):
        self.is_valid_stmt = False
        index = 0
        while index < len(self.current_statement):
            possible_production_rules = self._get_possible_production_rules(self.current_statement[-(index + 1)])
            matching_production = self._find_matching_production(index, possible_production_rules)
            if matching_production is not None:
                self._replace_current_tokens(index, matching_production)
                self.current_priority_level = 0
                self.set_valid_stmt_type()
                if len(self.current_statement) == MAX_FINAL_STATEMENT_LENGTH:
                    self.is_valid_stmt = True
                else:
                    self.reduce_and_handle_error()
            index += 1
        if not self.is_valid_stmt and self.current_priority_level == (self.number_of_priorities - 1) \
                and (self.program_grammar_applied is False and self.stmt_grammar_applied is False):
            raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)

    def set_valid_stmt_type(self):
        self.stmt_grammar_applied = self.current_grammar == statement_grammar
        self.program_grammar_applied = not self.stmt_grammar_applied

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
        self.current_statement[len(self.current_statement) - index:len(self.current_statement) - index] = [rule.result]
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
        if len(self.current_statement) == 1 and self.current_statement[0] is const.BLOCK_STMT:
            return
        self.current_grammar = program_grammar
        self.set_number_of_priorities_level()
        self.current_priority_level = 0
        try:
            self.reduce_program()
        except custom_exception.ParsingException:
            raise custom_exception.ParsingException(err_const.PROGRAM_PARSING_FAILED)

    def reduce_program(self):
        self.is_valid_stmt = False
        index = 0
        while index < len(self.current_statement):
            possible_production_rules = self._get_possible_production_rules(self.current_statement[-(index + 1)])
            matching_production = self._find_matching_production(index, possible_production_rules)
            if matching_production is not None:
                self._replace_current_tokens(index, matching_production)
                self.current_priority_level = 0
                if len(self.current_statement) == MAX_FINAL_STATEMENT_LENGTH:
                    self.is_valid_stmt = True
                else:
                    self.reduce_program()
                self.is_valid_stmt = True
            index += 1
        if not self.is_valid_stmt and self.current_priority_level == (self.number_of_priorities - 1):
            raise custom_exception.ParsingException(err_const.STMT_PARSING_FAILED)

    def set_check_program_values(self):
        self.token_index = 0
        del self.opening_stmt_indexes[:]
        self.opening_stmt_indexes.append(0)
        self.current_statement = self.program
        self.current_output_list = self.line_reductions

    def handle_parsing_error(self, err_code):
        self.errors.append(err.get_error_msg(err_code, [self.handle_style.line_number - 1]))
