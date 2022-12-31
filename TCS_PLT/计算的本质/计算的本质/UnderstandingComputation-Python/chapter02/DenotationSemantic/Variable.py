class Variable(object):
    def __init__(self, name):
        self.name = name

    def to_python(self):
        return self.name
