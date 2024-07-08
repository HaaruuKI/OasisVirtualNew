from django.urls import path
from details_games import views

urlpatterns = [
    path('details-games', views.detailsGames, name="details_games"),
    # path('login/', views.log_in, name="login"),
    # path('datails/', views.details_game, name="details"),
    # path('moreGames/', views.more_games, name="moreGames"),
    # path('register/',views.register, name="register")
]