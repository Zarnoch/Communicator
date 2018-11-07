import subprocess
import os


class ServerTestUtilities(object):
    """
    Missing methods:
     - send message
     - disconnect user
     - dispose
    """
    @staticmethod
    def start_server():
        fnull = open(os.devnull, 'w')
        args = "chat_server.py"
        subprocess.call(args, stdout=fnull, stderr=fnull, shell=False)

    @staticmethod
    def start_client(host, port):
        fnull = open(os.devnull, 'w')
        args = "chat_server.py {} {}".format(host, port)
        subprocess.call(args, stdout=fnull, stderr=fnull, shell=False)

