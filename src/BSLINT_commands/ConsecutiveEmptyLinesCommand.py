import re
import Constants as const

import src.ErrorMessagesBuilder.ErrorMessageHandler as Err
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class ConsecutiveEmptyLinesCommand(object):
    @staticmethod
    def execute(params):
        error = Err.ErrorMessageHandler()

        if params["empty_lines"] > params["consecutive_empty_lines"]:
            return error.get(ErrConst.CONSECUTIVE_EMPTY_LINES,
                             [params['consecutive_empty_lines'], params['line_number']])