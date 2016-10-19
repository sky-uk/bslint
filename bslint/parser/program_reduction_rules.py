import bslint.constants as const
from bslint.parser.reduction_rule_handler import ReductionRuleHandler

rules_list = [

    # region Block Statement reduction rules

    # region Print block statement

    ([const.PRINT_STATEMENT, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ([const.PRINT_STATEMENT, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ([const.PRINT_STATEMENT, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ([const.PRINT_STATEMENT, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion

    # region Variable assignment block statement

    ([const.VAR_AS, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ([const.VAR_AS, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ([const.VAR_AS, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ([const.VAR_AS, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion

    # region Function call block statement

    ([const.FUNCTION_CALL, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ([const.FUNCTION_CALL, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ([const.FUNCTION_CALL, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ([const.FUNCTION_CALL, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion

    # region Block statement block statement

    ([const.BLOCK_STATEMENT, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ([const.BLOCK_STATEMENT, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ([const.BLOCK_STATEMENT, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ([const.BLOCK_STATEMENT, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion
    # endregion
]

rules = []
for rule in rules_list:
    rules.append(ReductionRuleHandler(rule[0], rule[1]))
