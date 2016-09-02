import src


class FileReader:

    @staticmethod
    def lex_file(config_file, file_to_lex):
        config_json = src.read_json(config_file)

        fo = open(file_to_lex, "r+")
        str_to_lex = fo.read()

        bslint_command_executor = src.BSLintCommandHandler(config_json)
        bslint_command_executor.execute_bslint_command("check_file_encoding", {"file_path": file_to_lex})
        lexer = src.Lexer(config_json)


        lexer.lex(str_to_lex)
