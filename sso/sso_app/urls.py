from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('validate/', TokenValidationView.as_view(), name='validate'),
    path('logout/', LogoutGlobalView.as_view(), name='logout'),
    path('validasi-password/', views.validasi_password, name='validasi-password'),
]