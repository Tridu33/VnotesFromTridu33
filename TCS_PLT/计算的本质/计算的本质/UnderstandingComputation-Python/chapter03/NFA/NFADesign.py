from chapter03.NFA.NFA import NFA


class NFADesign(object):
    def __init__(self, start_state, accept_states, rulebook):
        self.start_state = start_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def to_nfa(self):
        return NFA(set([self.start_state]), self.accept_states, self.rulebook)

    def accepts(self, string):
        nfa = self.to_nfa()
        nfa.read_string(string)
        return nfa.accepting()