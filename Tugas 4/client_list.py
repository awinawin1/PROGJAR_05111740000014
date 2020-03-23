import socket
import sys
from time import sleep
import base64
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)


pesan = (b"list")

sock.send(pesan)
data = sock.recv(1024)
print("List: \n \n"+data.decode())
#data = sock.recv(1024)

#print(data)
sock.close()
