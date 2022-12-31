from chapter02.BigStepSemantic import Boolean


class While(object):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def evaluate(self, environment):
        if self.condition.evaluate(environment).value == Boolean(True).value:
            return self.evaluate(self.body.evaluate(environment))
        elif self.condition.evaluate(environment).value == Boolean(False).value:
            return environment
