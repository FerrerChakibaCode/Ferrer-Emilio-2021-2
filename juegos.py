import requests
import random

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'

# Preguntas sobre Python
def lab_left(player, cable_hdmi = False):
  if cable_hdmi:
    print(f'REGLAS DEL JUEGO -> {api.json()[0]["objects"][1]["game"]["rules"]}.\n')
    
    n = random.randint(0,1) #TODO Descifrar cómo responder la pregunta 0 del lab_left
    
    if n == 0:
      
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_2"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_3"]]
      print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])
      # str = "tengo en mi cuenta 50,00 $"
      # str = str.split()
      # str = [int(str[i]) for i in range(len(str)) if (str[i].replace(",",".")).isnumeric()]
      user_answer = input("Seleccione 'p' si desea una pista. Si no quiere una pista, escriba su respuesta.\n").lower()
      while player.clues > 0:
        if user_answer == 'p': #TODO VALIDACIÓN DE LA CANTIDAD DE PISTAS QUE LE QUEDAN AL USER
          print(pistas[0])
          pistas.pop(0)
          print(f"\nLe quedan {player.clues} cantidad de pistas, si desea otra pista, seleccione 'p'") # TODO PISTAS DEL USUARIO
        
    else:
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"]]
      print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])
      user_answer = input("Seleccione 'p' si desea una pista. Si no quiere una pista, escriba su respuesta.\n").lower()
      while player.clues > 0:
        if user_answer == 'p':
          print(pistas[0])
          pistas.pop(0)
          print(f"\nLe quedan {player.clues} cantidad de pistas, si desea otra pista, seleccione 'p'")

        else:
          break
      if user_answer == "frase = frase[::-1]":
        player.inventory.append(api.json()[0]["objects"][1]["game"]["award"])
        print('\n-------------------------------------------\nCORRECTO! Has desbloqueado el CARNET para tus siguientes retos...')
        player.show()

  else:
    print(api.json()[0]["objects"][1]["game"]["message_requirement"])

