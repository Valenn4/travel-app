from django.urls import path
from .views import register
from django.contrib.auth.views import LogoutView
from .views import LoginView
urlpatterns = [
    path('register/', register),
    path('login/', LoginView.as_view(
        template_name='authentication/login.html'
    )),
    path('auth/logout/', LogoutView.as_view())
]