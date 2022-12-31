from chapter02.BigStepSemantic.Number import Number


class Multiply(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, environment):
        return Number(self.left.evaluate(environment).value * self.right.evaluate(environment).value)
