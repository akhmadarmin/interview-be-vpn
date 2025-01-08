from vpn.proto import vpn_pb2, vpn_pb2_grpc
from app_vpn.models import DataPengguna
from django.contrib.auth.models import User

class UserService(vpn_pb2_grpc.UserServiceServicer):
    def GetDataPengguna(self, request, context):
        data_sementara = DataPengguna.objects.select_related('nama').all()
        
        listkosong_user = []
        for pengguna in data_sementara:
            user_message = vpn_pb2.User(
                id=pengguna.nama.id,
                username=pengguna.nama.username
            )
            pengguna_message = vpn_pb2.DataPengguna(
                id=pengguna.id,
                nama=user_message,
                email=pengguna.email,
                no_hp=pengguna.no_hp if pengguna.no_hp else 0
            )
            listkosong_user.append(pengguna_message)
        return vpn_pb2.DataPenggunaList(users=listkosong_user)
