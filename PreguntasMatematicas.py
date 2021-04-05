import enquiries
import random
import requests
import Player
import graficos
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/")
# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

class PreguntasMatematicas(Game):
  #PONER AWARD COMO VIDA EXTRA
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirement = self.game["requirement"] + ' 1'
    self.name = self.game["name"]
    self.rules = self.game["rules"].capitalize()
    self.award = self.game["award"]
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}\nEscribe tu resultado con un solo decimal.\n\n')
    print(self.question["question"])
    # self.answers = [self.question["answers"][x] for x in range (5)]

  def jugar(self, player):
    if self.requirement in player.inventory and self.award not in player.inventory:
      f = self.question["question"].split('f(x)=') #Tomamos la función del api y la dividimos para tomar la función en sí
      x = (f[0].split())[-1] # Antes de seguir modificando la variable 'f', tomamos nuestra X
      f = f[-1].replace(' ', '')
      f = f.replace('sen', 'sin')
      symbols = {'x': Symbol('x', real = True)}
      x = parse_expr(x, symbols) # Convertimos a X en type que Sympy acepte
      f = parse_expr(f, symbols) # Convertimos a f(x) en type que Sympy acepte

      derivada_f = diff(f, symbols['x']) # Hallar la derivada de la función
      print(derivada_f)

      evaluar_derivada_en_x = derivada_f.evalf(subs = {symbols['x']: x}) # Derivar la función en el valor de X
      evaluar_derivada_en_x = round(evaluar_derivada_en_x, 1) # Redondear a 1 decimal

      print(graficos.small_spaces)
      while True:
        user_answer = input('> ')

        if user_answer == str(evaluar_derivada_en_x):
          player.lives += 1
          player.inventory.append(self.award)
          print(f'\n-------------------------------------------\nCORRECTO! Has ganado una {self.award.upper()} para tus siguientes retos...')
          print(player.show())
          break

        elif user_answer != str(evaluar_derivada_en_x):
          player.lives -= 0.25
          print(f"Incorrecto! Has perdido un cuarto de vida, te quedan {player.lives}. Si desea seguir intentando responder ingrese su respuesta. Si no, presione 'Enter'\n")
          if user_answer == '':
            break

    elif self.award in player.inventory: # Si ya jugó, no puede volver a jugar...
        print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')

    else:
      print(graficos.small_spaces,self.message_requirement,graficos.small_spaces)
