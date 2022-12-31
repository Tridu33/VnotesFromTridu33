class TMConfiguration(object):
    def __init__(self, state, tape):
        self.state = state
        self.tape = tape

    def __str__(self):
        state = self.state
        tape = self.tape
        return '#<struct TMConfiguration state={state}, tape={tape}>'.format(**locals())

    __repr__ = __str__
