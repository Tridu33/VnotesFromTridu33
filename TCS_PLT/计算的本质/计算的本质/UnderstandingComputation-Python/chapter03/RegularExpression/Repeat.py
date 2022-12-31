from chapter03.DFA.FARule import FARule
from chapter03.NFA.NFADesign import NFADesign
from chapter03.NFA.NFARulebook import NFARulebook
from chapter03.RegularExpression.Pattern import Pattern


class Repeat(Pattern):
    def __init__(self, pattern):
        self.precedence = 2
        self.pattern = pattern

    def to_s(self):
        return self.pattern.bracket(self.precedence) + "*"

    def to_nfa_design(self):
        pattern_nfa_design = self.pattern.to_nfa_design()

        start_state = object()
        accept_states = pattern_nfa_design.accept_states + [start_state]
        rules = pattern_nfa_design.rulebook.rules
        extra_rules = [FARule(accept_state, None, pattern_nfa_design.start_state) for accept_state in pattern_nfa_design.accept_states] + [FARule(start_state, None, pattern_nfa_design.start_state)]
        rulebook = NFARulebook(rules + extra_rules)

        return NFADesign(start_state, accept_states, rulebook)