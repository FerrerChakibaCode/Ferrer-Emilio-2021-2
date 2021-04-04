import enquiries
import random
import requests
import Player
import graficos
from Game import Game
api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

class Quizizz(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    self.answers = [self.question[f'answer_{x}'] for x in range (2,len(self.question)-1)]
    self.correct_answer = [self.question["correct_answer"]]
    self.clues = [self.question[f'clue_{x}'] for x in range (1,len(self.question)-4)]

  def jugar(self, player):
    if self.award not in player.inventory:
      print(f'\n-------------------------------------------\n{self.game["name"].title()}\n-------------------------------------------\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
      print(graficos.small_spaces, self.question['question'], graficos.small_spaces)
      while player.lives > 0:

        user_answer = enquiries.choose('\n-------------------------------------------\nElija su respuesta', self.answers + self.correct_answer + ['Pista'] )
        if user_answer in self.correct_answer:
          print(f'\nEscogiste {user_answer}\n')
          player.inventory.append(self.award)
          print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
          print(player.show())
          break
        elif (user_answer not in self.correct_answer) and user_answer != 'Pista' :
          player.lives -= 0.5
          input(f"Incorrecto! Has perdido media vida, te quedan {player.lives} vidas. Si desea seguir intentando presione 'Enter'\n")

        elif user_answer == 'Pista' and len(self.clues) > 0 and player.clues > 0:
          print(f"PISTA: {self.clues[0]}")
          self.clues.pop(0)
          player.clues -= 1
          print(f"\nLe quedan {len(self.clues)} pistas en esta pregunta. Y a nivel global le quedan {player.clues} pistas.")
    
    elif self.award in player.inventory:
      print(f'Ya tienes {self.award}.upper() en tu inventario, no puedes volver a jugar este juego.')
