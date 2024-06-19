from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.log_in, name="login"),
    path('datails/', views.details_game, name="details"),
    path('moreGames/', views.more_games, name="moreGames"),
]