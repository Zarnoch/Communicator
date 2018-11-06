class TestScenario(object):
    assumptions = []

    def PrepareAssumptions(self):
        pass

    def Execution(self):
        pass

    def CheckResults(self):
        pass


class Assumption(object):
    def __init__(self, number, description, result):
        self.number = number
        self.description = description
        self.result = result