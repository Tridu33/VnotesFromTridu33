class Boolean(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def evaluate(self, environment):
        return self
