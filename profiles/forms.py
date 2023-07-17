from django import forms
from .models import UserProfile

class FormNewTravel(forms.Form):
    location = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    image = forms.ImageField()

class FormAddImage(forms.Form):
    image = forms.ImageField()

class FormChangeUser(forms.ModelForm):
    image_portate = forms.ImageField(max_length=None, required=False)
    image_profile = forms.ImageField(max_length=None, required= False)
    class Meta:
        model = UserProfile
        fields = ['image_portate', 'image_profile', 'description', 'nacionality']
