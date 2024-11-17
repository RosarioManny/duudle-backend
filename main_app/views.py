from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Word
from django.contrib.auth.models import User
from .serializers import UserSerializer, GameSerializer
# Authu
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.g
class Home(APIView):
  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

class GameDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  fields = '__all__'

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })
    
    
  
class LoginView(APIView):
  

  
# view for word
class WordList(generics.ListCreateAPIView):
  queryset = Word.abjects.all()
  serializer_class = WordSerializer
  
  
class WordDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Word.objects.all()
  serializer_class = WordSerializer
  lookup_field = 'id'
  
  
class WordGame(generics.CreateAPIView):
  serializer_class = GameSerializer
 
  
  def get_object(self):
    word_id = self.kwargs['word_id']
    word = Word.objects.get(pk=word_id)
    game = Game.objects.filter(word=word).first()
    return game
  
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
