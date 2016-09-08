import src

def run():
    config = src.load_config_file(user='SpellCheck/spellcheck-config.json', default='test-config.json')
    lexer = src.Lexer(config)
    lexer.lex("sdafsb ")