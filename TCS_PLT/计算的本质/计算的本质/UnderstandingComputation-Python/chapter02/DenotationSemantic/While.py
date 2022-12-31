class While(object):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def to_python(self):
        condition = self.condition.to_python()
        body = self.body.to_python()
        return 'while {condition}:\n    {body}'.format(**locals())