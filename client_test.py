# Import socket module
import socket

# Create a socket object
s = socket.socket()

host = ''
# Define the port on which you want to connect
port = 8886

# connect to the server on local computer
s.connect((host, port))

# s.sendall(bytes("0:17681885886:test", 'utf-8'))
# s.sendall(bytes("1:test@test.com:test", 'utf-8'))
s.sendall(bytes("2:17681885886:test:new_password", 'utf-8'))
while True:
    # receive data from the server
    in_data = s.recv(2048)
    msg = in_data.decode()
    if msg is not None:
        print("from server:", msg)
        # close the connection
        s.close()
        break
