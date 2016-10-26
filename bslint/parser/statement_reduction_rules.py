import bslint.constants as const
from bslint.parser.reduction_rule_handler import ReductionRuleHandler

rules_list = [

    # region Value

    # region Values with Operator
    ([const.ID, const.OPERATOR, const.ID], [const.VALUE]),
    ([const.VALUE, const.OPERATOR, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.OPERATOR, const.ID], [const.VALUE]),
    ([const.ID, const.OPERATOR, const.VALUE], [const.VALUE]),
    ([const.ID, const.OPERATOR, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.OPERATOR, const.ID], [const.VALUE]),
    ([const.VALUE, const.OPERATOR, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.OPERATOR, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.OPERATOR, const.FUNCTION_CALL], [const.VALUE]),
    # endregion

    # region Values with Plus
    ([const.ID, const.PLUS, const.ID], [const.VALUE]),
    ([const.ID, const.PLUS, const.PLUS, const.ID], [const.VALUE]),
    ([const.ID, const.PLUS, const.MINUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.PLUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.MINUS, const.ID], [const.VALUE]),
    ([const.ID, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.ID, const.PLUS, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.ID, const.PLUS, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.ID, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.ID, const.PLUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.ID, const.PLUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.ID], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.ID], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.VALUE, const.PLUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.PLUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.DOT, const.ID], [const.VALUE]),
    # endregion

    # region Values with Minus
    ([const.ID, const.MINUS, const.ID], [const.VALUE]),
    ([const.ID, const.MINUS, const.MINUS, const.ID], [const.VALUE]),
    ([const.ID, const.MINUS, const.PLUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.MINUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.PLUS, const.ID], [const.VALUE]),
    ([const.ID, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.ID, const.MINUS, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.ID, const.MINUS, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.ID, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.ID, const.MINUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.ID, const.MINUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.ID], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.ID], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.ID], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.VALUE, const.MINUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.VALUE], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.MINUS, const.FUNCTION_CALL], [const.VALUE]),
    ([const.FUNCTION_CALL, const.MINUS, const.PLUS, const.FUNCTION_CALL], [const.VALUE]),
    # endregion

    # endregion

    # region Enumerable Objects
    ([const.OPEN_CURLY_BRACKET, const.CLOSE_CURLY_BRACKET], [const.ENUMERABLE_OBJECT]),
    ([const.OPEN_CURLY_BRACKET, const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET],
                         [const.ENUMERABLE_OBJECT]),
    ([const.OPEN_SQUARE_BRACKET, const.CLOSE_SQUARE_BRACKET], [const.ENUMERABLE_OBJECT]),
    ([const.OPEN_SQUARE_BRACKET, const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET],
                         [const.ENUMERABLE_OBJECT]),
    ([const.OPEN_SQUARE_BRACKET, const.VALUE, const.CLOSE_SQUARE_BRACKET],
                         [const.ENUMERABLE_OBJECT]),
    ([const.OPEN_SQUARE_BRACKET, const.ID, const.CLOSE_SQUARE_BRACKET],
                         [const.ENUMERABLE_OBJECT]),

    # endregion

    # region Argument, Close Parenthesis
    ([const.ARGUMENT, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ([const.ID, const.COMMA, const.ID, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ([const.ID, const.COMMA, const.VALUE, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ([const.ID, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ([const.VALUE, const.COMMA, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ([const.VALUE, const.COMMA, const.ID, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    ([const.VALUE, const.COMMA, const.VALUE, const.CLOSE_PARENTHESIS],
                         [const.ARGUMENT, const.CLOSE_PARENTHESIS]),
    # endregion

    # region Associative Array Argument, Close Curly Bracket
    ([const.ID, const.COLON, const.VALUE], [const.ASSOCIATIVE_ARRAY_ARGUMENT]),
    (
        [const.ASSOCIATIVE_ARRAY_ARGUMENT, const.COMMA, const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET],
        [const.ASSOCIATIVE_ARRAY_ARGUMENT, const.CLOSE_CURLY_BRACKET]),
    # endregion

    # region Array Argument, Close Square Bracket
    ([const.ARRAY_ARGUMENT, const.COMMA, const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    ([const.ID, const.COMMA, const.ID, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    ([const.ID, const.COMMA, const.VALUE, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    ([const.ID, const.COMMA, const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    ([const.VALUE, const.COMMA, const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    ([const.VALUE, const.COMMA, const.ID, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    ([const.VALUE, const.COMMA, const.VALUE, const.CLOSE_SQUARE_BRACKET],
                         [const.ARRAY_ARGUMENT, const.CLOSE_SQUARE_BRACKET]),
    # endregion

    # region Function Declaration
    ([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.SUB, const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.FUNCTION, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.SUB, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.SUB, const.OPEN_PARENTHESIS, const.PARAM, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.SUB, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    ([const.SUB, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.ANONYMOUS_FUNCTION_DECLARATION]),
    # endregion

    # region Function Call
    ([const.ID, const.OPEN_PARENTHESIS, const.CLOSE_PARENTHESIS], [const.FUNCTION_CALL]),
    ([const.ID, const.OPEN_PARENTHESIS, const.ARGUMENT, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    ([const.ID, const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    ([const.ID, const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS], [const.FUNCTION_CALL]),
    ([const.ID, const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),
    ([const.ID, const.OPEN_PARENTHESIS, const.FUNCTION_CALL, const.CLOSE_PARENTHESIS],
                         [const.FUNCTION_CALL]),

    ([const.ID, const.DOT, const.FUNCTION_CALL], [const.FUNCTION_CALL]),
    ([const.FUNCTION_CALL, const.DOT, const.FUNCTION_CALL], [const.FUNCTION_CALL]),
    # endregion

    # region Value/ID/Variable Assignment in Brackets
    ([const.OPEN_PARENTHESIS, const.VALUE, const.CLOSE_PARENTHESIS], [const.VALUE]),
    ([const.OPEN_PARENTHESIS, const.ID, const.CLOSE_PARENTHESIS], [const.ID]),
    ([const.OPEN_PARENTHESIS, const.VAR_AS, const.CLOSE_PARENTHESIS], [const.VAR_AS]),
    # endregion

    # region Variable Assignment
    ([const.ID, const.EQUALS, const.ID], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.VALUE], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT], [const.VAR_AS]),

    ([const.ID, const.EQUALS, const.MINUS, const.VALUE], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.PLUS, const.VALUE], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.MINUS, const.ID], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.PLUS, const.ID], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.MINUS, const.FUNCTION_CALL], [const.VAR_AS]),
    ([const.ID, const.EQUALS, const.PLUS, const.FUNCTION_CALL], [const.VAR_AS]),
    # endregion

    # region Parameter
    ([const.PARAM, const.COMMA, const.PARAM], [const.PARAM]),
    ([const.ID, const.AS, const.TYPE], [const.PARAM]),
    ([const.VAR_AS, const.AS, const.TYPE], [const.PARAM]),
    # endregion

    # region For Statements

    # region For Statement to Value
    ([const.FOR, const.VAR_AS, const.TO, const.VALUE], [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.VALUE],
                         [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.ID],
                         [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.VALUE, const.STEP, const.FUNCTION_CALL],
                         [const.FOR_STATEMENT]),
    # endregion

    # region For Statement to ID
    ([const.FOR, const.VAR_AS, const.TO, const.ID], [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.VALUE],
                         [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.ID],
                         [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.ID, const.STEP, const.FUNCTION_CALL],
                         [const.FOR_STATEMENT]),
    # endregion

    # region For Statement to Function Call
    ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL], [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.VALUE],
                         [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.ID],
                         [const.FOR_STATEMENT]),
    ([const.FOR, const.VAR_AS, const.TO, const.FUNCTION_CALL, const.STEP, const.FUNCTION_CALL],
                         [const.FOR_STATEMENT]),
    # endregion
    # endregion

    # region While Statements
    ([const.WHILE, const.VAR_AS], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.ID], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.VALUE], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.FUNCTION_CALL], [const.WHILE_STATEMENT]),

    ([const.WHILE, const.PLUS, const.ID], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.PLUS, const.VALUE], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.PLUS, const.FUNCTION_CALL], [const.WHILE_STATEMENT]),

    ([const.WHILE, const.MINUS, const.ID], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.MINUS, const.VALUE], [const.WHILE_STATEMENT]),
    ([const.WHILE, const.MINUS, const.FUNCTION_CALL], [const.WHILE_STATEMENT]),
    # endregion

    # region Closing Statements
    ([const.END_FOR_TOKEN], [const.END_FOR]),
    ([const.END_IF_TOKEN], [const.END_IF]),
    ([const.END_WHILE_TOKEN], [const.END_WHILE]),
    ([const.END_SUB_TOKEN], [const.END_SUB]),
    ([const.END_FUNCTION_TOKEN], [const.END_FUNCTION]),
    ([const.END_TOKEN], [const.END]),
    # endregion

    # region Print Statements

    # region Simple Print
    ([const.PRINT_KEYWORD, const.VALUE], [const.PRINT_STATEMENT]),
    ([const.PRINT_KEYWORD, const.ID], [const.PRINT_STATEMENT]),
    ([const.PRINT_KEYWORD, const.FUNCTION_CALL], [const.PRINT_STATEMENT]),
    ([const.PRINT_KEYWORD, const.VAR_AS], [const.PRINT_STATEMENT]),
    ([const.PRINT_KEYWORD, const.PRINT_ARGUMENT], [const.PRINT_STATEMENT]),
    ([const.PRINT_KEYWORD, const.ENUMERABLE_OBJECT], [const.PRINT_STATEMENT]),
    # endregion

    # region Comma Print Arguments

    # region Variable Assignment Print Arguments
    ([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ID, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.COMMA, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.VALUE],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.COMMA, const.VALUE],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.COMMA, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.VAR_AS],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.COMMA, const.VAR_AS],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.COMMA, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.COMMA, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.COMMA, const.ENUMERABLE_OBJECT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.COMMA, const.ENUMERABLE_OBJECT],
                         [const.PRINT_ARGUMENT]),
    # endregion

    # region Simple Print Arguments
    ([const.ID, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ID, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.ID, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ID, const.COMMA, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    ([const.VALUE, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.COMMA, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    ([const.FUNCTION_CALL, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.COMMA, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    ([const.ENUMERABLE_OBJECT, const.COMMA, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ENUMERABLE_OBJECT, const.COMMA, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ENUMERABLE_OBJECT, const.COMMA, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.ENUMERABLE_OBJECT, const.COMMA, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ENUMERABLE_OBJECT, const.COMMA, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    # endregion

    # region Compound Print Arguments
    ([const.ID, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.ENUMERABLE_OBJECT, const.COMMA, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),

    # endregion

    # endregion

    # region Semi-Colon Print Arguments

    # region Variable Assignment Print Arguments
    ([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.PRINT_ARGUMENT],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.VALUE],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.ID],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.ID],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.FUNCTION_CALL],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.VAR_AS],
                         [const.PRINT_ARGUMENT]),

    ([const.ID, const.EQUALS, const.ID, const.SEMI_COLON, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.VALUE, const.SEMI_COLON, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.FUNCTION_CALL, const.SEMI_COLON, const.ENUMERABLE_OBJECT],
                         [const.PRINT_ARGUMENT]),
    ([const.ID, const.EQUALS, const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.ENUMERABLE_OBJECT],
                         [const.PRINT_ARGUMENT]),
    # endregion

    # region Simple Print Arguments
    ([const.ID, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.ID, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ([const.ID, const.SEMI_COLON, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.ID, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.ID, const.SEMI_COLON, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    ([const.VALUE, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.SEMI_COLON, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.SEMI_COLON, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    ([const.FUNCTION_CALL, const.SEMI_COLON, const.VALUE], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.SEMI_COLON, const.ID], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.SEMI_COLON, const.FUNCTION_CALL], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.SEMI_COLON, const.VAR_AS], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.SEMI_COLON, const.ENUMERABLE_OBJECT], [const.PRINT_ARGUMENT]),

    # endregion

    # region Compound Print Arguments
    ([const.ID, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.VALUE, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.FUNCTION_CALL, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),
    ([const.ENUMERABLE_OBJECT, const.SEMI_COLON, const.PRINT_ARGUMENT], [const.PRINT_ARGUMENT]),

    # endregion

    # endregion

    # endregion

    # region For Each
    ([const.FOR_EACH, const.ID, const.IN, const.ID], [const.FOR_EACH_STATEMENT]),
    ([const.FOR_EACH, const.ID, const.IN, const.VALUE], [const.FOR_EACH_STATEMENT]),
    ([const.FOR_EACH, const.ID, const.IN, const.FUNCTION_CALL], [const.FOR_EACH_STATEMENT]),
    # endregion

    # region If
    ([const.IF, const.VAR_AS], [const.IF_STATEMENT]),
    ([const.IF, const.VAR_AS], [const.IF_STATEMENT]),
    ([const.IF, const.VALUE], [const.IF_STATEMENT]),
    ([const.IF, const.ID], [const.IF_STATEMENT]),
    ([const.IF, const.FUNCTION_CALL], [const.IF_STATEMENT]),
    ([const.IF, const.ANONYMOUS_FUNCTION_DECLARATION], [const.IF_STATEMENT]),
    ([const.IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE], [const.IF_STATEMENT]),
    ([const.IF, const.VALUE, const.EQUALS, const.VALUE], [const.IF_STATEMENT]),
    ([const.IF, const.VALUE, const.EQUALS, const.ID], [const.IF_STATEMENT]),
    # end region

    # region If with then
    ([const.IF, const.VAR_AS, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.VAR_AS, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.VALUE, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.ID, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.FUNCTION_CALL, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.ANONYMOUS_FUNCTION_DECLARATION, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.VALUE, const.EQUALS, const.VALUE, const.THEN], [const.IF_STATEMENT]),
    ([const.IF, const.VALUE, const.EQUALS, const.ID, const.THEN], [const.IF_STATEMENT]),
    # end region If with then

    # region else if
    # region else If
    ([const.ELSE_IF, const.VAR_AS], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VAR_AS], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VALUE], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.ID], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.FUNCTION_CALL], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.ANONYMOUS_FUNCTION_DECLARATION], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VALUE, const.EQUALS, const.VALUE], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VALUE, const.EQUALS, const.ID], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE], [const.ELSE_STATEMENT]),
    # end region
    # end region

    # region else If then
    ([const.ELSE_IF, const.VAR_AS, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VAR_AS, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VALUE, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.ID, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.FUNCTION_CALL, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.ANONYMOUS_FUNCTION_DECLARATION, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.FUNCTION_CALL, const.EQUALS, const.VALUE, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VALUE, const.EQUALS, const.VALUE, const.THEN], [const.ELSE_IF_STATEMENT]),
    ([const.ELSE_IF, const.VALUE, const.EQUALS, const.ID, const.THEN], [const.ELSE_IF_STATEMENT])
    # end region

]

rules = []
for rule in rules_list:
    rules.append(ReductionRuleHandler(rule[0], rule[1]))
