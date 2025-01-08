from django.urls import path 
from .views import * 

urlpatterns = [
    path('', VpnProject3View.as_view(), name='project-vpn3')
]