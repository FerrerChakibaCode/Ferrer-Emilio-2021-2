import requests
import random
import Player
import graficos
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'
# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])
class Ahorcado(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto) # Se trae del padre: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    self.game = self.objeto["game"] # Todos los valores del juego completo
    self.award = self.game["award"] # Item del award
    self.name = self.game["name"] # Nombre del juego
    self.rules = self.game["rules"] # Reglas por si se equivoca
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    print("Seleccione la letra que escoja. Seleccione '1' si quiere una pista")
    self.answer = self.question["answer"].lower() # Respuesta en lower para que se pueda validar más fácil
    self.clues = [self.question[f"clue_{x}"] for x in range (1, len(self.question) - 1)] # Lista de pistas

  def jugar(self, player):
    intentos = 5 # Vidas del ahorcado
    letras_disponibles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_usadas = []
    self.answer = list(self.answer)
    answer_displayed = ['_' for letter in self.answer] # La respuesta que el usuario va construyendo.

    while intentos > 0 and player.lives > 0 and self.award not in player.inventory: # Condiciones para que pueda seguir jugando
      print(graficos.small_spaces, self.question["question"])
      if intentos == 5:
        print(graficos.ahorcado_5) # Estos prints son la situación actual del muñequito del ahorcado
      elif intentos == 4:
        print(graficos.ahorcado_4)
      elif intentos == 3:
        print(graficos.ahorcado_3)
      elif intentos == 2:
        print(graficos.ahorcado_2)
      elif intentos == 1:
        print(graficos.ahorcado_1)

      user_answer = input('> ')
      if user_answer == '1': # Si elige una pista...
        if player.clues > 0 and len(self.clues) > 0:
          print(self.clues[0])
          self.clues.pop(0)
        elif player.clues == 0:
          print('A usted ya no le quedan pistas')
        elif len(self.clues) == 0:
          print('Ya no le quedan pistas en este ahorcado')
        else:
          print('No puede utilizar más pistas')

      if user_answer in letras_usadas:
        print(f'Esta es la lista de letras usadas: {letras_usadas}')

      elif len(user_answer)>1:
        print('UNA SOLA LETRA A LA VEZ')
        print(' '.join(answer_displayed))

      elif user_answer in letras_disponibles: # Si la letra que escogió se puede usar
        letras_disponibles.pop(letras_disponibles.index(user_answer))
        letras_usadas.append(user_answer)
        
        # Contador para ver si una letra NO está
        c = 0
        for x in range(len(self.answer)):
          if user_answer == self.answer[x]:
            answer_displayed[x] = user_answer
            c += 1

        if c == 0: # Como el contador no se aumentó, la letra no está en la palabra
            player.lives -= 0.25
            intentos -= 1
            print(f"Incorrecto! Has perdido 0.25 vidas, te quedan {player.lives} vidas y {intentos} intentos para resolver el ahorcado.")
        
        print(' '.join(answer_displayed))
        user_answer = ('> ')
      
      if answer_displayed == self.answer: # Si la respuesta que armó es la que está en self.answer, ganó
        player.inventory.append(self.award)
        print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado el {self.award.upper()} para tus siguientes retos...')

        break
    
    if self.award in player.inventory: # Para que no repita el juego por el award
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')
    
    if intentos <= 0: # Cuando se muere el ahorcado
      print(graficos.ahorcado_muerto)
