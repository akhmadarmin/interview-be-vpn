from django.urls import path
from .views import CustomTokenObtainPairView, TokenValidationView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('validate/', TokenValidationView.as_view(), name='validate'),
 