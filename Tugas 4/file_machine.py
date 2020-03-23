from file import Dire
import json
import logging
import base64
#TUGAS NO2
p = Dire()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                nama = cstring[1].strip()
                file = cstring[2].strip()

                print(nama)
                print(file.encode())
                print("Upload")
                p.upload_data(nama,file.encode())
                print("Selesai")

                return "OK"
            elif (command=='list'):
                logging.warning("list")
                print("list")
                hasil = p.list_data()
                dict = {"status":"succes","data":hasil}

                #print(hasil)
                return json.dumps(dict)
            elif (command=='download'):
                logging.warning("download")
                nama = cstring[1].strip()
                print("masuk")
                hasil = p.download_data(nama)
                #print(hasil.decode())
               # hasil = hasil.decode
                return hasil[0]
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = FileMachine()
    input = "coba.txt"

    hasil = pm.proses("list")
    print(hasil)
