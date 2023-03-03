from django import forms

from .models import Chat

class ChatForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'autofocus' : True
    }))

    class Meta:
        model = Chat
        fields = '__all__'