import enquiries
import random
import requests
import Player
import graficos
from Game import Game
api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, 600, ['contraseña', 'llave', 'Titulo Universitario', 'Mensaje'])

class LogicaResuelve(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirement1 = self.game["requirement"][0]
    self.requirement2 = self.game["requirement"][1]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    self.answers = ['67', '41']
    self.answer = self.answers[n]

  def jugar(self, player):
    player.lives -= 1
    if (self.requirement1 and self.requirement2) in player.inventory and self.award not in player.inventory:
      print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\nTe quedan entonces {player.lives} vidas.\n')
      while player.lives > 0:
        print(graficos.small_spaces, self.question, graficos.small_spaces)
        user_answer = input('> ')
        while not user_answer.isnumeric():
          user_answer = input('Por favor ingrese un número entero\n> ')
        if user_answer == self.answer:
          player.inventory.append(self.award)
          print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
          print(player.show())
          break
        else:
          player.lives -= 0.5
          print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")
    else:
      print(self.message_requirement, f'\nTe quedan {player.lives} vidas.')       

    if player.lives <= 0:
      print(graficos.good_bye) # TODO cambiar por un ASCII de game-over

# logica = LogicaResuelve(2, 0)
# logica.jugar(emilio)
# print('vamos de nuevo')