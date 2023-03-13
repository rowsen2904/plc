from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.userLogin, name='login'),

    path('logout/', views.loggingout, name='logout'),

    path('register/', views.userRegister, name='register'),
]