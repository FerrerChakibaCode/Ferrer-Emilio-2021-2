import requests
import random
import Player
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, 600, ['contraseña'])

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
    self.answers = [self.question["answers"][x] for x in range (5)]
    self.clues = [self.question[f"clue_{x}"] for x in range (1,4)]

  def jugar(self, user_answer, player):
    while player.lives > 0:
      if user_answer in self.answers:
        player.inventory.append(self.award)
        print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
        print(player.show())
        break

      elif user_answer == 'p' and len(self.clues) > 0 and player.clues > 0:
        print(self.clues[0])
        self.clues.pop(0)
        player.clues -= 1
        user_answer = input('> ')
      
      elif user_answer == 'p' and len(self.clues) == 0:
        print('No quedan pistas en esta pregunta.')
        user_answer = input('> ')
      
      elif user_answer == 'p' and player.clues == 0:
        print('No te quedan pistas')
        user_answer = input('> ')      

      else:
        player.lives -= 0.5
        user_answer = input(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")

    if player.lives == 0:
      print('Game over...') #TODO programar los game over

#award = adivi.jugar_adivinanza(user_answer)
#emilio.inventory.append(award)
#print(f'el inventorio actual es: {emilio.inventory}')