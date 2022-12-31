class Machine(object):
    def __init__(self, statement, environment):
        self.statement = statement
        self.environment = environment

    def step(self):
        self.statement, self.environment = self.statement.reduce(self.environment)

    def run(self):
        while self.statement.reducible():
            print(self.statement.to_s(), end=', ')
            print(dict([(k, v.value) for k, v in self.environment.items()]))
            self.step()
        print(self.statement.to_s(), end=', ')
        print(dict([(k, v.value) for k, v in self.environment.items()]))
