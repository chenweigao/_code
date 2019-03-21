import socket
import sys

# create a TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
s.bind(server_address)
s.listen(5)  # backlog = 1

while True:
    print("waiting for connections...")
    # accept() -> (socket object, address info)
    connection, client_address = s.accept()

    try:
        print('connection from: ', client_address)

        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from ', client_address)
                break

    finally:
        connection.close()
