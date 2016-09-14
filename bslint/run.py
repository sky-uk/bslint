import bslint

def run():
    config = bslint.load_config_file(user='SpellCheck/spellcheck-config.json', default='test-config.json')
    lexer = bslint.Lexer(config)
    lexer.lex("sdafsb ")