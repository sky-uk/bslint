import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class SpacesAroundOperatorsCommand(object):
    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()
        if params["on_operator"]:
            if params["white_space"] != params["spaces_around_operators"]:
                return error.get(ErrConst.NO_SPACE_AROUND_OPERATORS,
                                 [str(params["spaces_around_operators"]),
                                  params["line_number"]])
