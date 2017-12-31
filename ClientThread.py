import threading

from process_data import ProcessData


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.socket = clientsocket

    def run(self):
        in_data = self.socket.recv(2048).decode()
        print("received data:",in_data)
        if in_data is not None:
            data = ProcessData.process(in_data)
            print("process data: ", data)
            self.socket.sendall(bytes(data, 'utf-8'))
            self.socket.close()

