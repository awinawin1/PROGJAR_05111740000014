import shelve
import uuid
import socket
import os
import base64
#TUGAS NO1

class Dire:
    def __init__(self):
        if not os.path.exists("Hasil"):
            os.makedirs("Hasil")
    def upload_data(self,nama=None,file=None):

        makan = file
        print(base64.decodestring(makan))
        f = open("Hasil/"+nama,"wb")
        f.write(base64.decodestring(makan))

        return True
    def download_data(self,nama=None):
        # ======Membaca file download =====
        are = []
        f = open("Hasil/" + nama, "rb")
        l =f.read()
        f.close()
        print(l)

        hasil = base64.encodestring(l)
        print(hasil)
        are.append(hasil.decode())
        print(are)

        return are

    def list_data(self):
        file_list = os.listdir("Hasil")
        f = []
        for filename in file_list:
            f.append(filename)
        return f

if __name__=='__main__':
    dire = Dire()
    input = "coba.txt"
    #ini = dire.download_data(input)
    # print(ini)
    # dire.upload_data("gambartugas.jpg")
    #dire.download_data("gambartugas.jpg")

    print(dire.list_data())


   # p.create_data("vanPersie","621235")
   # p.create_data("vanNistelroy","621236")
   # p.create_data("vanDerVaart","621237")
   # print(dire.list_data())
   # print(dire.get_data('vanbasten'))
