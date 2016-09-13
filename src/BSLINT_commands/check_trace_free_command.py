import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst


class CheckTraceFreeCommand(object):
    @staticmethod
    def execute(params):
        return {"error_key": ErrConst.TRACEABLE_CODE, "error_params": []}