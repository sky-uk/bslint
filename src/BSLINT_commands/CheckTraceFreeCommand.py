import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class CheckTraceFreeCommand(object):
    @staticmethod
    def execute(params):
        return {"error_key": ErrConst.TRACEABLE_CODE, "error_params": []}