import bslint.parser.valid_token_associations as vta


def is_valid_token(preceding_token, current_token):
    return current_token in vta.valid_token_associations[preceding_token]