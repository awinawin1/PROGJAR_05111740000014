
from socket import *
import socket
import threading
import logging
import time
import sys
import base64
from file_machine import FileMachine

pm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        file = (b"")
        tes = []
        while True:
           
            while True:
              #  try:

                    data = self.connection.recv(1024)

                 #   self.connection.sendall(b"hali")
                    file = file + data
                    tes.append(data)
                    bytenya = int(sys.getsizeof(data))


                #    print(b"isi = " + data)
                    if bytenya != 1057 :
                        #print(bytenya)
                      #  self.connection.sendall(b"akhitnya")

                        break
                    else :
                        #print(bytenya)
                        self.connection.sendall(b"halo")

            #print("Sudah terdapat file dengan nama yang sama")

            data = file

            if data:
                d = data.decode()

                hasil = pm.proses(d)
                hasil=hasil

                self.connection.sendall(hasil.encode())

             #   sleep(3)
            else:
                break
        self.connection.close()



class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8889))
        self.my_socket.listen(1)
        #self.my_socket.settimeout(100)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    print("Mencari Koneksi")
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()
