from django.urls import path
from .views import Home, CreateUserView, LoginView, VerifyUserView, GameDetails, WordList, WordDetail, WordGame, GameList, DrawingList


urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('users/register/',CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refesh'),
  path('games/', GameList.as_view(), name='game-list'),
  path('games/<int:game_id>/', GameDetails.as_view(), name='Game-Details'),
  path('words/', WordList.as_view(), name='word-list'),
  path('words/<int:id>/', WordDetail.as_view(), name='word-list'),
  path('words/<int:id>/game', WordGame.as_view(), name='Word-Game'), 
  path('drawings/', DrawingList.as_view(), name='drawing-list'), 
]