from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Drawing, Word

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password']
    )

    return user 

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(read_only=True)
  word = WordSerializer(many=True, read_only=True)

  class Meta:
    model = Game
    fields = '__all__'
