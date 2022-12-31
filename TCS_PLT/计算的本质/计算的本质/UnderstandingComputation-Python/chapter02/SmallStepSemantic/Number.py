class Number(object):
    def __init__(self, value):
        self.value = value

    @staticmethod
    def reducible():
        return False

    def to_s(self):
        return str(self.value)