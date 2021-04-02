import requests
import Player
import random
import sympy

api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña', 'llave'])


def library_right(player): # Criptograma
  # castigo = 1 vida por partida perdida, award = api.json()[1]["objects"][2]["game"]["award"], preguntas, alfabetos
  if api.json()[1]["objects"][2]["game"]["requirement"] in player.inventory: # Chequear si tiene el requirement

    print(f'\n-------------------------------------------\n{(api.json()[1]["objects"][2]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

    n = random.randint(0,len(api.json()[1]["objects"][2]["game"]["questions"]) - 1)

    alfabeto_ordenado_largo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    desplazamiento = api.json()[1]["objects"][2]["game"]["questions"][n]["desplazamiento"]
    print('el desplazamiento es', desplazamiento)
    alfabeto_desplazado = []

    for x in range(26):
      
      print(alfabeto_ordenado_largo[x])
      alfabeto_desplazado.append(alfabeto_ordenado_largo[x + desplazamiento])

    print(alfabeto_desplazado)
    # while True:
      
    #   mensaje_original = list((api.json()[1]["objects"][2]["game"]["questions"][n]["question"]).lower())

      #cifrar mensaje
      #mensaje_cifrado = 

  else:
    print(api.json()[1]["objects"][2]["game"]["message_requirement"])

library_right(emilio)