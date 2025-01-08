import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import grpc
from vpn.proto import vpn_pb2, vpn_pb2_grpc

def jalan():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = vpn_pb2_grpc.UserServiceStub(channel)

        try:
            request = vpn_pb2.Empty()
            response = stub.GetDataPengguna(request)

            print("response server:")
            for pengguna in response.users:
                print(f"ID: {pengguna.id}, Username: {pengguna.nama.username}, Email: {pengguna.email}, No HP: {pengguna.no_hp}")
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")

if __name__ == "__main__":
    jalan()