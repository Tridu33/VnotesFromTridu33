class NPDA(object):
    def __init__(self, current_configurations, accept_states, rulebook):
        self._current_configurations = current_configurations
        self.accept_states = accept_states
        self.rulebook = rulebook

    @property
    def current_configurations(self):
        return self.rulebook.follow_free_moves(self._current_configurations)

    @property
    def accepting(self):
        if [config for config in self.current_configurations if config.state in self.accept_states]:
            return True
        else:
            return False

    def read_character(self, character):
        self._current_configurations = self.rulebook.next_configurations(self.current_configurations, character)

    def read_string(self, string):
        for character in string:
            self.read_character(character)