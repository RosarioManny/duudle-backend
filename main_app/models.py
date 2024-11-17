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
  result = models.BooleanField(default=False) # <--- False
  word = models.ManyToManyField(Word) #<--- Later Pass in Word Model
  user = models.OneToOneField(User) # <---- Later pass in User
  drawing= models.CharField() # <------- Drawing model ?
  created_at = models.DateTimeField(auto_now_add=True) # <--- Auto Adds a Timestapmp of When game was created. 
  difficulty = models.CharField(
    choices=DIFFICULTY_CHOICES, 
    defualt=DIFFICULTY_CHOICES[0][0]
    )

class Drawing(models.Model):
  game_id = models.OneToOneField(Game)
  art = models.JSONField()
  # guess = models.CharField()

