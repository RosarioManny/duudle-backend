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

  def get_queryset(self):
    user = self.request.user
    return Game.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    word_associated_with_game = Word.objects.include(id__in=instance.word.all())
    word_serializer = WordSerializer(word_associated_with_game, many=True)

    return Response({
      'game': serializer.data,
      'word_associated_with_game': word_serializer.data    
    })
  
  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    is_result = self.get_object()
    # game.result
    if Drawing.prediction == 'PASS':
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
  # fields = '__all__'
  
# The Word and The Game it belongs too
class WordGame(generics.RetrieveAPIView):
  serializer_class = GameSerializer
  
  def get_object(self):
    word_id = self.kwargs['id']
    word = Word.objects.get(pk=word_id) #<--- word.prompt?
    game = Game.objects.filter(word=word).first() #<--- Will only pull the first word. Below is code that could randomize the choice. 
    # max_id = Game.objects.latest('id').id 
    # random_id = random.randint(1, max_id)
    # random_object = Game.objects.filter(id=random_id).first()
    return game

class AddDrawingToGame(APIView):
  serializer_class = DrawingSerializer # <------ may need to add another drawing view

  def post(self, request, game_id, drawing_id):
    game = Game.objects.get(id=game_id)
    drawings = Drawing.objects.get(id=drawing_id)
    # game.drawings.add(drawing)
    return Response({'message': f'Drawing {drawings.id} added to Game {game.id}'})


