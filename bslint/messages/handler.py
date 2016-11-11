import bslint.messages.error_constants as err_const
import bslint.messages.print_constants as print_const


def get_error_msg(key, params=None):
    return get_message(key, err_const.MESSAGE_TABLE, params, "")


def get_print_msg(key, params=None):
    return get_message(key, print_const.MESSAGE_TABLE, params, "\n")


def get_message(key, message_table, params, extra_chars):
    params = params or []
    if key not in message_table:
        raise ValueError(err_const.NO_SUCH_KEY)
    return message_table[key].get_message(params) + extra_chars
