import enquiries
import random
import requests
import Player
import graficos
from Game import Game
api = requests.get("https://api-escapamet.vercel.app/")
# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

class EscogeNumero(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto) # Se trae del padre: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    self.game = self.objeto["game"] # Todos los valores del juego completo
    self.award = self.game["award"] # item del award
    self.name = self.game["name"] # nombre del juego
    self.rules = self.game["rules"] # reglas por si se equivoca

    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n] # pregunta que le toca
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    print(self.question["question"])
    self.clues = ['Estás cerca un poco abajo', 'Estás cerca un poco arriba', 'Estás muy abajo', 'Estás muy arriba']

  def jugar(self, player):
    num = random.randint(1,15) # número por adivinar
    fails = 0 # intentos fallidos
    while player.lives > 0 and self.award not in player.inventory:
      if fails == 3:
        player.lives -= 0.33 # cuando se equivoca 3 veces pasa esto
        player.lives = round(player.lives, 2)
        print(f"Incorrecto! Has perdido 0.33 vidas, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")
        fails = 0
      user_answer = input('> ')
      user_answer = int(user_answer)
      diferencia_answer_num = user_answer - num
      if diferencia_answer_num > 0 and diferencia_answer_num < 3:
        print(self.clues[1])
        fails += 1
      
      elif diferencia_answer_num >= 3: # revisa que tan cerca esta, igual que los elif
        print(self.clues[3])
        fails += 1
      
      elif diferencia_answer_num > -3 and diferencia_answer_num < 0:
        print(self.clues[0])
        fails += 1

      elif diferencia_answer_num <= -3:
        print(self.clues[2])
        fails += 1
      
      elif num == user_answer:
        player.inventory.append(self.award)
        print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
        print(player.show())
        break

    if self.award in player.inventory:
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')

    if player.lives == 0: # si se muere
      print(f'{graficos.good_bye}')
