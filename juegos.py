import requests
import random
import Player

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña'])

def lab_left(player): # Preguntas sobre Python
  if "cable_hdmi" in player.inventory:
    print(f'\n-------------------------------------------\n{(api.json()[0]["objects"][1]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][1]["game"]["rules"]}.\n')
    
    n = (0,(len(api.json()[0]["objects"][1]["game"]["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    
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

def lab_right(player): # Adivinanzas
  #TODO en el juego donde el award sea "contraseña, verificar que se esté dando esto"

  if "contraseña" in player.inventory:

    print(f'\n-------------------------------------------\n{(api.json()[0]["objects"][2]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

    n = (0,(len(api.json()[0]["objects"][2]["game"]["questions"]))-1) # Seleccionador random de qué pregunta toca responder

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

def library_center(player): # Ahorcado
  #TODO Gráficas en simultáneo con el juego, por el amor de Dios

  print(f'\n-------------------------------------------\n{(api.json()[1]["objects"][0]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[1]["objects"][0]["game"]["rules"]}.\n')

  n = random.randint(0,(len(api.json()[1]["objects"][0]["game"]["questions"]))-1) # Seleccionador random de qué pregunta toca responder

  pistas = [api.json()[1]["objects"][0]["game"]["questions"][n]["clue_1"], api.json()[1]["objects"][0]["game"]["questions"][n]["clue_2"], api.json()[1]["objects"][0]["game"]["questions"][n]["clue_3"]]
  letras_disponibles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letras_usadas = []

  answer = (api.json()[1]["objects"][0]["game"]["questions"][n]["answer"]).lower()
  answer = list(answer) # Lista de strings de la respuesta directa del API.
  answer_displayed = ['_' for letter in answer] # La respuesta que el usuario va construyendo.
  print(api.json()[1]["objects"][0]["game"]["questions"][n]["question"])
  
  intentos = 5
  while intentos > 0:
    
    print("Seleccione la letra que escoja. Seleccione '1' si quiere una pista")
    user_answer = input("> ").lower()
    
    if user_answer == '1':
      if player.clues > 0 and len(pistas) > 0:
        print(pistas[0])
        pistas.pop(0)
      elif player.clues == 0:
        print('A usted ya no le quedan pistas')
      elif len(pistas) == 0:
        print('Ya no le quedan pistas en este ahorcado')
      else:
        print('No puede utilizar más pistas')

    if user_answer in letras_usadas:
      print(f'Esta es la lista de letras usadas: {letras_usadas}')

    if user_answer in letras_disponibles:
      letras_disponibles.pop(letras_disponibles.index(user_answer))
      letras_usadas.append(user_answer)
      
      # Contador para ver si una letra NO está
      c = 0
      for x in range(len(answer)):
        if user_answer == answer[x]:
          answer_displayed[x] = user_answer
          c += 1

      if c == 0:
          player.lives -= 0.25
          intentos -= 1
          print(f"Incorrecto! Has perdido 0.25 vidas, te quedan {player.lives} vidas y {intentos} intentos para resolver el ahorcado.")
          

      print(' '.join(answer_displayed))
       


    if answer_displayed == answer:
      player.inventory.append(api.json()[1]["objects"][0]["game"]["award"])
      print('\n-------------------------------------------\nCORRECTO! Has desbloqueado el CABLE HDMI para tus siguientes retos...')
      player.show()
      break

def library_left(player): # Preguntas matemáticas
  #Reglas, Pistas, Awards
  if "libro de Matemáticas" in player.inventory:
    print(f'\n-------------------------------------------\n{(api.json()[1]["objects"][1]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[1]["objects"][1]["game"]["rules"]}.\n\n')
  
    n = (0,(len(api.json()[1]["objects"][1]["game"]["questions"]))-1) # Seleccionador random de qué pregunta toca responder
  
    pistas = [api.json()[1]["objects"][1]["game"]["questions"][n]["clue_1"]]

    while True:
      print(api.json()[1]["objects"][1]["game"]["questions"][n]["question"])
      answer = api.json()[1]["objects"][1]["game"]["questions"][n]["answer"] #VALIDAR CON PYTHON SI EL RESULTADO DE LA DERIVADA ES CORRECTO
      #user_answer = 
      #       x = sympy.Symbol('x')
      # funcion_api = api.json()[1]["objects"][1]["game"]["questions"][n]["question"]
      # f = funcion_api.split('f(x)=')
      # f = (f[-1]).replace(' ', '')
      # print(f, type(f))
      # derivada_f = f.diff(x)
      # print(derivada_f)
  
  else: # Si no tiene el libro de matemáticas
    print(api.json()[1]["objects"][1]["game"]["message_requirement"])

def library_right(player): # Criptograma
  # castigo = 1 vida por partida perdida, award = api.json()[1]["objects"][2]["game"]["award"], preguntas, alfabetos
  if api.json()[1]["objects"][2]["game"]["requirement"] in player.inventory: # Chequear si tiene el requirement

    print(f'\n-------------------------------------------\n{(api.json()[1]["objects"][2]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

    n = random.randint(0,len(api.json()[1]["objects"][2]["game"]["questions"]) - 1)
    alfabeto_ordenado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    desplazamiento = api.json()[1]["objects"][2]["game"]["questions"][n]["desplazamiento"]
    alfabeto_desplazado = [alfabeto_ordenado[x + desplazamiento] for x in range(len(alfabeto_ordenado)) ]
    print(alfabeto_desplazado)
    while True:
      
      mensaje_original = list((api.json()[1]["objects"][2]["game"]["questions"][n]["question"]).lower())

      #cifrar mensaje
      #mensaje_cifrado = 

  else:
    print(api.json()[1]["objects"][2]["game"]["message_requirement"])
    
# lab_right(emilio)
# library_center(emilio)