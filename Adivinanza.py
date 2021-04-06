import requests
import random
import Player
import graficos
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'

class Adivinanza(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto) # Se trae del padre: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    self.game = self.objeto["game"] # Todos los valores del juego completo
    self.message_requirement = self.game["message_requirement"] # Mensaje por si no tiene el requisito
    self.requirement = self.game["requirement"] # Requisito
    self.award = self.game["award"] # Item de award
    self.name = self.game["name"] # Nombre del juego para printear
    self.rules = self.game["rules"] # Reglas por si se equivoca

    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n] # Definir la pregunta
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    print(self.question["question"])
    self.clues = [self.question[f"clue_{x}"] for x in range (1,4)]
    self.answers = [self.question["answers"][x] for x in range (len(self.question["answers"]))]

    

  def jugar(self, player):
    while player.lives > 0 and self.award not in player.inventory:
      user_answer = input('> ')
      if user_answer in self.answers:
        player.inventory.append(self.award)
        print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
        break

      elif user_answer == 'p' and len(self.clues) > 0 and player.clues > 0: # Si es apto para pistas
        print(self.clues[0])
        self.clues.pop(0)
        player.clues -= 1
      
      elif user_answer == 'p' and len(self.clues) == 0: # Si no le quedan pistas
        print('No quedan pistas en esta pregunta.')
      
      elif user_answer == 'p' and player.clues == 0: # Si no le quedan pistas
        print('No te quedan pistas')

      else: # Si se equivoca...
        player.lives -= 0.5 
        print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")

    if player.lives == 0: # Si se muere
      print(graficos.good_bye)

    if self.award in player.inventory: # Para que no repita
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.') 

