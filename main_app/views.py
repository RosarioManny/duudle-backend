from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Word
from .serializers import WordSerializer, GameSerializer

# Create your views here.
class Home(APIView):
  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  fields = '__all__'
  
  
  
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
  
