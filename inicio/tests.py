# import os
# import json
# from steam_web_api import Steam

# KEY = os.environ.get("STEAM_API_KEY")

# list_game = [1245620,570,1151340,2519060,495420]
# steam = Steam(KEY)

# for game in list_game:
#     game_id = game
#     game = steam.apps.get_app_details(game)
#     name_game = game[str(game_id)]["data"]["name"]
#     img_game = game[str(game_id)]["data"]["header_image"]

#     print(name_game)
#     print(img_game)

# def combinar_listas_en_diccionario(lista_claves, lista_valores):
#   diccionario_combinado = dict(zip(lista_claves, lista_valores))
#   return diccionario_combinado

# # Ejemplo de uso
# claves = ["nombre", "edad", "ciudad"]
# valores = ["Juan", 30, "Nogales"]

# diccionario_resultado = combinar_listas_en_diccionario(claves, valores)
# print(diccionario_resultado["nombre"])  # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Nogales'}

# lista = [1245620,570,1151340]
# sublista = lista[1:]
# for i in sublista:
#     print(i) 


diccionario = {
    10: 100,
    20: 300,
    30: 350,
    40: 475,
    50: 525
}

clave = 100

if clave in diccionario:
    print(f'La clave {clave} está y el valor asociado es {diccionario[clave]}')
else:
    print(f'{clave} no está en el diccionario')  # en este ejemplo esto no puede suceder
