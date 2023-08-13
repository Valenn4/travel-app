from django import forms
from .models import LivingRoom
class FormNewLivingRoom(forms.ModelForm):

    class Meta:
        model = LivingRoom
        fields = ["name", "nacionality"]