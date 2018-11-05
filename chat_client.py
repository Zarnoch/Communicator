import socket
import select
import msvcrt
import sys


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python chat_client.py hostname port")
        sys.exit()

    host = "localhost" #sys.argv[1]
    port = 8888 #int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except:
        print("Unable to connect to server")
        sys.exit()

    print("Connected to server, start typing")
    '''nick = input("Write you nick: ")
    s.send(("<USER NICK {}>".format(nick)).encode())'''

    prompt()

    while True:
        socket_list = [sys.stdin, s]

        read_sockets = select.select([s], [], [], 1)[0]

        if msvcrt.kbhit():
            read_sockets.append(sys.stdin)

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print("\nDisconnected from server")
                    sys.exit()
                else:
                    sys.stdout.write("{}\r".format(data.decode()))
                    prompt()
            else:
                msg = sys.stdin.readline()
                s.send(msg.encode())
                prompt()
