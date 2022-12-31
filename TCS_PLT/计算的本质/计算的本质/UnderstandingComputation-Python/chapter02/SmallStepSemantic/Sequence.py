from chapter02.SmallStepSemantic.DoNothing import DoNothing


class Sequence(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def to_s(self):
        return '{first}; {second}'.format(first=self.first.to_s(), second=self.second.to_s())

    @staticmethod
    def reducible():
        return True

    def reduce(self, environment):
        if self.first == DoNothing():
            return self.second, environment
        else:
            reduced_first, reduced_environment = self.first.reduce(environment)
            return Sequence(reduced_first, self.second), reduced_environment
