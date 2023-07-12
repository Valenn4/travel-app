from django.urls import path
from .views import register, login
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('auth/logout/', LogoutView.as_view())
]