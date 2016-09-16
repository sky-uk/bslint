import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as Err


class error_message_handler:
    @staticmethod
    def get(key, params=[]):
        if key not in Err.ERROR_TABLE:
            raise ValueError("No Error with such key")
        return Err.ERROR_TABLE[key].get_message(params)



