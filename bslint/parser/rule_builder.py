import collections


def load_grammar_rules(rules_list):
    grammar_rule = collections.namedtuple('Rule', ['rule', 'result', 'priority'])
    rules = {}
    for priority in rules_list:
        if priority not in rules:
            rules[priority] = {}
        for final_token in rules_list[priority]:
            if final_token not in rules[priority]:
                rules[priority][final_token] = []
            for rule in rules_list[priority][final_token]:
                rules[priority][final_token].append(grammar_rule(rule[0], rule[1], priority))
    return rules
