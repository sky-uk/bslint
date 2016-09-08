"""bslint.bslint: provides entry point main()."""
__version__ = "0.2.1"
import os
import sys
import src
import src.Constants as const

is_lexed_correctly = True


def main():
    print(const.TITLE_COLOUR + "BSLint: A linter for BrightScript. %s. \n" % __version__ + const.END_COLOUR)
    global is_lexed_correctly
    if len(sys.argv) == 1:
        lint_all("")
    else:
        filename = '/' + sys.argv[1]
        file = os.getcwd() + filename
        if not os.path.exists(file):
            is_lexed_correctly = False
        if os.path.isfile(file):
            lint_specific(file)
        else:
            lint_all(filename)
    if is_lexed_correctly:
        print(const.PASS_COLOUR + 'All lexed correctly' + const.END_COLOUR)
        print("\n")


def lint_all(directory):
    for root, dirs, files in os.walk(os.getcwd() + directory):

        for file in files:
            if file.endswith(".brs"):
                filepath = os.path.join(root, file)
                filepath = filepath.replace(os.getcwd() + '/', '')
                lint_specific(filepath)


def lint_specific(filename):
    if filename.endswith(".brs"):
        file_reader = src.FileReader()
        result = file_reader.read_file(filename)
        lexer = src.Lexer(result[2])
        if result[0]:
            print(result[0])

        lex_result = lexer.lex(result[1])
        if lex_result["Status"] == "Error" or lex_result["Warnings"]:
            global is_lexed_correctly
            is_lexed_correctly = False
            print(const.FILE_COLOUR + filename + const.END_COLOUR)
            if lex_result["Status"] == "Error":
                for error in lex_result["Tokens"]:
                    print(const.ERROR_COLOUR + str(error) + const.END_COLOUR)
            for warning in lex_result["Warnings"]:
                print(const.WARNING_COLOUR + str(warning) + const.END_COLOUR)
            print("\n")
    else:
        is_lexed_correctly = False
