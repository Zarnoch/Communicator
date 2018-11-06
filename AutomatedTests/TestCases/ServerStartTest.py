import AutomatedTests.Core
import AutomatedTests.TestScenario
from AutomatedTests.TestScenario import Assumption, TestScenario



class StartServerTest(TestScenario):
    serverStarted = False


    def PrepareAssumptions(self):
        self.assumptions.append(Assumption(1, "Open connection", "Not tested"))
        self.assumptions.append(Assumption(2, "Open connection", "Not tested"))

    def Execution(self):
        AutomatedTests.Core.ServerTestUtilities.startServer()
        if('cos z konsoli' == "os oczekiwane"):
            serverStarted = True

    def CheckResults(self):
        self.assumptions[0].result = "Pass" if self.serverStarted else "Fail"