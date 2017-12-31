import socket

from ClientThread import ClientThread

LOCALHOST = "127.0.0.1"
PORT = 8886
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', PORT))

while True:
    server.listen(5)
    clientsock, clientAddress = server.accept()
    if clientsock is not None:
        newthread = ClientThread(clientAddress, clientsock)
        newthread.daemon = True
        newthread.start()
