import bslint.error_messages_builder.error_builder.error_messages_constants as err


def get_message(key, params=[]):
    if key not in err.ERROR_TABLE:
        raise ValueError("No Error with such key")
    return err.ERROR_TABLE[key].get_message(params)



