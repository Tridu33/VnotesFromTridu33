from chapter02.SmallStepSemantic.Number import Number


class Add(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    @staticmethod
    def reducible():
        return True

    def reduce(self, environment):
        if self.left.reducible():
            return Add(self.left.reduce(environment), self.right)
        elif self.right.reducible():
            return Add(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.value + self.right.value)

    def to_s(self):
        return self.left.to_s() + ' + ' + self.right.to_s()