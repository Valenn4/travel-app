from django import forms
from .models import Image

class FormNewTravel(forms.Form):
    location = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    image = forms.ImageField()