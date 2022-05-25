from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
]
