from django.shortcuts import render,redirect
import os
from steam_web_api import Steam

# Create your views here.
def index (request):
    KEY = os.environ.get("STEAM_API_KEY")

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
    return render(request,"index.html",contexto)

def log_in (request):
    return render(request, "log_in.html")

def details_game(request):
    if request.method == 'POST':
        steam_id = request.POST['steamid']
    
    KEY = os.environ.get("STEAM_API_KEY")
    steam = Steam(KEY)

    game_search = steam.apps.search_games(str(steam_id))
    price_game = game_search["apps"][0]["price"]

    game = steam.apps.get_app_details(str(steam_id))
    game_rec = game[str(steam_id)]["data"]
    name_game = game_rec["name"]
    img_game = game_rec["header_image"]
    description_game = game_rec["short_description"]
    description_game_long = game_rec["detailed_description"]


    if "dlc" in game[str(steam_id)]["data"]:
        dlc_game = game[str(steam_id)]["data"]["dlc"]
        name_dlc_list = []
        img_list_dlc = []
        price_list_dlc = []
        
        try: 
            if dlc_game != "": 
                for dlc in dlc_game:
                    dlc_game_search = steam.apps.search_games(str(dlc))
                    game_dlc = steam.apps.get_app_details(str(dlc))[str(dlc)]
                    name_dlc = game_dlc["data"]["name"]
                    img_dlc = game_dlc["data"]["capsule_image"]
                    price_dlc = dlc_game_search["apps"][0]["price"]
                    
                    name_dlc_list.append(name_dlc)
                    img_list_dlc.append(img_dlc)
                    price_list_dlc.append(price_dlc)
                lista_zip =zip(name_dlc_list,img_list_dlc,price_list_dlc)
            else:
                print("No hay dlc")
        except Exception as e:
            print("Error al obtener DLC",e)
        # print ("si exite")
    else:                                                                                                                                                                                     
        lista_zip = ""
        print ("La palabra no se encuentra")
    
    contexto = {"name": name_game, "img":img_game,"price":price_game,"desc": description_game, "dlc": lista_zip, "desc_long":description_game_long}
    return render(request, "details_game.html",contexto)

def more_games(request):
    return render(request, "more_games.html")