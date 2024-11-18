from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Word, Drawing
from django.contrib.auth.models import User
from .serializers import UserSerializer, GameSerializer, WordSerializer, DrawingSerializer
from random import random
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Authu
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# Create your views here.g
class Home(APIView):

  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

# REGISTER
class CreateUserView(generics.CreateAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer

 def create(self, request, *arg, **kwargs):
  response = super().create(request, *arg, **kwargs)
  user = User.objects.get(username=response.data['username'])
  refresh = RefreshToken.for_user(user)
  return Response({
  'refresh': str(refresh),
  'access': str(refresh.access_token),
  'user': response.data
  }) 
# LOGIN
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
  
# AUTHENTICATION
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    user = User.objects.get(username=request.user)
    refresh = RefreshToken.for_user(request.user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })
  
# Games Listed
class GameList(generics.ListCreateAPIView):
  queryset = Game.objects.all()
  serializer_class = GameSerializer

# Game Details
class GameDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  fields = '__all__'
  lookup_field = 'id'
  serializer_class = GameSerializer

  def get_queryset(self):
    user = self.request.user
    return Game.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    word_associated_with_game = Word.objects.filter(id__in=instance.word.all())
    word_serializer = WordSerializer(word_associated_with_game, many=True)

    return Response({
      'game': serializer.data,
      'word_associated_with_game': word_serializer.data  
    })
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    if instance.result == 'PASS':
      Game.result = True
    else:
      return Response('You Failed.')  

# view for word
class WordList(generics.ListCreateAPIView):
  queryset = Word.objects.all()
  serializer_class = WordSerializer
  
class WordDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Word.objects.all()
  serializer_class = WordSerializer
  lookup_field = 'id'
  
# The Word and The Game it belongs too
class WordGame(generics.CreateAPIView):
  serializer_class = GameSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    user = self.request.user
    
    word_id = self.kwargs['id']
    word = Word.objects.get(pk=word_id)
    serializer.save(user=user,word=[word])

class DrawingList(generics.ListCreateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer

  def post(self, request, *args, **kwargs):
    game_id = kwargs.get('id')  # Retrieve the game ID from the URL
    game = Game.objects.get(id=game_id)  # Get the Game object

    # Add game_id to request data
    drawing_data = request.data.copy()  # Create a mutable copy of request.data
    drawing_data['game'] = game.id  # Add the game ID to the drawing data

    # Pass the modified data to the serializer
    serializer = self.get_serializer(data=drawing_data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
