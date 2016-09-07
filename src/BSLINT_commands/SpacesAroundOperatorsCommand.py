import re
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class SpacesAroundOperatorsCommand(object):
    @staticmethod
    def execute(params):
        if not re.match("(\S{0,1})\s{" + str(params["spaces_around_operators"]) + "}\S\s{" + str(
                params["spaces_around_operators"]) + "}\S{0,1}$", params["characters"]):
            return {"error_key": ErrConst.NO_SPACE_AROUND_OPERATORS,
                    "error_params": [params["spaces_around_operators"]]}
