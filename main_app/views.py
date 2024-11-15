from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game

class Home(APIView):
  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Game.objects.all()
  fields = '__all__'