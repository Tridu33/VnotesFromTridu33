class DPDARulebook(object):
    def __init__(self, rules):
        self.rules = rules

    def next_configuration(self, configuration, character):
        return self.rule_for(configuration, character).follow(configuration)

    def rule_for(self, configuration, character):
        for rule in self.rules:
            if rule.applies_to(configuration, character):
                return rule
        return None

    def applies_to(self, configuration, character):
        return self.rule_for(configuration, character) != None

    def follow_free_moves(self, configuration):
        if self.applies_to(configuration, None):
            return self.follow_free_moves(self.next_configuration(configuration, None))
        else:
            return configuration