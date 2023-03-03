from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.AuthToken.as_view()),
    path('token/', obtain_auth_token)
]
