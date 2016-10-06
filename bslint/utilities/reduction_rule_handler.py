class ReductionRuleHandler:
    def __init__(self, rules, result):
        self.rules = rules
        self.result = result

    def get_rule_last(self):
        return self.rules[-1]