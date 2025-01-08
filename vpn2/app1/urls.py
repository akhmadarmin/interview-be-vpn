from django.urls import path 
from .views import * 

urlpatterns = [
    path('', VpnProject2View.as_view(), name='project-vpn2')
]
