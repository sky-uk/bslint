import bslint.utilities.commands as commands


class FileReader:
    @staticmethod
    def read_file(file_to_lex):
        fo = open(file_to_lex, "r+")
        str_to_lex = fo.read()

        return {"invalid_encoding": commands.check_file_encoding(file_to_lex), "str_to_lex": str_to_lex}
