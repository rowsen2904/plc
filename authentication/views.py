from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .forms import LoginForm


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('chat:index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chat:index')
        else:
            messages.error(request, 'Username or Password filled uncorrect!')

    page = 'login'
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'authentication.html', context)


def userRegister(request):
    if request.user.is_authenticated:
        return redirect('chat:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            group = Group.objects.get(name='user')
            user.save()
            login(request, user)
            user.groups.add(group)
            return redirect('chat:index')

        messages.error(request, 'An error is occurred during registration')

    page = 'register'
    form = UserCreationForm(request.POST or None)
    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'authentication.html', context)


def loggingout(request):
    logout(request)
    return redirect('chat:index')
