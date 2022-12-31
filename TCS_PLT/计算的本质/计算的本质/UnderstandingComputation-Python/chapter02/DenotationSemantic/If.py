class If(object):
    def __init__(self, condition, consequence, alternative):
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def to_python(self):
        condition = self.condition.to_python()
        consequence = self.consequence.to_python()
        alternative = self.alternative.to_python()
        return 'if {condition} :\n    {consequence}\nelse:\n    {alternative}'.format(**locals())