class Sequence(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def to_python(self):
        first = self.first.to_python()
        second = self.second.to_python()
        return '{first}\n{second}'.format(**locals())
