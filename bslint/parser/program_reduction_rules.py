import bslint.constants as const
from bslint.parser.reduction_rule_handler import ReductionRuleHandler

rules = [

    # region Block Statement reduction rules

    # region Print block statement

    ReductionRuleHandler([const.PRINT_STATEMENT, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.PRINT_STATEMENT, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.PRINT_STATEMENT, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.PRINT_STATEMENT, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion

    # region Variable assignment block statement

    ReductionRuleHandler([const.VAR_AS, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.VAR_AS, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.VAR_AS, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.VAR_AS, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion

    # region Function call block statement

    ReductionRuleHandler([const.FUNCTION_CALL, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion

    # region Block statement block statement

    ReductionRuleHandler([const.BLOCK_STATEMENT, const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.BLOCK_STATEMENT, const.VAR_AS], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.BLOCK_STATEMENT, const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ReductionRuleHandler([const.BLOCK_STATEMENT, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

    # endregion
    # endregion
]
