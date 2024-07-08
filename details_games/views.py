from django.shortcuts import render
import os 
from steam_web_api import Steam # type: ignore

KEY = os.environ.get("STEAM_API_KEY")

# Create your views here.
def detailsGames(request):
    if request.method == 'POST':
        steam_id = request.POST['steamid']
    
    steam = Steam(KEY)

    game_search = steam.apps.search_games(str(steam_id))
    price_game = game_search["apps"][0]["price"]

    game = steam.apps.get_app_details(str(steam_id))
    game_rec = game[str(steam_id)]["data"]
    name_game = game_rec["name"]
    img_game = game_rec["header_image"]
    description_game = game_rec["short_description"]
    description_game_long = game_rec["detailed_description"]
    lenguages = game_rec.get("supported_languages", "No disponible")
    

    pc_requirements = game_rec.get("pc_requirements", {})
    mac_requirements = game_rec.get("mac_requirements", {})
    linux_requirements = game_rec.get("linux_requirements", {})

    pc_requirement_minimum = pc_requirements.get("minimum", "No disponible")
    pc_requirement_recommended = pc_requirements.get("recommended", "No disponible")
    mac_requirement_minimum = mac_requirements.get("minimum", "No disponible")
    mac_requirement_recommended = mac_requirements.get("recommended", "No disponible")
    linux_requirement_minimum = linux_requirements.get("minimum", "No disponible")
    linux_requirement_recommended = linux_requirements.get("recommended", "No disponible")
    
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
    else:                                                                                                                                                                                     
        lista_zip = ""
    
    contexto = {"name": name_game, "img":img_game,"price":price_game,"desc": description_game, "dlc": lista_zip, "desc_long":description_game_long,"pc_minimum":pc_requirement_minimum,"pc_recommended":pc_requirement_recommended,"mac_minimum":mac_requirement_minimum,"mac_recommended":mac_requirement_recommended,"linux_minimum":linux_requirement_minimum,"linux_recommended":linux_requirement_recommended, "lenguage": lenguages}
    return render(request, "details_game.html",contexto)
