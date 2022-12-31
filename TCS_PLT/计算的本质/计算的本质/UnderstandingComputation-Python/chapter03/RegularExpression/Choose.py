from chapter03.DFA.FARule import FARule
from chapter03.NFA.NFADesign import NFADesign
from chapter03.NFA.NFARulebook import NFARulebook
from chapter03.RegularExpression.Pattern import Pattern


class Choose(Pattern):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.precedence = 0

    def to_s(self):
        return '|'.join({pattern.bracket(self.precedence) for pattern in [self.first, self.second]})

    def to_nfa_design(self):
        first_nfa_design = self.first.to_nfa_design()
        second_nfa_design = self.second.to_nfa_design()

        start_state = object()
        accept_states = first_nfa_design.accept_states + second_nfa_design.accept_states
        rules = first_nfa_design.rulebook.rules + second_nfa_design.rulebook.rules
        extra_rules = [FARule(start_state, None, nfa_design.start_state) for nfa_design in [first_nfa_design, second_nfa_design]]
        rulebook = NFARulebook(rules + extra_rules)

        return NFADesign(start_state, accept_states, rulebook)