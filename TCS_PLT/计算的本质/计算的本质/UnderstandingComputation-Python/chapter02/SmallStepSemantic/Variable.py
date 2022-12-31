class Variable(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def reducible():
        return True

    def reduce(self, environment):
        return environment[self.name]

    def to_s(self):
        return str(self.name)
