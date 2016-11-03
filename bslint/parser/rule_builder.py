import collections


def load_grammar_rules(rules_list):
    grammar_rule = collections.namedtuple('Rule', ['rule', 'result', 'priority'])
    rules = {}
    for priority in rules_list:
        for rule in rules_list[priority]:
            if priority not in rules:
                rules[priority] = []
            rules[priority].append(grammar_rule(rule[0], rule[1], priority))
    return rules
