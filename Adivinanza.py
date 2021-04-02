import requests
import random
import Player
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña'])

class Adivinanza(Game):
  def __init__(self, room, objeto):
    # PARA SABER: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirement = self.game["requirement"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]

    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    print(self.question["question"])
    self.answers = [(api.json()[0]["objects"][2]["game"]["questions"][n]["answers"][x]) for x in range (5)]
    self.clues = [self.question[f"clue_{x}"] for x in range (1,4)]

  def jugar_adivinanza(self, user_answer, player):
    while True:
      if user_answer in self.answers:
        emilio.inventory.append(self.award)
        print('\n-------------------------------------------\nCORRECTO! Has desbloqueado la LLAVE para tus siguientes retos...')
        print(emilio.show())
        return self.award
        break

      elif user_answer == 'p' and len(self.clues) > 0:
        print(self.clues[0])
        self.clues.pop(0)
        user_answer = input('> ')
      
      elif user_answer == 'p' and len(self.clues) == 0:
        print('no te quedan pistas')
        user_answer = input('> ')
      else:
        user_answer = input('la cagaste.\n> ')

      
def lab_right(player): # Adivinanzas
  #TODO en el juego donde el award sea "contraseña, verificar que se esté dando esto"

  if "contraseña" in player.inventory:

    print(f'\n-------------------------------------------\n{(api.json()[0]["objects"][2]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

    n = random.randint(0,(len(api.json()[0]["objects"][2]["game"]["questions"]))-1) # Seleccionador random de qué pregunta toca responder

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

adivi = Adivinanza(room = 0, objeto = 2)
user_answer = input('> ')
adivi.jugar_adivinanza(user_answer, player = emilio)

#award = adivi.jugar_adivinanza(user_answer)
#emilio.inventory.append(award)
#print(f'el inventorio actual es: {emilio.inventory}')