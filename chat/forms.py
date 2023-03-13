from django import forms

from .models import Chat

class ChatForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'autofocus' : True
    }))

    img = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class' : 'form-control',
    }))

    class Meta:
        model = Chat
        fields = ['message', 'img',]