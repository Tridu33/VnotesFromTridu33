from chapter02.BigStepSemantic.Boolean import Boolean


class LessThan(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, environment):
        return Boolean(self.left.evaluate(environment).value < self.right.evaluate(environment).value)
