from django.shortcuts import generics, status, permissions
from rest_framework import generics
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
  user = User.objectsgrt(username=request.user)
  refresh = RefreshToken.for_user(request.user)
  return Response({
   'refresh': str(refresh),
   'access': str(refresh.access_token),
   'user': UserSerializer(user).data
  })