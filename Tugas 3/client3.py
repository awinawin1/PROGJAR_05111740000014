import logging
import requests
import threading
from datetime import datetime
import os

def download_gambar(url=None,nama=None):
    if (url is None):
        return False
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = nama
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi},Diunduh pada waktu = {current_time} ")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':

    threads = []

    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/z0dszHm0jds6LudgG2Ghkc5f5ro=/0x0:999x666/750x500/data/photo/2020/03/04/5e5f3232e3f5f.jpg','1',))
    threads.append(t)
    t = threading.Thread(target=download_gambar, args=('https://asset.kompas.com/crops/Bs1bR-MAnGIUgy_iM1VQy1CMuD8=/3x0:988x657/750x500/data/photo/2018/09/21/1515242984.jpg','2',))
    threads.append(t)

    for thr in threads:
        thr.start()
