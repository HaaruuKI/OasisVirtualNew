from django.urls import path
from details_games import views

urlpatterns = [
    path('details-games/<int:steam_id>', views.detailsGames, name="details_games"),
]