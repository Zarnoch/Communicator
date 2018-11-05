import subprocess
import os


class ServerTestUtilities:

    def startServer(self):
        FNULL = open(os.devnull, 'w')
        args = "chat_server.py"
        subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

    def startClient(self, host, port):
        FNULL = open(os.devnull, 'w')
        args = "chat_server.py {} {}".format(host, port)
        subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

