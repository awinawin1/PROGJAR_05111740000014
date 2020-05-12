# Tugas 10

Lapran di file Tugas10_Risky Aswi Narni_05111740000014.pdf

Jalankan async_server.py pada port 9002, 9003, 9004, 9005 (lihat pada BackendList)
![alt text](Gambar/3.png)

Jalankan file lb.py, jalankan di port 44444
![alt text](Gambar/5.png)

Jalankan browser, akseslah http://localhost:44444/page.html
![alt text](Gambar/1.png)

Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian
![alt text](Gambar/2.png)

Tabel pembanding dengan async_server dengan server_thread_http dengan Asyncronus Server Dengan Load Balance
![alt text](Gambar/tabel.png)
 

Hasil SS performance test Asyncronus Server Dengan Load Balance
- ab -n 1000 -c 1 -r http://127.0.0.1:44444/
![alt text](Gambar/m1.png)
- ab -n 1000 -c 10 -r http://127.0.0.1:44444/
![alt text](Gambar/m10.png)
- ab -n 1000 -c 50 -r http://127.0.0.1:44444/
![alt text](Gambar/m50.png)
- ab -n 1000 -c 100 -r http://127.0.0.1:44444/
![alt text](Gambar/m100.png)
- ab -n 1000 -c 150 -r http://127.0.0.1:44444/
![alt text](Gambar/m150.png)



