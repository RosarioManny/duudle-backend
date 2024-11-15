from django.shortcuts import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Game, Drawing, Word
from .serializers import UserSerializer
# Create your views here.
class Home(APIView):
 def get(self, request):
  content = {'message': 'welcome to Whataduudle'}
  return Response(content)