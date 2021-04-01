import requests
import Player
import random
api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña'])
def library_center(player):
  # No tiene requirement, tiene 5 intentos
  #award: api.json()[1]["objects"][0]["game"]["award"]
  print(f'\n-------------------------------------------\n{(api.json()[1]["objects"][0]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[1]["objects"][0]["game"]["rules"]}.\n')

  n = random.randint(0,2)

  pistas = [api.json()[1]["objects"][0]["game"]["questions"][n]["clue_1"], api.json()[1]["objects"][0]["game"]["questions"][n]["clue_2"], api.json()[1]["objects"][0]["game"]["questions"][n]["clue_3"]]
  letras_disponibles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  answer = (api.json()[1]["objects"][0]["game"]["questions"][n]["answer"]).lower()

  answer = list(answer)
  answer_displayed = ['_' for letter in answer]
  print(api.json()[1]["objects"][0]["game"]["questions"][n]["question"])
  while True:
    
    print("Seleccione la letra que escoja. Seleccione '1' si quiere una pista")
    user_answer = input("> ").lower()

    if user_answer in letras_disponibles:
      letras_disponibles.pop(letras_disponibles.index(user_answer))
      if user_answer in answer:
        answer_displayed[answer.index(user_answer)] = user_answer
      print(' '.join(answer_displayed))
      # for x in range(len(answer)):
      #   if user_answer == answer[x]:
      #     answer_displayed[x] = user_answer
      # print(' '.join(answer_displayed))

    if answer_displayed == answer:
      print('Lo lograste!')
      break

library_center(emilio)