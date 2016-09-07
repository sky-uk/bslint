import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class ConsecutiveEmptyLinesCommand(object):
    @staticmethod
    def execute(params):
        if params["empty_lines"] > params["consecutive_empty_lines"]:
            return {"error_key": ErrConst.CONSECUTIVE_EMPTY_LINES, "error_params": [params['consecutive_empty_lines']]}