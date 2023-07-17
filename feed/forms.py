from django import forms
from profiles.models import Message

class FormNewMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']