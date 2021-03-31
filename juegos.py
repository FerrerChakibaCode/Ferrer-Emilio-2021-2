import requests
import random

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'

# Preguntas sobre Python
def lab_left(player):
  if "cable_hdmi" in player.inventory:
    print(f'\n-------------------------------------------\n{api.json()[0]["objects"][1]["game"]["name"]}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][1]["game"]["rules"]}.\n')
    
    n = random.randint(0,1) #TODO Descifrar cómo responder la pregunta 0 del lab_left
    
    if n == 0:
      
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_2"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_3"]]
      print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])
      # str = "tengo en mi cuenta 50,00 $"
      # str = str.split()
      # str = [int(str[i]) for i in range(len(str)) if (str[i].replace(",",".")).isnumeric()]
      user_answer = input("Seleccione 'p' si desea una pista. Si no quiere una pista, escriba su respuesta.\n").lower()
      if player.clues > 0:
        if user_answer == 'p' and player.clues > 0 and len(pistas) > 0:
          print(pistas[0])
          pistas.pop(0)
          print(f"\nLe quedan {player.clues} cantidad de pistas, si desea otra pista, seleccione 'p'")
          
    else:
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"]]
      
      print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])
      
      while True:
        user_answer = input("Seleccione 'p' si desea una pista. Si no quiere una pista, escriba su respuesta.\n").lower()
        if user_answer == 'p' and player.clues > 0 and len(pistas) > 0:
          print(pistas[0])
          pistas.pop(0)
          player.clues -= 1
          print(f"\nLe quedan {player.clues} pistas, si desea otra pista, seleccione 'p'")

        elif user_answer == 'p' and player.clues == 0:
          print('Usted no tiene más pistas...\n')

        elif user_answer == "frase = frase[::-1]":
          player.inventory.append(api.json()[0]["objects"][1]["game"]["award"])
          print('\n-------------------------------------------\nCORRECTO! Has desbloqueado el CARNET para tus siguientes retos...')
          player.show()
          break
        
        else:
          player.lives -= 0.5
          keep = input('Incorrecto! Has perdido media vida. Si desea seguir intentando responder ingrese su respuesta. Si no, ingrese (N)o\n').lower()
          if keep == 'n':
            break

  else:
    print(api.json()[0]["objects"][1]["game"]["message_requirement"])


def lab_right(player):
  if "introducir contraseña de la computadora" in player.inventory:

    print(f'\n-------------------------------------------\n{api.json()[0]["objects"][2]["game"]["name"]}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

    n = random.randint(0,2)

    pistas = [api.json()[0]["objects"][2]["game"]["questions"][n]["clue_1"], api.json()[0]["objects"][2]["game"]["questions"][n]["clue_2"], api.json()[0]["objects"][2]["game"]["questions"][n]["clue_3"]]
    
    print(api.json()[0]["objects"][2]["game"]["questions"][n]["question"])
    user_answer = input("Seleccione 'p' si desea una pista. Si no quiere una pista, escriba su respuesta.\n").lower()

  

  else:
    print(api.json()[0]["objects"][2]["game"]["message_requirement"])

    