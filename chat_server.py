import socket
import select


def broadcast_data(sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message.encode())
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)


if __name__ == "__main__":
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    CONNECTION_LIST.append(server_socket)

    print("Chat server has started on port: " + str(PORT))

    while True:
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                broadcast_data(sockfd, "Client ({} {}) is online.\n".format(addr[0], addr[1]))
                print("Client ({} {}) connected.".format(addr[0], addr[1]))
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "<{}> {}".format(str(sock.getpeername()), data.decode()))
                        print("Client: {} sent message.".format((str(sock.getpeername()))))
                except:
                    broadcast_data(sock, "Client ({} {}) is offline.\n".format(addr[0], addr[1]))
                    print(sock, "Client ({} {}) is offline.".format(addr[0], addr[1]))
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    server_socket.close()