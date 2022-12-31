class Stack(object):
    def __init__(self, contents):
        self.contents = contents

    def push(self, character):
        return Stack([character] + self.contents)

    @property
    def pop(self):
        return Stack(self.contents[1:])

    @property
    def top(self):
        return self.contents[0]

    def __str__(self):
        top = self.contents[0]
        underside = ''.join(self.contents[1:])
        return '#<Stack ({top}){underside}>'.format(**locals())

    __repr__ = __str__
