from django.urls import path
from .views import Home, GameDetails

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('/games/<int:game_id>/', GameDetails.as_view(), name='Game-Details')
]