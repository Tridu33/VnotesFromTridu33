from chapter03.DFA.FARule import FARule
from chapter03.NFA.NFADesign import NFADesign
from chapter03.NFA.NFARulebook import NFARulebook
from chapter03.RegularExpression.Pattern import Pattern


class Literal(Pattern):
    def __init__(self, character):
        self.precedence = 3
        self.character = character

    def to_s(self):
        return self.character

    def to_nfa_design(self):
        start_state = object()
        accept_states = object()
        rule = FARule(start_state, self.character, accept_states)
        rulebook = NFARulebook([rule])
        return NFADesign(start_state, [accept_states], rulebook)
