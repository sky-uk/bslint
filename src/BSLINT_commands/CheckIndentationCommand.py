import re
import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst
import Constants as const


class CheckIndentationCommand(object):
    @staticmethod
    def execute(params):
        if params["indentation_level"] == const.DECREMENT_INDENTATION or \
                        params["indentation_level"] == const.SPECIAL_INDENTATION:
            params["current_indentation_level"] += -1
        warning = CheckIndentationCommand._handle_warnings(params)
        if params["indentation_level"] == const.INCREMENT_INDENTATION or \
                        params["indentation_level"] == const.SPECIAL_INDENTATION:
            params["current_indentation_level"] += 1

        return warning, params["current_indentation_level"]

    @staticmethod
    def _handle_warnings(params):
        error = Err.ErrorMessageHandler()
        if re.search(r"\S", params["characters"]):
            if params["indentation"]["params"]["only_tab_indents"]:
                if not re.match("\t{" + str(params["current_indentation_level"]) + "}\S", params["characters"]):
                    return error.get(ErrConst.TAB_AND_SPACES, [str(params["line_number"])])
            else:
                if not re.match("\s{" + str(
                                params["indentation"]["params"]["tab_size"] *
                                params["current_indentation_level"]) + "}\S",
                                params["characters"]):
                    return error.get(ErrConst.TAB_INDENTATION_ERROR,
                                     [params["indentation"]["params"]["tab_size"], str(params["line_number"])])
