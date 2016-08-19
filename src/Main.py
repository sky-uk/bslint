import src


def main(filepath):
    fo = open(filepath, "r+")
    str_to_parse = fo.read()

    return str_to_parse


def lex_from_file():
    filepath = "../resources/BasicStringAssignment.txt"
    fo = open(filepath, "r+")
    str_to_parse = fo.read()
    lexer = src.Lexer()
    print(lexer.lex(str_to_parse))

if __name__ == "__main__":
    lex_from_file()

