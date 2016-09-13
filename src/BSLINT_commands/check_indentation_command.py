import re
import src.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import src.constants as const


class CheckIndentationCommand(object):
    @staticmethod
    def execute(params):
        if params["indentation_level"] == const.DECREMENT_INDENTATION or \
                        params["indentation_level"] == const.SPECIAL_INDENTATION:
            params["current_indentation_level"] -= 1
        warning = CheckIndentationCommand._handle_warnings(params)
        if params["indentation_level"] == const.INCREMENT_INDENTATION or \
                        params["indentation_level"] == const.SPECIAL_INDENTATION:
            params["current_indentation_level"] += 1

        return warning, params["current_indentation_level"]

    @staticmethod
    def _handle_warnings(params):
        if re.search(r"\S", params["characters"]):
            if params["only_tab_indents"]:
                if not re.match("\t{" + str(params["current_indentation_level"]) + "}\S", params["characters"]):
                    return {"error_key": ErrConst.TAB_AND_SPACES, "error_params": []}
            else:
                if not re.match("\s{" + str(
                                params["tab_size"] *
                                params["current_indentation_level"]) + "}\S",
                                params["characters"]):
                    return {"error_key": ErrConst.TAB_INDENTATION_ERROR, "error_params": [params["tab_size"]]}
