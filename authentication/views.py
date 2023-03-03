from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .decorators import allowed_users

def userLogin(request):
  if request.user.is_authenticated:
    return redirect('chat:index')

  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user)
      return redirect('chat:index')
    else: messages.error(request, 'Username or Password filled uncorrect!')

  page = 'login'
  form = LoginForm(request.POST or None)
  context = {
    'form' : form,
    'page' : page,
  }
  return render(request, 'login.html', context)


def loggingout(request):
  logout(request)
  return redirect('chat:index')