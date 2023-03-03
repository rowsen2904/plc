from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Chat
from .forms import ChatForm

from authentication.decorators import allowed_users, unauthenticated_user


@login_required(login_url='/authentication/login/')
def index(request):
    forms = ChatForm()
    if request.method == 'GET':
        chats = Chat.objects.all().order_by('-created_time')
        if request.user.groups.all()[0].name != 'superadmin':
            user = 'user'
        else : user = 'admin'
        context = {
            'chats': chats,
            'forms': forms,
            'user' : user,
        }
        return render(request, 'chat/index.html', context)

    forms = ChatForm(request.POST)
    if forms.is_valid():
        message = forms.save(commit=False)
        message.username = request.user.username
        message.save()
        return redirect('chat:index')

@allowed_users(allowed_roles=['superadmin'])
def cleanChat(request):
    Chat.objects.all().delete()
    return redirect('chat:index')

@allowed_users(allowed_roles=['superadmin'])
def deleteMessage(request, id):
    message = Chat.objects.get(id=id)
    message.delete()
    return redirect('chat:index')