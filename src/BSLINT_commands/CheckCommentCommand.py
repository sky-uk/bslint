import re


class CheckCommentCommand(object):

    def execute(params):
        if not re.match(r"('|rem)\s*TODO\s+([A-Z]{2,3})", params["token"]):
            return "Comments must be TODOs and must be initialled. Line number: " + str(params["line_number"])
