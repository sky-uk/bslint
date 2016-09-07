import string
import src


class StylingRulesHandler:

    def __init__(self, config):
        self.config = config

    def apply(self, command, params={}):
        class_name = string.capwords(command, "_").replace("_", "") + "Command"
        if self.config[command]['active'] is True:
            return getattr(src, class_name).execute({**params, **self.config[command]['params']})