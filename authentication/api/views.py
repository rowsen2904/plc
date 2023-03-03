from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

class AuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        context = {
            'user' : str(request.user),
            'auth' : str(request.auth),
        }

        return Response(context)