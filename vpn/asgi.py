"""
ASGI config for vpn project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vpn.settings')
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

import grpc
from concurrent import futures

from vpn.proto import vpn_pb2_grpc
from .grpc_services import UserService


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
vpn_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    return server

async def application(scope, receive, send):
    if scope["type"] == "http":
        await django_asgi_app(scope, receive, send)
    elif scope["type"] == "grpc":
        server = grpc_server()
        await server.handle(scope, receive, send)