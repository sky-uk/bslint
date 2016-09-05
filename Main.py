import sys
import src
import glob


def run(file):
    file_reader = src.FileReader()
    result = file_reader.read_file(file)
    lexer = src.Lexer(result[2])
    if result[0]:
        print(result[0])

    lex_result = lexer.lex(result[1])
    if lex_result["Status"] == "Error":
        print("Errors in  " + filename + ": " + str(lex_result["Tokens"]) + "\n\n")
        if lex_result["Warnings"]:
            print("Warnings in  " + filename + ": " + str(lex_result["Warnings"]) + "\n\n")
        else:
            print(filename + " lexed without warnings")
    else:
        print(filename + " lexed without errors")
        if lex_result["Warnings"]:
            print("Warnings in  " + filename + ": " + str(lex_result["Warnings"]) + "\n\n")
        else:
            print(filename + " lexed without warnings")


if __name__ == '__main__':
    for filename in glob.iglob(sys.argv[1] + '/**/*.brs', recursive=True):
        run(filename)
        #print(filename)
    # run(sys.argv[1])
