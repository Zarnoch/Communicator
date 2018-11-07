from automated_tests.core import ServerTestUtilities
from automated_tests.test_scenario import TestScenario
from automated_tests.assumtion import Assumption


class StartServerTest(TestScenario):
    server_started = False

    def prepare_assumptions(self):
        self.assumptions.append(Assumption(1, "Open connection", "Not tested"))
        self.assumptions.append(Assumption(2, "Open connection", "Not tested"))

    def execute(self):
        # ServerTestUtilities.start_server()
        if 'cos z konsoli' == "os oczekiwane":
            self.server_started = True

    def check_results(self):
        self.assumptions[0].result = "Pass" if self.server_started else "Fail"
