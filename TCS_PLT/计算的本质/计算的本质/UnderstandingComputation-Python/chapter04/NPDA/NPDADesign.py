from chapter04.NPDA.NPDA import NPDA
from chapter04.NPDA.PDAConfiguration import PDAConfiguration
from chapter04.NPDA.Stack import Stack


class NPDADesign(object):
    def __init__(self, start_state, bottom_character, accept_states, rulebook):
        self.start_state = start_state
        self.bottom_character = bottom_character
        self.accept_states = accept_states
        self.rulebook = rulebook

    def accepts(self, string):
        npda = self.to_npda
        npda.read_string(string)
        return npda.accepting

    @property
    def to_npda(self):
        start_stack = Stack([self.bottom_character])
        start_configuration = PDAConfiguration(self.start_state, start_stack)
        return NPDA(set([start_configuration]), self.accept_states, self.rulebook)