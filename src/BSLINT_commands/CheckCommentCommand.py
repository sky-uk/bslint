import re


class CheckCommentCommand(object):

    @staticmethod
    def execute(params):
        if params["allow_TODOs"] and params["allow_generic_comments"]:
            if re.match(r"('|rem)\s*TODO", params["token"]):
                if not re.match(r"('|rem)\s*TODO\s+([A-Z]{2,3})", params["token"]):
                    return "TODOs must be initialled. Line number: " + str(params["line_number"])

        elif params["allow_TODOs"] and not params["allow_generic_comments"]:
            if not re.match(r"('|rem)\s*TODO\s+([A-Z]{2,3})", params["token"]):
                return "Comments must be TODOs and must be initialled. Line number: " + str(params["line_number"])

        elif not params["allow_TODOs"] and params["allow_generic_comments"]:
            if re.match(r"('|rem)\s*TODO", params["token"]):
                return "Comments must not be TODOs. Line number: " + str(params["line_number"])

        else:
            return "Comments are not allowed. Line number: " + str(params["line_number"])
