class DFA(object):
    def __init__(self, current_state, accept_states, rulebook):
        self.current_state = current_state
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepting(self):
        return self.current_state in self.accept_states

    def read_character(self, character):
        self.current_state = self.rulebook.next_state(self.current_state, character)

    def read_string(self, string):
        for character in string:
            self.read_character(character)