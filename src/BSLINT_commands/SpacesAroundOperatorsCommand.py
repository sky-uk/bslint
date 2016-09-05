import re
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class SpacesAroundOperatorsCommand(object):
    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()
        if not re.match("(\S{0,1})\s{" + str(params["spaces_around_operators"]) +"}\S\s{" + str(params["spaces_around_operators"]) + "}\S{0,1}$", params["characters"]):
                return error.get(ErrConst.NO_SPACE_AROUND_OPERATORS,
                                 [str(params["spaces_around_operators"]),
                                  params["line_number"]])
