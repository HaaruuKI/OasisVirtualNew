from django.shortcuts import render,redirect
import os
from steam_web_api import Steam # type: ignore

KEY = os.environ.get("STEAM_API_KEY")

def main(request):
    list_steam_id = [1245620,570,1151340,2519060,495420,1509960]
    steam = Steam(KEY)
    list_game_name= []
    list_game_img = []
    list_steamid = []
    
    for game in list_steam_id:
        game_id = game
        game = steam.apps.get_app_details(game)
        name_game = game[str(game_id)]["data"]["name"]
        img_game = game[str(game_id)]["data"]["header_image"]
                
        list_game_name.append(name_game)
        list_game_img.append(img_game)

    for steamid in list_steam_id:
        list_steamid.append(steamid)
   
    stream_id = list_steamid
    img = list_game_img   
    
    contexto = {'listas': zip(stream_id,img)}
    return render(request,"main.html",contexto)