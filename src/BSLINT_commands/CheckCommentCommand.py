import re
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class CheckCommentCommand(object):

    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()
        if params["TODOs"]["allow_TODOs"] and params["allow_generic_comments"]:
            if re.match(r"('|rem)\s*TODO", params["token"]):
                if not re.match(params["TODOs"]["format"], params["token"]):
                    return error.get(ErrConst.NON_CONVENTIONAL_TODO, [str(params["line_number"])])

        elif params["TODOs"]["allow_TODOs"] and not params["allow_generic_comments"]:
            if not re.match(params["TODOs"]["format"], params["token"]):
                return error.get(ErrConst.NON_CONVENTIONAL_TODO_AND_NO_COMMENTS, [str(params["line_number"])])

        elif not params["TODOs"]["allow_TODOs"] and params["allow_generic_comments"]:
            if re.match(r"('|rem)\s*TODO", params["token"]):
                return error.get(ErrConst.NO_TODOS, [str(params["line_number"])])

        else:
            return error.get(ErrConst.COMMENTS_NOT_ALLOWED, [str(params["line_number"])])

