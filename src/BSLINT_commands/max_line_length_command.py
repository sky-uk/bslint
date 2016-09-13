import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst


class MaxLineLengthCommand(object):
    @staticmethod
    def execute(params):
        if params["max_line_length"] < params["line_length"]:
            return {"error_key": ErrConst.LINE_LENGTH, "error_params": [params["max_line_length"]]}