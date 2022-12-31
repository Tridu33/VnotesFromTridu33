from chapter03.DFA.DFA import DFA


class DFADesign(object):
    def __init__(self, start_state, accept_states, rulebook):
        self.start_state = start_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def to_dfa(self):
        return DFA(self.start_state, self.accept_states, self.rulebook)

    def accepts(self, string):
        dfa = self.to_dfa()
        dfa.read_string(string)
        return dfa.accepting()
