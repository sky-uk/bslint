import bslint.error_messages_builder.error_messages_constants as err
import bslint.error_messages_builder.error_messages_constants as err_const


def get_message(key, params=[]):
    if key not in err.ERROR_TABLE:
        raise ValueError(err_const.NO_SUCH_KEY)
    return err.ERROR_TABLE[key].get_message(params)



