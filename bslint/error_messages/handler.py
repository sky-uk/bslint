import bslint.error_messages.constants as err_const


def get_message(key, params=None):
    params = params or []
    if key not in err_const.ERROR_TABLE:
        raise ValueError(err_const.NO_SUCH_KEY)
    return err_const.ERROR_TABLE[key].get_message(params)
