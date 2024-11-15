from django.db import models
from django.contrib.auth.models import User

# Word Model
DIFFICULTY_CHOICES = (
  ('easy', 'Easy'),
  ('medium', 'Medium'),
  ('hard', 'Hard'),
)

class Word(models.Model):
  prompt = models.CharField(max_length=100)
  difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')

class Game(models.Model):
  winner = models.BooleanField() # <--- True
  current_word = models.ManyToManyField(Word) #<--- Later Pass in Word Model
  user = models.OneToOneField(User, on_delete=models.CASCADE) # <---- Later pass in User
  created_at = models.DateTimeField(auto_now_add=True) # <--- Auto Adds a Timestapmp of When game was created. 

class Drawing(models.Model):
  art = models.JSONField()
  game_id = models.OneToOneField