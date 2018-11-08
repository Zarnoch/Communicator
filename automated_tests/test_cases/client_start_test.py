from automated_tests.core import ServerTestUtilities, ClientTestUtilities, CoreTestUtilities
from automated_tests.test_scenario import TestScenario
from automated_tests.assumption import Assumption


class ClientServerTest(TestScenario):
    server_started = False
    client_started = False

    ip = "localhost"
    host = "8888"

    def prepare_assumptions(self):
        self.assumptions.append(Assumption(1, "Run chat server", "Not tested"))
        self.assumptions.append(Assumption(2, "Run chat client on {} and {} port".format(self.ip, self.host), "Not tested"))
        self.assumptions.append(Assumption(3, "Connect client to server", "Not tested"))

    def execute(self):
        server_process = ServerTestUtilities.start_server()
        response = CoreTestUtilities.read_console(server_process)
        if response == b'Chat server has started on port: 8888\r\n':
            self.server_started = True

        client_process = ClientTestUtilities.start_client(self.ip, self.host)
        response = CoreTestUtilities.read_console(client_process)
        if response == b'Connected to server, start typing\r\n':
            self.client_started = True

    def check_results(self):
        self.assumptions[0].result = "Pass" if self.server_started else "Fail"
        self.assumptions[1].result = "Pass" if self.client_started else "Fail"
        self.assumptions[2].result = "Pass" if self.client_started else "Fail"

