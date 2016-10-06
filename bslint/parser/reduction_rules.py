import bslint.constants as const
from bslint.parser.reduction_rule_handler import ReductionRuleHandler

rules = [
    ReductionRuleHandler([const.ID, const.OPERATOR, const.ID], const.VALUE),
    ReductionRuleHandler([const.VALUE, const.OPERATOR, const.VALUE], const.VALUE),
    ReductionRuleHandler([const.VALUE, const.OPERATOR, const.ID], const.VALUE),
    ReductionRuleHandler([const.ID, const.OPERATOR, const.VALUE], const.VALUE),
    ReductionRuleHandler([const.ID, const.OPERATOR, const.FUNCTION_CALL], const.VALUE),
    ReductionRuleHandler([const.FUNCTION_CALL, const.OPERATOR, const.ID], const.VALUE),
    ReductionRuleHandler([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], const.VALUE),
    ReductionRuleHandler([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], const.VALUE),
    ReductionRuleHandler([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], const.VALUE),

    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS], const.FUNCTION_CALL),

    ReductionRuleHandler([const.ARGUMENT, const.COMMA, const.ARGUMENT], const.ARGUMENT),
    ReductionRuleHandler([const.ID], const.ARGUMENT),
    ReductionRuleHandler([const.VALUE], const.ARGUMENT),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID], const.VAR_AS),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE], const.VAR_AS),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL], const.VAR_AS),

    ReductionRuleHandler([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         const.FUNCTION_DECLARATION),
    ReductionRuleHandler([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         const.FUNCTION_DECLARATION),
    ReductionRuleHandler([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         const.FUNCTION_DECLARATION),
    ReductionRuleHandler([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         const.FUNCTION_DECLARATION),

    ReductionRuleHandler([const.PARAM, const.COMMA, const.PARAM], const.PARAM),
    ReductionRuleHandler([const.ID, const.AS, const.TYPE], const.PARAM),
    ReductionRuleHandler([const.ID], const.PARAM),
    ReductionRuleHandler([const.VAR_AS], const.PARAM),
    ReductionRuleHandler([const.VAR_AS, const.AS, const.TYPE], const.PARAM),

    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE], const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.VALUE],
                         const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.ID],
                         const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL],
                         const.FOR_STATEMENT),

    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID], const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.VALUE],
                         const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.ID],
                         const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.FUNCTION_CALL],
                         const.FOR_STATEMENT),

    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL], const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE],
                         const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.ID],
                         const.FOR_STATEMENT),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.FUNCTION_CALL],
                         const.FOR_STATEMENT),
]
