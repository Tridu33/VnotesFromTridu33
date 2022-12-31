from chapter02.SmallStepSemantic import If
from chapter02.SmallStepSemantic.DoNothing import DoNothing
from chapter02.SmallStepSemantic.Sequence import Sequence


class While(object):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def to_s(self):
        return 'while (%s) {%s}' % (self.condition.to_s(), self.body.to_s())

    @staticmethod
    def reducible():
        return True

    def reduce(self, environment):
        return If(self.condition, Sequence(self.body, self), DoNothing()), environment
