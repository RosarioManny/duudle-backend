from django.contrib import admin
from .models import Game, Word, Drawing

# Register your models here.
admin.site.register(Game)
admin.site.register(Word)
admin.site.register(Drawing)