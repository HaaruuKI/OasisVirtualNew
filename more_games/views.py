from django.shortcuts import render
import os
from steam_web_api import Steam # type: ignore

KEY = os.environ.get("STEAM_API_KEY")

def moreGames(request):
    steam = Steam(KEY)
    query = request.GET.get('q')
    # print(query)

    steam_app = steam.apps.search_games(str(query))
    steam_app_list = steam_app["apps"]

    name_game_list = []
    img_game_list = []
    for i in range(len(steam_app_list)):
        list_id = steam_app["apps"][i]
        name_game = list_id["name"]
        img_game = list_id["img"]  

        name_game_list.append(name_game)
        img_game_list.append(img_game)

    contexto = {"lista": zip(name_game_list,img_game_list)}
    return render(request,'more_games.html',contexto)