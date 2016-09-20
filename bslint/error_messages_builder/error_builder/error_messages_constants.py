import bslint.error_messages_builder.error_builder.error_message_builder as ErrBuilder

ERROR = "ERROR"
WARNING = "WARNING"

LINE_LENGTH = "LINE_LENGTH"
FILE_ENCODING = "FILE_ENCODING"
CONSECUTIVE_EMPTY_LINES = "CONSECUTIVE_EMPTY_LINES"
UPPERCASE_VARIABLE = "UPPERCASE_VARIABLE"
TAB_INDENTATION_ERROR = "TAB_INDENTATION_ERROR"
TAB_AND_SPACES = "TAB_AND_SPACES"
TYPO_IN_CODE = "TYPO_IN_CODE"
TRACEABLE_CODE = "TRACEABLE_CODE"
NON_CONVENTIONAL_TODO = "NON_CONVENTIONAL_TODO"
COMMENTS_NOT_ALLOWED = "COMMENTS_NOT_ALLOWED"
NO_RETURN_AND_PARAMETERS_TYPES = "NO_RETURN_AND_PARAMETERS_TYPES"
NOT_CAPITALISED_VARIABLE_NAMES = "NOT_CAPITALISED_VARIABLE_NAMES"
NO_SPACE_AROUND_OPERATORS = "NO_SPACE_AROUND_OPERATORS = {NO_SPACE_AROUND_OPERATORS"
NO_SPACE_BETWEEN_METHOD_AND_PARAMETERS = "NO_SPACE_BETWEEN_METHOD_AND_PARAMETERS"
UNMATCHED_QUOTATION_MARK = "UNMATCHED_QUOTATION_MARK"
NON_CONVENTIONAL_TODO_AND_NO_COMMENTS = "NON_CONVENTIONAL_TODO_AND_NO_COMMENTS"
NO_TODOS = "NO_TODOS"
METHOD_DECLARATION_SPACING = "METHOD_DECLARATION_SPACING"

ERROR_TABLE = {
        LINE_LENGTH: ErrBuilder.Error(WARNING + ": Line length exceeds {} number of characters. Line number: {}"),
        FILE_ENCODING: ErrBuilder.Error(WARNING + ": Your files should conform to {} encoding"),
        CONSECUTIVE_EMPTY_LINES: ErrBuilder.Error(WARNING + ": Cannot have more than {} consecutive empty lines. Line number: {}"),
        UPPERCASE_VARIABLE: ErrBuilder.Error(WARNING + ": Variables should begin with a lowercase letter: line number: {}"),
        TAB_INDENTATION_ERROR: ErrBuilder.Error(WARNING + ": Tab indentation should be set to {} spaces. Line number: {}"),
        TAB_AND_SPACES: ErrBuilder.Error(WARNING + ": Invalid indentation, you must indent with tabs. Line number: {}"),
        TYPO_IN_CODE: ErrBuilder.Error(WARNING + ": You have spelling mistakes in your code. Line number: {}"),
        TRACEABLE_CODE: ErrBuilder.Error(WARNING + ": Print statements not allowed. Line number: {}"),
        NON_CONVENTIONAL_TODO_AND_NO_COMMENTS: ErrBuilder.Error(WARNING + ": Comments must be TODOs and must follow convention. Line number: {}"),
        COMMENTS_NOT_ALLOWED: ErrBuilder.Error(WARNING + ": No comments allowed. Line number: {}"),
        NO_RETURN_AND_PARAMETERS_TYPES: ErrBuilder.Error(WARNING + ": No return and parameter types declared. Line number: {}"),
        NOT_CAPITALISED_VARIABLE_NAMES: ErrBuilder.Error(WARNING + ": Variable types must be capitalised. Line number: {}"),
        NO_SPACE_AROUND_OPERATORS: ErrBuilder.Error(WARNING + ": Operators must be surrounded by {} space(s). Line number: {}"),
        NO_SPACE_BETWEEN_METHOD_AND_PARAMETERS: ErrBuilder.Error( WARNING + ": You must put a space between method name and parameter list. Line number: {}"),
        UNMATCHED_QUOTATION_MARK: ErrBuilder.Error(ERROR + ": You have unmatched quotation marks at {} on line number: {}"),
        NON_CONVENTIONAL_TODO: ErrBuilder.Error(WARNING + ": TODOs must follow convention. Line number: {}"),
        NO_TODOS: ErrBuilder.Error(WARNING + ": Comments must not be TODOs. Line number: {}"),
        METHOD_DECLARATION_SPACING: ErrBuilder.Error(WARNING + ": The spacing on the method declaration is incorrect: {}"),
    }
