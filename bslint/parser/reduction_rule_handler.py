class ReductionRuleHandler:
    def __init__(self, rule, result):
        self.rule = rule
        self.result = result

    def get_last_token(self):
        return self.rule[-1]