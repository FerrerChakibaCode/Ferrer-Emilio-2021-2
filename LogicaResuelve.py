import enquiries
import random
import requests
import Player
import graficos
from Game import Game
api = requests.get("https://api-escapamet.vercel.app/")

class LogicaResuelve(Game):
  def __init__(self, room, objeto): 
    super().__init__(room, objeto)  # Se trae del padre: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    self.game = self.objeto["game"] # Todos los valores del juego completo
    self.message_requirement = self.game["message_requirement"]  # Mensaje por si no tiene el requisito
    self.requirement1 = self.game["requirement"][0]  # requisito
    self.requirement2 = self.game["requirement"][1] # requisito
    self.award = self.game["award"] # item del award
    self.name = self.game["name"] # nombre del juego
    self.rules = self.game["rules"] # reglas por si se equivoca
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    self.answers = ['67', '41'] # respuestas 
    self.answer = self.answers[n] # respuesta especifica a la pregunta que le toca

  def jugar(self, player):
    
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

          break
        else:
          player.lives -= 1
          print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")
    
    elif self.award in player.inventory:
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')

    elif not (self.requirement1 and self.requirement2 in player.inventory):
      player.lives -= 1
      print(graficos.small_spaces, self.message_requirement, f'\nTe quedan {player.lives} vidas.')       

    if player.lives <= 0:
      print(graficos.good_bye)
