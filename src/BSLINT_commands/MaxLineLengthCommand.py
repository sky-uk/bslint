class MaxLineLengthCommand(object):
    @staticmethod
    def execute(params):
        if params["max_line_length"] < params["line_length"]:
            return "Line length exceeds max line length [" + str(params["max_line_length"]) + "]. Line number: " + str(
                params["line_number"])
        return None
