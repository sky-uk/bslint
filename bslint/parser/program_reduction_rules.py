import bslint.constants as const
import bslint.parser.rule_builder as rule_builder

RULES_LIST = {
    const.PRIORITY_ZERO: {
        const.BLOCK_STMT: [
            ([const.BLOCK_STMT, const.BLOCK_STMT], const.BLOCK_STMT),
            ([const.IF_STMT, const.BLOCK_STMT], const.IF_BLOCK),
            ([const.ELSE_IF_STMT, const.BLOCK_STMT], const.ELSE_IF_BLOCK)
        ],
        # region Block Statement reduction RULES
        const.EXIT_STMT: [([const.EXIT_STMT], const.BLOCK_STMT)],
        const.PRINT_STMT: [([const.PRINT_STMT], const.BLOCK_STMT)],
        const.FUNCTION_CALL: [([const.FUNCTION_CALL], const.BLOCK_STMT)],
        const.VAR_AS: [([const.VAR_AS], const.BLOCK_STMT)],
        const.RETURN_STMT: [([const.RETURN_STMT], const.BLOCK_STMT)],
        # endregion

        const.END_WHILE: [
            ([const.WHILE_STMT, const.BLOCK_STMT, const.END_WHILE], const.BLOCK_STMT),
            ([const.WHILE_STMT, const.END_WHILE], const.BLOCK_STMT)
        ],
        const.END_FOR: [
            ([const.FOR_STMT, const.BLOCK_STMT, const.END_FOR], const.BLOCK_STMT),
            ([const.FOR_STMT, const.END_FOR], const.BLOCK_STMT),
            ([const.FOR_EACH_STMT, const.BLOCK_STMT, const.END_FOR], const.BLOCK_STMT),
            ([const.FOR_EACH_STMT, const.END_FOR], const.BLOCK_STMT),
        ],

        const.END_FUNCTION: [
            ([const.FUNCTION_DECLARATION, const.BLOCK_STMT, const.END_FUNCTION], const.BLOCK_STMT),
            ([const.FUNCTION_DECLARATION, const.END_FUNCTION], const.BLOCK_STMT)
        ],

        # region IF statement
        const.END_IF: [
            ([const.IF_STMT, const.BLOCK_STMT, const.END_IF], const.BLOCK_STMT),
            ([const.ELSE_STMT, const.BLOCK_STMT, const.END_IF], const.END_IF),
            ([const.IF_BLOCK, const.ELSE_IF_BLOCK, const.END_IF], const.BLOCK_STMT)
        ],
        const.ELSE_IF_BLOCK: [([const.ELSE_IF_BLOCK, const.ELSE_IF_BLOCK], const.ELSE_IF_BLOCK)],
        # endregion
    }
}

RULES = rule_builder.load_grammar_rules(RULES_LIST)
