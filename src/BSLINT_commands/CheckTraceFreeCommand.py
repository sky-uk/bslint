import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class CheckTraceFreeCommand(object):
    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()
        return error.get(ErrConst.TRACEABLE_CODE, [params['line_number']])