import bslint.lexer as lexer


def get_string_to_parse(filepath):
    fo = open(filepath, "r+")
    str_to_parse = fo.read()

    return str_to_parse


def lex_from_file():
    filepath = "../resources/SkeletonMain.brs"
    fo = open(filepath, "r+")
    str_to_parse = fo.read()
    print(lexer.lex(str_to_parse))

if __name__ == "__main__":
    lex_from_file()

