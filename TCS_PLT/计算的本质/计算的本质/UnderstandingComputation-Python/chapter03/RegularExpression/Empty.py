from chapter03.NFA.NFADesign import NFADesign
from chapter03.NFA.NFARulebook import NFARulebook
from chapter03.RegularExpression.Pattern import Pattern


class Empty(Pattern):
    def __init__(self):
        self.precedence = 3
        self.character = None

    @staticmethod
    def to_s():
        return ''

    @staticmethod
    def to_nfa_design():
        start_state = object()
        accept_states = [start_state]
        rulebook = NFARulebook([])
        return NFADesign(start_state, accept_states, rulebook)
