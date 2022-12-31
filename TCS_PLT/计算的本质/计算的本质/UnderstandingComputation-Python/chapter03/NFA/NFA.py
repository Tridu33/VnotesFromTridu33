class NFA(object):
    def __init__(self, current_states, accept_states, rulebook):
        self._current_states = current_states
        self.accept_states = accept_states
        self.rulebook = rulebook

    @property
    def current_states(self):
        return self.rulebook.follow_free_moves(self._current_states)

    def accepting(self):
        if [state for state in self.current_states if state in self.accept_states]:
            return True
        else:
            return False

    def read_character(self, character):
        self._current_states = self.rulebook.next_states(self.current_states, character)

    def read_string(self, string):
        for character in string:
            self.read_character(character)