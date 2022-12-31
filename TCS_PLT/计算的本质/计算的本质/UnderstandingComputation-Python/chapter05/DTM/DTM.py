class DTM(object):
    def __init__(self, current_configuration, accept_states, rulebook):
        self.current_configuration = current_configuration
        self.accept_states = accept_states
        self.rulebook = rulebook

    @property
    def accepting(self):
        return self.current_configuration.state in self.accept_states

    @property
    def step(self):
        self.current_configuration = self.rulebook.next_configuration(self.current_configuration)

    @property
    def run(self):
        while True:
            self.step
            if self.accepting or self.if_stuck:
                break

    @property
    def if_stuck(self):
        return not self.accepting and not self.rulebook.applies_to(self.current_configuration)