from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class VpnProject3View(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "sedang mengakses app1 vpn3 (project3)"})
