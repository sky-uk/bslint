import src


class FileReader:
    @staticmethod
    def read_file(file_to_lex):
        config_json = src.load_config_file()
        # print(config_json)

        fo = open(file_to_lex, "r+")
        str_to_lex = fo.read()

        bslint_command_executor = src.BSLintCommandHandler(config_json)
        return bslint_command_executor.execute_bslint_command("check_file_encoding",
                                                              {"file_path": file_to_lex}), str_to_lex, config_json
