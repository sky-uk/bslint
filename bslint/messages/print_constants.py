from bslint import constants as const
from bslint.messages import builder as build

PATH_DOSNT_EXIST = "PATH_DOSNT_EXIST"
LINTING_COMPLETE = "LINTING_COMPLETE"
ALL_LINTED_CORRECTLY = "ALL_LINTED_CORRECTLY"
NO_MANIFEST = "NO_MANIFEST"
NO_BSLINTRC = "NO_BSLINTRC"
CANNOT_PARSE_BSLINTRC = "CANNOT_PARSE_BSLINTRC"
TOTAL_WARNINGS = "TOTAL_WARNINGS"
TOTAL_ERRORS = "TOTAL_ERRORS"
ERRORS_IN_FILE = "ERRORS_IN_FILE"
WARNINGS_IN_FILE = "WARNINGS_IN_FILE"
DESCRIPTION = "DESCRIPTION"
FILE_NAME = "FILE_NAME"
IN_FILE = "_IN_FILE"

WARNING_COLOUR = '\033[93m'
PASS_COLOUR = '\033[92m'
END_COLOUR = '\033[0m'
ERROR_COLOUR = '\033[91m'
FILE_COLOUR = '\033[34;4m'
TITLE_COLOUR = '\033[95m'
HEADER_COLOUR = '\033[34;4m'
TOTAL_COLOUR = '\033[35m'


MESSAGE_TABLE = {
    PATH_DOSNT_EXIST:
        build.Message(ERROR_COLOUR + "The path you have provided does not exist." + END_COLOUR),
    LINTING_COMPLETE:
        build.Message(FILE_COLOUR + "LINTING COMPLETE" + END_COLOUR),
    ALL_LINTED_CORRECTLY:
        build.Message(PASS_COLOUR + "All linted correctly" + END_COLOUR),
    NO_MANIFEST:
        build.Message(ERROR_COLOUR + "No manifest file found" + END_COLOUR),
    NO_BSLINTRC:
        build.Message(ERROR_COLOUR + "Cannot find bslintrc, using default config." + END_COLOUR),
    CANNOT_PARSE_BSLINTRC:
        build.Message(ERROR_COLOUR + "Unable to parse JSON in .bslintrc file" + END_COLOUR),
    TOTAL_WARNINGS:
        build.Message(TOTAL_COLOUR + "TOTAL WARNINGS: {}" + END_COLOUR),
    TOTAL_ERRORS:
        build.Message(TOTAL_COLOUR + "TOTAL ERRORS: {}" + END_COLOUR),
    const.WARNINGS + IN_FILE:
        build.Message(TOTAL_COLOUR + "WARNINGS IN FILE: {}" + END_COLOUR + "\n"),
    const.ERRORS + IN_FILE:
        build.Message(TOTAL_COLOUR + "ERRORS IN FILE: {}" + END_COLOUR + "\n"),
    DESCRIPTION:
        build.Message(TITLE_COLOUR + "BSLint: A linter for BrightScript." + END_COLOUR),
    const.WARNINGS: build.Message(WARNING_COLOUR + "{}" + END_COLOUR),
    const.ERRORS: build.Message(ERROR_COLOUR + "{}" + END_COLOUR),
    FILE_NAME: build.Message('\r' + FILE_COLOUR + "{}" + END_COLOUR)
}
