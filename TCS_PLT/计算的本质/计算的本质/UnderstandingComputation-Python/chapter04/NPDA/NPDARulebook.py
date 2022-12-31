class NPDARulebook(object):
    def __init__(self, rules):
        self.rules = rules

    def next_configurations(self, configurations, character):
        nexts = []
        for config in configurations:
            nexts += self.follow_rules_for(config, character)

        return set(nexts)

    def follow_rules_for(self, configuration, character):
        return [rule.follow(configuration) for rule in self.rules_for(configuration, character)]

    def rules_for(self, configuration, character):
        return [rule for rule in self.rules if rule.applies_to(configuration, character)]

    def follow_free_moves(self, configurations):
        more_configurations = self.next_configurations(configurations, None)

        not_in_configs = []
        for more in more_configurations:
            flag = False
            for config in configurations:
                if str(more) == str(config):
                    flag = True
            if not flag:
                not_in_configs += [more]

        if not not_in_configs:
            return configurations
        else:
            return self.follow_free_moves(configurations.union(set(not_in_configs)))