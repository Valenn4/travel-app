from django.urls import path
from .views import register
from django.contrib.auth.views import LogoutView
from .views import LoginView
from .forms import FormLogin
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', LoginView.as_view(
        template_name='authentication/login.html',
        authentication_form=FormLogin
    ), name="auth_login"),
    path('auth/logout/', LogoutView.as_view(), name="auth_logout")
]