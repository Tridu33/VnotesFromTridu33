class Add(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_python(self):
        left = repr(self.left.to_python())
        right = repr(self.right.to_python())
        return 'eval({left}, globals()) + eval({right}, globals())'.format(**locals())
