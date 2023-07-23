from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from profiles.models import UserProfile
from django.views.generic.edit import FormView

class FormRegister(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password1', 'password2', 'first_name', 'email']



class FormLogin(AuthenticationForm):
    error_messages = {
        'invalid_login': ("El usuario o la contraseña es incorrecto.")
    }