from django.urls import path 
from .views import * 

urlpatterns = [
    path('', VpnProject1View.as_view(), name='project-vpn1')
]
