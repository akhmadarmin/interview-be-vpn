** Mohon maaf tidak bisa mengimplementasikan Docker karena spesifikasi laptop kurang mendukung **

**STruktur project **

# vpn adalah project 1 dan manage.py adalah milik vpn project 1
# app_vpn adalah app milik vpn project 1 yang berisi database contoh untuk jawaban soal pertama
# vpn2 adalah project 2
# vpn3 adalah project 3
# sso khusus untuk single sign on yang dipisahkan untuk menjaga agar project1, project2, project3 jika kelak dikembangkan tidak terganggu


# JAWABAN 

# POIN 1

- Integrasi antara gRPC dan Django.
- Komunikasi dengan stub Python (grpc_client.py).
- Reflection API untuk testing dengan grpcurl.

# running di env

# interview-be-vpn/vpn:$ uvicorn vpn.asgi:application --reload
# interview-be-vpn/vpn:$ python grpc_server.py 

- cukup menjalankan perintah uvicorn vpn.asgi:application --reload tanpa harus menjalankan django runserver

**send request**

- grpcurl -plaintext -d '{}' localhost:50051 ServicePenguna/AmbilUser
- atau dengan running file grpc_client.py 

- python grpc_client.py 

-------------

# POIN 2

- jalankan project pertama (vpn) python manage.py runserver 
- jalankan project kedua (vpn2) python manage.py runserver 0.0.0.0:8001
- jalankan project ketiga (vpn3) python manage.py runserver 0.0.0.0:8002
- jalankan project sso python manage.py runserver 0.0.0.0:8003
- semua menggunakan user dan password admin:ngantuk123
- lalu send request ke sso dengan perintah 
- curl -X POST -d "username=admin&password=ngantuk123" http://127.0.0.1:8003/akses/sso/login/
- a kan menghasilkan 
- {"refresh":"..","access":"eyJhbGciOi.."}
- lalu send request lagi dengan curl 
- curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2Mjk3Njk4LCJpYXQiOjE3MzYyOTczOTgsImp0aSI6IjA2MjFmNjNiZDRjMjQ5YzQ4ZTFjZDAwODAyODgyMzU2IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.i5PLK8-vn7jrP-jBarnpZbWj5DklIzDI2IyGMFIUoBw" http://127.0.0.1:8000/akses/app-vpn1/

- akan menghasilkan {message":"sedang mengakses app1 vpn1 (project1)"}

- logout global 
- curl -X POST -H "Authorization: Bearer <ACCESS_TOKEN>" \
-    -d "refresh_token=<REFRESH_TOKEN>" \
-    http://127.0.0.1:8003/akses/sso/logout/	 

- jika berhasil akan menampilkan 
- >      http://127.0.0.1:8003/akses/sso/logout/
-  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
-                                 Dload  Upload   Total   Spent    Left  Speed
- 100   316  100    47  100   269    262   1500 --:--:-- --:--:-- --:--:--  1765{"message":"Logout berhasil, token blacklist."}

-------------

# Poin 3
- setelah project django sudah atau masih running 
- python manage.py runserver 0.0.0.0:8003
- dapat kirim request dengan curl 
- curl -X POST -H "Content-Type: application/json" \
-   -d '{"username": "admin", "password": "ngantuk123"}' \
-   http://127.0.0.1:8003/akses/sso/validasi-password/

- jika berhasil akan ada response 
- {"message":"Password berhasil."}
- sedangkan di server sso mengembalikan response 
- [08/Jan/2025 03:39:23] "POST /akses/sso/validasi-password/ HTTP/1.1" 200 32

- Penjelasan : 
- PBKDF2 mudah digunakan, secure, tidak perlu dependency tambahan seperti argon ataupun bcrypt, kompatibel untuk beberapa jenis apps yang cross platform
- alternatif yang rekomendasi digunakan dari PBKDF2 adalah Bcrypt yang memang sudah menjadi default django, namun Scrypt yang sudah banyak digunakan di app product fintech, insurtech dll lebih tepat, bisa disesuaikan tergantung kebutuhan jenis app nya.