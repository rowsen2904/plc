from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(attrs={
      'class' : 'form-control',
      'autofocus' : True
    }), 
    required=True)
    
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={
    'class' : 'form-control'
    }), 
    required=True)