class Assign(object):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def to_python(self):
        name = self.name
        expression = repr(self.expression.to_python())
        return '{name} = eval({expression}, globals())'.format(**locals())
