class DPDA(object):
    def __init__(self, current_configuration, accept_states, rulebook):
        self._current_configuration = current_configuration
        self.accept_states = accept_states
        self.rulebook = rulebook

    @property
    def current_configuration(self):
        return self.rulebook.follow_free_moves(self._current_configuration)

    @property
    def accepting(self):
        if self.current_configuration.state in self.accept_states:
            return True
        else:
            return False

    def next_configuration(self, character):
        if self.rulebook.applies_to(self.current_configuration, character):
            return self.rulebook.next_configuration(self.current_configuration, character)
        else:
            return self.current_configuration.stuck

    @property
    def if_stuck(self):
        return self.current_configuration.if_stuck

    def read_character(self, character):
        self._current_configuration = self.next_configuration(character)

    def read_string(self, string):
        for char in string:
            if not self.if_stuck:
                self.read_character(char)