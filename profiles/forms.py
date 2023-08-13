from django import forms
from .models import UserProfile, Publication, Trip

class FormNewTravel(forms.ModelForm):
    image = forms.ImageField(required=True)
    class Meta:
        model = Trip
        fields = ['location', 'title']

class FormAddImage(forms.Form):
    image = forms.ImageField()

class FormChangeUser(forms.ModelForm):
    image_portate = forms.ImageField(max_length=None, required=False)
    image_profile = forms.ImageField(max_length=None, required= False)
    class Meta:
        model = UserProfile
        fields = ['image_portate', 'image_profile', 'description', 'nacionality']


class FormNewMessage(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['message','location']