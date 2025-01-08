from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.response import Response

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