class Error:

    def __init__(self, message):
        self.message = message

    def get_message(self, params):
        return self.message.format(*(params))
