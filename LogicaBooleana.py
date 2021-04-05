import enquiries
import random
import requests
import Player
import graficos
from Game import Game
api = requests.get("https://api-escapamet.vercel.app/")
# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

class LogicaBooleana(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirement = self.game["requirement"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    self.answer = self.question["answer"]
  
  def jugar(self, player):
    if self.requirement in player.inventory and self.award not in player.inventory:
      
      print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
      while player.lives > 0:
        enunciado_pregunta = self.question["question"]  
        #print(enunciado_pregunta)
        enunciado_pregunta = enunciado_pregunta.split('?', 1)
        print(enunciado_pregunta[0],'\n\n', enunciado_pregunta[1])        
        user_answer = input(f'{graficos.small_spaces} > ').capitalize()
        while user_answer != 'True' and user_answer != 'False':
          user_answer = input('De un valor booleano, por favor.\n> ')
        if user_answer == self.answer:
          player.inventory.append(self.award)
          print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
          break
        
        else:
          player.lives -= 0.5
          print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")

      if player.lives <= 0:
        print(graficos.good_bye)
    
    elif self.award not in player.inventory and self.requirement not in player.inventory:
      print(graficos.small_spaces, self.message_requirement, graficos.small_spaces)
    
    elif self.award in player.inventory:
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')
