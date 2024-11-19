from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Game, Word, Drawing
from .serializers import UserSerializer, GameSerializer, WordSerializer, DrawingSerializer


class Home(APIView):

  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv  USER VIEWS  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
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
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv  GAME VIEWS  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class GameList(generics.ListCreateAPIView):
  queryset = Game.objects.all()
  serializer_class = GameSerializer


class GameDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  fields = '__all__'
  lookup_field = 'id'
  serializer_class = GameSerializer

  # def get_queryset(self):
  #   user = self.request.user
  #   return Game.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    word_associated_with_game = Word.objects.filter(id__in=instance.word.all())
    word_serializer = WordSerializer(word_associated_with_game, many=True)

    return Response({
      'game': serializer.data,
      'word_associated_with_game': word_serializer.data  
    })
  
  def partial_update(self, request, *args, **kwargs):
    # Get the game object by game_id from the URL
    game = self.get_object()

    # Check if "word_id" is in the request data
    word_id = request.data.get('word')

    if word_id:
        # If word_id is provided, handle word update and difficulty assignment
        try:
            word = Word.objects.get(id=word_id)
            
            # Update the game's associated word
            game.word.set([word])
            
            # Automatically update the game's difficulty to match the word's difficulty
            game.difficulty = word.difficulty
            game.result = False
            game.save()

        except Word.DoesNotExist:
            return Response({"error": "Word not found."}, status=status.HTTP_404_NOT_FOUND)

    # If "word_id" is not in the request data, process the normal PATCH update
    serializer = self.get_serializer(game, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  # Save other changes to the game
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # def partial_update(self, request, *args, **kwargs):
  #   # Get the game object by game_id from URL
  #   game = self.get_object()

  #   # Handle the word update based on the word_id passed in the request data
  #   word_id = request.data.get('word')
  #   if word_id:
  #       try:
  #           word = Word.objects.get(id=word_id)
  #           game.word.set([word])  # Update the associated word
  #       except Word.DoesNotExist:
  #           return Response({"error": "Word not found."}, status=status.HTTP_404_NOT_FOUND)

  #   # Handle other fields in the request and update the Game instance
  #   serializer = self.get_serializer(game, data=request.data, partial=True)
  #   if serializer.is_valid():
  #       serializer.save()
  #       return Response(serializer.data, status=status.HTTP_200_OK)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv  WORD VIEWS  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class WordList(generics.ListCreateAPIView):
  queryset = Word.objects.all()
  serializer_class = WordSerializer
  
class WordDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Word.objects.all()
  serializer_class = WordSerializer
  lookup_field = 'id'
  

class WordGame(generics.CreateAPIView):
  serializer_class = GameSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    user = self.request.user
    
    word_id = self.kwargs['id']
    word = Word.objects.get(pk=word_id)
    serializer.save(user=user,word=[word])
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv  DRAWING VIEWS  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class DrawingList(generics.ListCreateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer

  def post(self, request, *args, **kwargs):
    game_id = kwargs.get('id') 
    game = Game.objects.get(id=game_id)  

    drawing_data = request.data.copy()  
    drawing_data['game'] = game.id   

    serializer = self.get_serializer(data=drawing_data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)

    return Response(serializer.data, status=status.HTTP_201_CREATED)



# class ClearDrawings(APIView):
#     def delete(self, request, *args, **kwargs):
#         game_id = kwargs.get('id')  # Get game ID from URL
#         try:
#             # Delete all drawings associated with the given game
#             drawings_deleted, _ = Drawing.objects.filter(game_id=game_id).delete()
#             return Response(
#                 {"message": f"Successfully cleared {drawings_deleted} drawings for game {game_id}."},
#                 status=status.HTTP_200_OK,
#             )
#         except Game.DoesNotExist:
#             return Response(
#                 {"error": "Game not found."},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
            
            
            
# from django.urls import path
# from .views import DrawingList, ClearDrawings

# urlpatterns = [
#     path('games/<int:id>/drawings/', DrawingList.as_view(), name='drawing-list'),
#     path('games/<int:id>/drawings/clear/', ClearDrawings.as_view(), name='clear-drawings'),
# ]


# DELETE /games/1/drawings/clear/