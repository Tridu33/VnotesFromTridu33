from chapter02.SmallStepSemantic.DoNothing import DoNothing


class Assign(object):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def to_s(self):
        return '{name} = {expression}'.format(name=self.name, expression=self.expression.to_s())

    @staticmethod
    def reducible():
        return True

    def reduce(self, environment):
        if self.expression.reducible():
            return Assign(self.name, self.expression.reduce(environment)), environment
        else:
            return DoNothing(), dict(environment, **{self.name: self.expression})
