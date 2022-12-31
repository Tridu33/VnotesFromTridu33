class DTMRulebook(object):
    def __init__(self, rules):
        self.rules = rules

    def next_configuration(self, configuration):
        return self.rule_for(configuration).follow(configuration)

    def rule_for(self, configuration):
        for rule in self.rules:
            if rule.applies_to(configuration):
                return rule

    def applies_to(self, configuration):
        return self.rule_for(configuration) != None
