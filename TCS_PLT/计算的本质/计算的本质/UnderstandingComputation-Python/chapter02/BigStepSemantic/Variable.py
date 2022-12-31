class Variable(object):
    def __init__(self, name):
        self.name = name

    def evaluate(self, environment):
        return environment[self.name]
