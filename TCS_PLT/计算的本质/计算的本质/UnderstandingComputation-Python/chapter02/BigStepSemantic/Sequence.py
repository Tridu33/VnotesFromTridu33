class Sequence(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def evaluate(self, environment):
        return self.second.evaluate(self.first.evaluate(environment))
