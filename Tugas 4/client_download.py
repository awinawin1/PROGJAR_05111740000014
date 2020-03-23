import socket
import sys
import base64
import os
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)


request = "Tugas3_05111740000014_awin.pdf"
request = request.encode()
print("Mendownload file "+request.decode()+"...")
f = open(request,"wb")
file =(b"")
sock.send(request)
data = sock.recv(1024)
while True:
    file = file + data

    if sys.getsizeof(data) != 1057:

        break
    else :
        data = sock.recv(1024)

file = base64.decodestring(file)

f.write(file)
f.close()
f = open("Hasil/Tugas3_05111740000014_awin.pdf","rb")
#print(f.read())


f.close()
print("file "+request+"telah berhasil terdownload")
sock.close()
