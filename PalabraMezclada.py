import enquiries
import random
import requests
import Player
import graficos
from Game import Game
api = requests.get("https://api-escapamet.vercel.app/")
# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

class PalabraMezclada(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]


  def jugar(self, player):

    n = random.randint(0,len(self.question["words"])-1) # Número de la palabra del API que le oca descifrar
    word = self.question["words"][n]
    word = list(word)
    random.shuffle(word)
    word = ''.join(word)
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n-------------------------------------------\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    print(self.question["question"], graficos.small_spaces,'Categoría: ',self.question["category"],'\nPalabra: ',word, graficos.small_spaces)
    
    while player.lives > 0 and self.award not in player.inventory:
      user_answer = input('> ')
      if user_answer == self.question["words"][n]:
        player.inventory.append(self.award)
        print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
        break

      elif len(user_answer) != len(self.question["words"][n]):
        print('Escriba una palabra del mismo largo al enunciado...')
      
      else:
        player.lives -= 0.5
        print(f"Incorrecto! Has perdido media vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")
    
    if self.award in player.inventory:
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')
