import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class MaxLineLengthCommand(object):
    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()
        if params["max_line_length"] < params["line_length"]:
            return error.get(ErrConst.LINE_LENGTH, [str(params["max_line_length"]), str(params["line_number"])])
        return None
