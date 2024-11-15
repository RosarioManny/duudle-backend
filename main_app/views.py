from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Home(APIView):
  def get(self, request):
    content = {'message': 'welcome to Whataduudle'}
    return Response(content)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
  # queryset = 
  fields = '__all__'