from chapter02.BigStepSemantic import Boolean


class If(object):
    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def evaluate(self, environment):
        if self.condition.evaluate(environment).value == Boolean(True).value:
            return self.consequence.evaluate(environment)
        elif self.condition.evaluate(environment).value == Boolean(False).value:
            return self.alternative.evaluate(environment)
