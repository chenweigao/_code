import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM for connection-oriented protocols
# SOCK_DGRAM for connectionless protocols.

server_address = ('localhost', 5000)

print('connecting to {} port {}'.format(*server_address))
s.connect(server_address)
while True:
    try:
        message = sys.stdin.readline()
        message = bytes(message, 'utf-8')
        print('sending {!r}'.format(message))
        s.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = s.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        s.close()
