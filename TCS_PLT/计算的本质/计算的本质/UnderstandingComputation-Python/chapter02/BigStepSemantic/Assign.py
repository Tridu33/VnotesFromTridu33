class Assign(object):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def evaluate(self, environment):
        return dict(environment, **{self.name: self.expression.evaluate(environment)})
