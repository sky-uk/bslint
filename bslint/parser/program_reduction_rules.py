import collections
import bslint.constants as const

RULE = collections.namedtuple('Rule', ['rule', 'result'])
RULES_LIST = [

    # region Block Statement reduction RULES

    # region Variable assignment block statement

    ([const.PRINT_STATEMENT], [const.BLOCK_STATEMENT]),
    ([const.FUNCTION_CALL], [const.BLOCK_STATEMENT]),
    ([const.VAR_AS], [const.BLOCK_STATEMENT]),
    ([const.BLOCK_STATEMENT, const.BLOCK_STATEMENT], [const.BLOCK_STATEMENT]),

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

    ([const.WHILE_STATEMENT, const.BLOCK_STATEMENT, const.END_WHILE], [const.BLOCK_STATEMENT]),
    ([const.WHILE_STATEMENT, const.END_WHILE], [const.BLOCK_STATEMENT]),
    ([const.FOR_STATEMENT, const.BLOCK_STATEMENT, const.END_FOR], [const.BLOCK_STATEMENT]),
    ([const.FOR_STATEMENT, const.END_FOR], [const.BLOCK_STATEMENT]),
    ([const.FOR_EACH_STATEMENT, const.BLOCK_STATEMENT, const.END_FOR], [const.BLOCK_STATEMENT]),
    ([const.FOR_EACH_STATEMENT, const.END_FOR], [const.BLOCK_STATEMENT]),
    ([const.FUNCTION_DECLARATION, const.BLOCK_STATEMENT, const.END_FUNCTION], [const.BLOCK_STATEMENT]),
    ([const.FUNCTION_DECLARATION, const.END_FUNCTION], [const.BLOCK_STATEMENT]),

    # region IF statement
    ([const.IF_STATEMENT, const.BLOCK_STATEMENT, const.END_IF], [const.BLOCK_STATEMENT]),
    ([const.IF_STATEMENT, const.BLOCK_STATEMENT], [const.IF_BLOCK]),
    ([const.ELSE_IF_STATEMENT, const.BLOCK_STATEMENT], [const.ELSE_IF_BLOCK]),
    ([const.ELSE_STATEMENT, const.BLOCK_STATEMENT, const.END_IF], [const.END_IF]),
    ([const.ELSE_IF_BLOCK, const.ELSE_IF_BLOCK], [const.ELSE_IF_BLOCK]),
    ([const.IF_BLOCK, const.ELSE_IF_BLOCK, const.END_IF], [const.BLOCK_STATEMENT])
    # endregion

]

RULES = []
for rule in RULES_LIST:
    RULES.append(RULE(rule[0], rule[1]))
