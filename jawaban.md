** Mohon maaf tidak bisa mengimplementasikan Docker karena spesifikasi laptop kurang mendukung **

**STruktur project **

# vpn adalah project 1 dan manage.py adalah milik vpn project 1
# app_vpn adalah app milik vpn project 1 yang berisi database contoh untuk jawaban soal pertama
# vpn2 adalah project 2
# vpn3 adalah project 3
# sso khusus untuk single sign on yang dipisahkan untuk menjaga agar project1, project2, project3 jika kelak dikembangkan tidak terganggu


# JAWABAN 

## POIN 1

- Integrasi antara gRPC dan Django.
- Komunikasi dengan stub Python (grpc_client.py).
- Reflection API untuk testing dengan grpcurl.

# running di env

# interview-be-vpn/vpn:$ uvicorn vpn.asgi:application --reload
# interview-be-vpn/vpn:$ python grpc_server.py 

- cukup menjalankan perintah uvicorn vpn.asgi:application --reload tanpa harus menjalankan django runserver

**send request**

#grpcurl -plaintext -d '{}' localhost:50051 ServicePenguna/AmbilUser
- atau dengan running file grpc_client.py 

#python grpc_client.py 

-------------

## POIN 2

- jalankan project pertama (vpn) python manage.py runserver 
- jalankan project kedua (vpn2) python manage.py runserver 0.0.0.0:8001
- jalankan project ketiga (vpn3) python manage.py runserver 0.0.0.0:8002
- jalankan project sso python manage.py runserver 0.0.0.0:8003
- semua menggunakan user dan password admin:ngantuk123
- lalu send request ke sso dengan perintah 
# curl -X POST -d "username=admin&password=ngantuk123" http://127.0.0.1:8003/akses/sso/login/
- a kan menghasilkan 
- {"refresh":"..","access":"eyJhbGciOi.."}
- lalu send request lagi dengan curl 
# curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM2Mjk3Njk4LCJpYXQiOjE3MzYyOTczOTgsImp0aSI6IjA2MjFmNjNiZDRjMjQ5YzQ4ZTFjZDAwODAyODgyMzU2IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.i5PLK8-vn7jrP-jBarnpZbWj5DklIzDI2IyGMFIUoBw" http://127.0.0.1:8000/akses/app-vpn1/

# akan menghasilkan message":"sedang mengakses app1 vpn1 (project1)"}
