import src


class FileReader:
    @staticmethod
    def read_file(file_to_lex):
        config_json = src.load_config_file()

        fo = open(file_to_lex, "r+")
        str_to_lex = fo.read()

        bslint_command_executor = src.StylingRulesHandler(config_json)
        return bslint_command_executor.apply("check_file_encoding",
                                             {"file_path": file_to_lex}), str_to_lex, config_json
