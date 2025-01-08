import os
import sys
import django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vpn.settings')
django.setup()
import grpc
from concurrent import futures
from vpn.proto import vpn_pb2, vpn_pb2_grpc
from vpn.grpc_services import UserService

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vpn_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    server.add_insecure_port("[::]:50051")
    print("running port 50051")

    try:
        server.start()
        print("server running")
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("server stop")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    server()