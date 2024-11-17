from django.urls import path
from .views import Home, GameDetails
# CreateUserView, LoginView, VerifyUserView, 

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('users/register/',CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refesh'),
  path('/games/<int:game_id>/', GameDetails.as_view(), name='game-details'),
]