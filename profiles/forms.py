from django import forms

class FormNewTravel(forms.Form):
    location = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    image = forms.ImageField()