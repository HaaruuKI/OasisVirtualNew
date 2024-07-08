from django.urls import path
from more_games import views
urlpatterns = [
    path('more-games/', views.moreGames, name="more_games")
]