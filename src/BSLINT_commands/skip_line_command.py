class SkipLineCommand(object):

    @staticmethod
    def execute(params):
        return params["line_number"] + 1
