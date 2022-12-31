class PDAConfiguration(object):
    STUCK_STATE = object()

    def __init__(self, state, stack):
        self.state = state
        self.stack = stack

    @property
    def stuck(self):
        return PDAConfiguration(self.__class__.STUCK_STATE, self.stack)

    @property
    def if_stuck(self):
        return self.state == self.__class__.STUCK_STATE

    def __str__(self):
        state = self.state
        stack = repr(self.stack)
        return '#<struct PDAConfiguration state={state}, stack={stack}>'.format(**locals())

    __repr__ = __str__
