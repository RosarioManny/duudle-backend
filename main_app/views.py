from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Word
from django.contrib.auth.models import User
from .serializers import UserSerializer, GameSerializer

# Create your views here.g
class Home(APIView):
  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

class GameDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  fields = '__all__'

class CreateUserView(generics.CreateAPIView):
  
class LoginView(APIView):
  

  
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response ({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })