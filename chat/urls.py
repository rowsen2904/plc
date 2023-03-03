from django.urls import path

from . import views 

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('clean/', views.cleanChat, name='clean_chat'),
    path('deletemessage/<str:id>/', views.deleteMessage, name='delete'),
]