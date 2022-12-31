from chapter04.PDA.DPDA import DPDA
from chapter04.PDA.PDAConfiguration import PDAConfiguration
from chapter04.PDA.Stack import Stack


class DPDADesign(object):
    def __init__(self, start_state, bottom_character, accept_states, rulebook):
        self.start_state = start_state
        self.bottom_character = bottom_character
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepts(self, string):
        dpda = self.to_dpda
        dpda.read_string(string)
        return dpda.accepting

    @property
    def to_dpda(self):
        start_stack = Stack([self.bottom_character])
        start_configuration = PDAConfiguration(self.start_state, start_stack)
        return DPDA(start_configuration, self.accept_states, self.rulebook)