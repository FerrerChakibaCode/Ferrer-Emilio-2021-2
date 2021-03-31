import requests
import random
import Player

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña'])
# Preguntas sobre Python
def lab_left(player):
  if "cable_hdmi" in player.inventory:
    print(f'\n-------------------------------------------\n{api.json()[0]["objects"][1]["game"]["name"]}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][1]["game"]["rules"]}.\n')
    
    n = random.randint(0,1) #TODO Descifrar cómo responder la pregunta 0 del lab_left
    
    if n == 0:
      #SI LE TOCA LA PREGUNTA 0
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_2"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_3"]] #Crear lista con pistas para esa pregunta

      while True:
        print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])
        user_answer = input("Seleccione 'p' si desea una pista.\n").lower()
        if user_answer == 'p' and player.clues > 0 and len(pistas) > 0:
          print(pistas[0])
          pistas.pop(0)
          player.clues -= 1
          print(f"\nLe quedan {player.clues} cantidad de pistas, si desea otra pista, seleccione 'p'")

        elif user_answer == 'p' and (player.clues == 0 or len(pistas) == 0):
            print('No le quedan pistas...\n')

        elif user_answer == "frase = int(float(((frase.split())[-2]).replace(',','.')))" or user_answer == "int(float(((frase.split())[-2]).replace(',','.')))" or user_answer == "frase = int(float(((frase.split())[4]).replace(',','.')))" or user_answer == "int(float(((frase.split())[4]).replace(',','.')))":
          player.inventory.append(api.json()[0]["objects"][1]["game"]["award"])
          print('\n-------------------------------------------\nCORRECTO! Has desbloqueado el CARNET para tus siguientes retos...')
          player.show()
          break

        elif user_answer == '':
          break

        else:
          player.lives -= 0.5
          print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")

    else:
      ##SI LE TOCA LA PREGUNTA 0
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"]] #Crear lista con pistas para esa pregunta
      
      while True:
        print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])

        user_answer = input("Seleccione 'p' si desea una pista.\n").lower()
        if user_answer == 'p' and player.clues > 0 and len(pistas) > 0:
          print(pistas[0])
          pistas.pop(0)
          player.clues -= 1
          print(f"\nLe quedan {player.clues} pistas, si desea otra pista, seleccione 'p'")

        elif user_answer == 'p' and (player.clues == 0 or len(pistas) == 0):
          print('No le quedan pistas...\n')

        elif user_answer == "frase = frase[::-1]":
          player.inventory.append(api.json()[0]["objects"][1]["game"]["award"])
          print('\n-------------------------------------------\nCORRECTO! Has desbloqueado el CARNET para tus siguientes retos...')
          player.show()
          break
        
        elif user_answer == '':
          break

        else:
          player.lives -= 0.5
          print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")

  else:
    print(api.json()[0]["objects"][1]["game"]["message_requirement"])


def lab_right(player): #TODO en el juego donde el award sea "contraseña, verificar que se esté dando esto"
  #TODO recordar DESCONTAR VIDAS, que el loop de preguntas sea continuo, dar el award, verificar tema con las pistas
  if "contraseña" in player.inventory:

    print(f'\n-------------------------------------------\n{api.json()[0]["objects"][2]["game"]["name"]}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

    n = random.randint(0,2)

    pistas = [api.json()[0]["objects"][2]["game"]["questions"][n]["clue_1"], api.json()[0]["objects"][2]["game"]["questions"][n]["clue_2"], api.json()[0]["objects"][2]["game"]["questions"][n]["clue_3"]]
    
    

    while True:
      print(api.json()[0]["objects"][2]["game"]["questions"][n]["question"])
    
      answers = [(api.json()[0]["objects"][2]["game"]["questions"][n]["answers"][x]) for x in range (5)]
      user_answer = input("Seleccione 'p' si desea una pista.\n").lower()
      
      if user_answer == 'p' and player.clues > 0 and len(pistas) > 0:
        print(pistas[0])
        pistas.pop(0)
        player.clues -= 1
        print(f"\nLe quedan {player.clues} cantidad de pistas, si desea otra pista, seleccione 'p'")

      elif user_answer == 'p' and (player.clues == 0 or len(pistas) == 0):
          print('No le quedan pistas...\n')

      elif user_answer in answers:
        player.inventory.append(api.json()[0]["objects"][2]["game"]["award"])
        print('\n-------------------------------------------\nCORRECTO! Has desbloqueado la LLAVE para tus siguientes retos...')
        player.show()
        break
      
      elif user_answer == '':
        break

      else:
        player.lives -= 0.5
        print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")


  else: #Si no tiene la Contraseña
    print(api.json()[0]["objects"][2]["game"]["message_requirement"])

