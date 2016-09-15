import bslint
import bslint.commands as commands


class FileReader:
    @staticmethod
    def read_file(file_to_lex):
        config_json = bslint.load_config_file()

        fo = open(file_to_lex, "r+")
        str_to_lex = fo.read()

        return commands.check_file_encoding(file_to_lex), str_to_lex, config_json
