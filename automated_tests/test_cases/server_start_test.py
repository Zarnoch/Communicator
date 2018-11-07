from automated_tests.core import ServerTestUtilities
from automated_tests.test_scenario import TestScenario
from automated_tests.assumption import Assumption

class StartServerTest(TestScenario):
    server_started = False

    def prepare_assumptions(self):
        self.assumptions.append(Assumption(1, "Open connection", "Not tested"))

    def execute(self):
        server_process = ServerTestUtilities.start_server()
        response = ServerTestUtilities.read_console(server_process)
        if response == b'Chat server has started on port: 8888\r\n':
            self.server_started = True

    def check_results(self):
        self.assumptions[0].result = "Pass" if self.server_started else "Fail"
