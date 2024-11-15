from django.db import models

class Game(models.Model):
    winner = models.BooleanField() # <--- True
    current_word = models.ManyToManyField() #<--- Later Pass in Word Model
    user_id = models.OneToOneField() # <---- Later pass in User
    created_at = models.DateTimeField(auto_now_add=True) # <--- Auto Adds a Timestapmp of When game was created. 
