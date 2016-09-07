import re
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class CheckCommentCommand(object):

    @staticmethod
    def execute(params):
        if params["TODOs"]["allow_TODOs"] and params["allow_generic_comments"]:
            if re.match(r"('|rem)\s*TODO", params["token"]):
                if not re.match(params["TODOs"]["format"], params["token"]):
                    return {"error_key": ErrConst.NON_CONVENTIONAL_TODO, "error_params": []}

        elif params["TODOs"]["allow_TODOs"] and not params["allow_generic_comments"]:
            if not re.match(params["TODOs"]["format"], params["token"]):
                return {"error_key": ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, "error_params": []}

        elif not params["TODOs"]["allow_TODOs"] and params["allow_generic_comments"]:
            if re.match(r"('|rem)\s*TODO", params["token"]):
                return {"error_key": ErrConst.NO_TODOS, "error_params": []}

        else:
            return {"error_key": ErrConst.COMMENTS_NOT_ALLOWED, "error_params": []}

