import bslint.constants as const
from bslint.parser.reduction_rule_handler import ReductionRuleHandler

rules = [

    # region Value

    # region Values with Operator
    ReductionRuleHandler([const.ID, const.OPERATOR, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.OPERATOR, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.OPERATOR, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.OPERATOR, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.OPERATOR, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.OPERATOR, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], [const.VALUE]),
    # endregion

    # region Values with Plus
    ReductionRuleHandler([const.ID, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.PLUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.PLUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    # endregion

    # region Values with Minus
    ReductionRuleHandler([const.ID, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.ID, const.MINUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.ID], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.VALUE, const.MINUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.VALUE], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    # endregion

    # endregion

    # region Argument, Close Parenthesis
    ReductionRuleHandler([const.ARGUMENT, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ReductionRuleHandler([const.ID, const.COMMA, const.ID, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ReductionRuleHandler([const.ID, const.COMMA, const.VALUE, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ReductionRuleHandler([const.ID, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.ID, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.VALUE, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    # endregion

    # region Function Declaration
    ReductionRuleHandler([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ReductionRuleHandler([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    # endregion

    # region Function Call
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], [const.FUNCTION_CALL]),
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS], [const.FUNCTION_CALL]),
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    ReductionRuleHandler([const.ID, const.OPEN_PARENTHESIS, const.FUNCTION_CALL, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    # endregion

    # region Value/ID/Variable Assignment in Brackets
    ReductionRuleHandler([const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS], [const.VALUE]),
    ReductionRuleHandler([const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS], [const.ID]),
    ReductionRuleHandler([const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS], [const.VAR_AS]),
    # endregion

    # region Variable Assignment
    ReductionRuleHandler([const.ID, const.EQUALS, const.ID], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL], [const.VAR_AS]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.MINUS, const.VALUE], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.PLUS, const.VALUE], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.MINUS, const.ID], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.PLUS, const.ID], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.MINUS, const.FUNCTION_CALL], [const.VAR_AS]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.PLUS, const.FUNCTION_CALL], [const.VAR_AS]),
    # endregion

    # region Parameter
    ReductionRuleHandler([const.PARAM, const.COMMA, const.PARAM], [const.PARAM]),
    ReductionRuleHandler([const.ID, const.AS, const.TYPE], [const.PARAM]),
    ReductionRuleHandler([const.VAR_AS, const.AS, const.TYPE], [const.PARAM]),
    # endregion

    # region For Statements

    # region For Statement to Value
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE], [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.VALUE],
                         [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.ID],
                         [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL],
                         [const.FOR_STATEMENT]),
    # endregion

    # region For Statement to ID
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID], [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.VALUE],
                         [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.ID],
                         [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.FUNCTION_CALL],
                         [const.FOR_STATEMENT]),
    # endregion

    # region For Statement to Function Call
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL], [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE],
                         [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.ID],
                         [const.FOR_STATEMENT]),
    ReductionRuleHandler([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.FUNCTION_CALL],
                         [const.FOR_STATEMENT]),
    # endregion
    # endregion

    # region While Statements
    ReductionRuleHandler([const.WHILE, const.VAR_AS], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.ID], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.VALUE], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.FUNCTION_CALL], [const.WHILE_STATEMENT]),

    ReductionRuleHandler([const.WHILE, const.PLUS, const.ID], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.PLUS, const.VALUE], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.PLUS, const.FUNCTION_CALL], [const.WHILE_STATEMENT]),

    ReductionRuleHandler([const.WHILE, const.MINUS, const.ID], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.MINUS, const.VALUE], [const.WHILE_STATEMENT]),
    ReductionRuleHandler([const.WHILE, const.MINUS, const.FUNCTION_CALL], [const.WHILE_STATEMENT]),
    # endregion

    # region Closing Statements
    ReductionRuleHandler([const.END_FOR_TOKEN], [const.END_FOR]),
    ReductionRuleHandler([const.END_IF_TOKEN], [const.END_IF]),
    ReductionRuleHandler([const.END_WHILE_TOKEN], [const.END_WHILE]),
    ReductionRuleHandler([const.END_SUB_TOKEN], [const.END_SUB]),
    ReductionRuleHandler([const.END_FUNCTION_TOKEN], [const.END_FUNCTION]),
    ReductionRuleHandler([const.END_TOKEN], [const.END]),
    # endregion

    # region Print Statements

    # region Simple Print
    ReductionRuleHandler([const.PRINT_KEYWORD, const.VALUE], [const.PRINT_STATEMENT]),
    ReductionRuleHandler([const.PRINT_KEYWORD, const.ID], [const.PRINT_STATEMENT]),
    ReductionRuleHandler([const.PRINT_KEYWORD, const.FUNCTION_CALL], [const.PRINT_STATEMENT]),
    ReductionRuleHandler([const.PRINT_KEYWORD, const.VAR_AS], [const.PRINT_STATEMENT]),
    ReductionRuleHandler([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], [const.PRINT_STATEMENT]),
    # endregion

    # region Comma Print Arguments

    # region Variable Assignment Print Arguments
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.VALUE],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.VAR_AS],
                         [const.PRINT_ARGUMENT]),
    # endregion

    # region Simple Print Arguments
    ReductionRuleHandler([const.ID, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.VALUE, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.FUNCTION_CALL, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    # endregion

    # region Compound Print Arguments
    ReductionRuleHandler([const.ID, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    # endregion

    # endregion

    # region Semi-Colon Print Arguments

    # region Variable Assignment Print Arguments
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.ID],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS],
                         [const.PRINT_ARGUMENT]),
    # endregion

    # region Simple Print Arguments
    ReductionRuleHandler([const.ID, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.SEMI_COLON, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.ID, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.VALUE, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),

    ReductionRuleHandler([const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    # endregion

    # region Compound Print Arguments
    ReductionRuleHandler([const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ReductionRuleHandler([const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    # endregion

    # endregion

    # endregion

    # For Each n In aa
    # region For Each
    ReductionRuleHandler([const.FOR_EACH, const.ID, const.IN, const.ID], [const.FOR_EACH_STATEMENT]),
    ReductionRuleHandler([const.FOR_EACH, const.ID, const.IN, const.VALUE], [const.FOR_EACH_STATEMENT]),
    ReductionRuleHandler([const.FOR_EACH, const.ID, const.IN, const.FUNCTION_CALL], [const.FOR_EACH_STATEMENT]),
    # endregion

]
