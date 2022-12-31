from chapter03.DFA.FARule import FARule
from chapter03.NFA.NFADesign import NFADesign
from chapter03.NFA.NFARulebook import NFARulebook
from chapter03.RegularExpression.Pattern import Pattern


class Concatenate(Pattern):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.precedence = 1

    def to_s(self):
        return ''.join({pattern.bracket(self.precedence) for pattern in [self.first, self.second]})

    def to_nfa_design(self):
        first_nfa_design = self.first.to_nfa_design()
        second_nfa_design = self.second.to_nfa_design()

        start_state = first_nfa_design.start_state
        accept_state = second_nfa_design.accept_states
        rules = first_nfa_design.rulebook.rules + second_nfa_design.rulebook.rules
        extra_rules = [FARule(state, None, second_nfa_design.start_state) for state in first_nfa_design.accept_states]
        rulebook = NFARulebook(rules + extra_rules)

        return NFADesign(start_state, accept_state, rulebook)
