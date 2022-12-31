class DFARulebook(object):
    def __init__(self, rules):
        self.rules = rules

    def next_state(self, state, character):
        return self.rule_for(state, character).follow()

    def rule_for(self, state, character):
        for rule in self.rules:
            if rule.applies_to(state, character):
                return rule
