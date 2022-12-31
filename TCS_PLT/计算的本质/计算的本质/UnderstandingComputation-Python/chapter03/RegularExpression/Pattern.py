class Pattern(object):
    def bracket(self, outer_precedence):
        if self.precedence < outer_precedence:
            return '(' + self.to_s() + ')'
        else:
            return self.to_s()

    def __str__(self):
        return '/' + self.to_s() + '/'

    def matches(self, string):
        return self.to_nfa_design().accepts(string)
