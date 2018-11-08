from subprocess import Popen, PIPE

"""
Missing methods:
 - send message
 - disconnect user
 - dispose
"""


class ServerTestUtilities(object):
    @staticmethod
    def start_server():
        return Popen(r"py C:\Users\arek_\PycharmProjects\Communicator1\chat_server.py", shell=False, stdout=PIPE, stdin=PIPE, stderr=PIPE)


class ClientTestUtilities(object):

    @staticmethod
    def start_client(host, port):
        return Popen(r"py C:\Users\arek_\PycharmProjects\Communicator1\chat_client.py {} {}".format(host, port), shell=False, stdout=PIPE, stdin=PIPE, stderr=PIPE)


class CoreTestUtilities(object):

    @staticmethod
    def read_console(process):
        return process.stdout.readline()

    @staticmethod
    def write_to_console(process, text):
        process.stdin.write("{}\n".format(text))
