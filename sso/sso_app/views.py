from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class TokenValidationView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({'message': 'Token valid', 'response': response.data})

class LogoutGlobalView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "ambil token refresh"}, status=400)
            
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout berhasil, token blacklist."}, status=200)
        except TokenError:
            return Response({"error": "Token sudah diblacklist."}, status=400)

@api_view(['POST'])
def validasi_password(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "harus pakai user dan password."}, status=400)

    try:
        user = User.objects.get(username=username)

        if not check_password(password, user.password):
            raise AuthenticationFailed("Password tidak bisa.")

        return Response({"message": "Password berhasil."}, status=200)

    except User.DoesNotExist:
        return Response({"error": "User salah atau tidak ada."}, status=404)
    except AuthenticationFailed as e:
        return Response({"error": str(e)}, status=401)
    except Exception as e:
        return Response({"error": f"Ada Error: {str(e)}"}, status=500)