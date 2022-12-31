from chapter04.NPDA.PDAConfiguration import PDAConfiguration


class PDARule(object):
    def __init__(self, state, character, next_state, pop_character, push_characters):
        self.state = state
        self.character = character
        self.next_state = next_state
        self.pop_character = pop_character
        self.push_characters = push_characters

    def applies_to(self, configuration, character):
        return self.state == configuration.state and \
               self.pop_character == configuration.stack.top and \
               self.character == character

    def follow(self, configuration):
        return PDAConfiguration(self.next_state, self.next_stack(configuration))

    def next_stack(self, configuration):
        popped_stack = configuration.stack.pop
        for item in self.push_characters[::-1]:
            popped_stack = popped_stack.push(item)
        return popped_stack

    def __str__(self):
        s = repr(self.state)
        char = repr(self.character)
        nexts = repr(self.next_state)
        pop_char = repr(self.pop_character)
        push_chars = repr(self.push_characters)

        return '#<struct PDARule\n\
        state={s},\n\
        character={char},\n\
        next_state={nexts},\n\
        pop_character={pop_char},\n\
        push_characters={push_chars}'.format(**locals())

    __repr__ = __str__