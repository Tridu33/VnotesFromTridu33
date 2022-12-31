from chapter02.SmallStepSemantic import Boolean


class If(object):
    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def reduce(self, environment):
        if self.condition.reducible():
            return If(self.condition.reduce(environment), self.consequence, self.alternative), environment
        else:
            if self.condition.value == Boolean(True).value:
                return self.consequence, environment
            elif self.condition.value == Boolean(False).value:
                return self.alternative, environment

    @staticmethod
    def reducible():
        return True

    def to_s(self):
        return 'if {%s} {%s} else {%s}' % (self.condition.to_s(), self.consequence.to_s(), self.alternative.to_s())
