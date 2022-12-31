class DoNothing(object):
    @staticmethod
    def to_s():
        return 'do_nothing'

    def __eq__(self, other):
        return isinstance(other, DoNothing)

    @staticmethod
    def reducible():
        return False
