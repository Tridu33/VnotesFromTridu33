class Number(object):
    def __init__(self, value):
        self.value = value

    def to_python(self):
        return repr(self.value)
