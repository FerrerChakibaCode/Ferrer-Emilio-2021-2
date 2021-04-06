import enquiries
import random
import requests
import Player
import graficos
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr
from Game import Game
import word_search
class SopaLetras(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.award = self.game["award"]
    self.name = (self.game["name"]).replace('_', ' ')
    self.rules = self.game["rules"]

    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.name.title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\nIngrese \'p\' si desea una pista.')
    self.clues = [self.question[f"clue_{x}"] for x in range(1,4)]
    self.answers = [self.question["answer_1"], self.question["answer_2"], self.question["answer_3"]]

  def jugar(self, player):
    self.filas = 15
    self.columnas = 15
    matriz_vacia = [[] for x in range (self.filas)]
    for fila in matriz_vacia:
      for x in range(self.filas):
        fila.append(' ')

    palabras = ['', '', '']
    for x in range(len(palabras)):
      palabras[x] = self.answers[x]
    posicionamiento = random.randint(1,3)
    while len(palabras) > 0:
      try: # Hago un try acá porque si el juego se rompe, va al except. Va a hacer 'try' a hacer la sopa bien
        palabra = palabras[-1]
        # posicionamiento = random.randint(1,3)    # HORIZONTALES: 3, VERTICALES: 2, DIAGONALES: 1
        
        if posicionamiento == 1:
        
          fila = random.randint(0,(self.filas - len(palabra[0])) - 2) # Posicion random de la primera letra de la palabra
          columna = random.randint(0, self.columnas - len(palabra[0]) - 2)
          disponible = False
          for x in range(len(palabra)):
            if matriz_vacia[fila + x][columna + x] == ' ' or matriz_vacia[fila + x][columna + x] == palabra[x]:
              disponible = True
            else:
              disponible = False
              raise Exception
              break
          if disponible:
            for x in range(len(palabra)):
              if matriz_vacia[fila + x][columna + x] == ' ' or matriz_vacia[fila + x][columna + x] == palabra[x]:
                matriz_vacia[fila + x][columna + x] = palabra[x]


        elif posicionamiento == 2:

          fila = random.randint(0,(self.filas - len(palabra[0])) - 2)
          columna = random.randint(0, 14)
          for x in range(len(palabra)):
            if matriz_vacia[fila + x][columna] == ' ' or matriz_vacia[fila + x][columna] == palabra[x]:
              disponible = True              
            else:
              disponible = False
              raise Exception
              break
          if disponible:
            for x in range(len(palabra)):
              if matriz_vacia[fila + x][columna] == ' ' or matriz_vacia[fila + x][columna + x] == palabra[x]:
                matriz_vacia[fila + x][columna] = palabra[x]              
        elif posicionamiento == 3:

          fila = random.randint(0, 14)
          columna = random.randint(0,(self.filas - len(palabra[0])) - 2)
          for x in range(len(palabra)):
            if matriz_vacia[fila][columna + x] == ' ' or matriz_vacia[fila][columna + x] == palabra[x]:
              disponible = True
            else:
              disponible = False
              raise Exception 
              break       
          if disponible:
            for x in range(len(palabra)):
              if matriz_vacia[fila][columna + x] == ' ' or matriz_vacia[fila + x][columna + x] == palabra[x]:
                matriz_vacia[fila][columna + x] = palabra[x]              
        palabras.pop()
        posicionamiento = random.randint(1,3)
      except:
        posicionamiento = random.randint(1,3)


    #Ahora a rellenar la matriz con letras random
    alfabeto = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
# ,'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'    
    for x in range(len(matriz_vacia)):
      for y in range(len(matriz_vacia)):
        if matriz_vacia[x][y] == ' ':
          random.shuffle(alfabeto)
          matriz_vacia[x][y] = alfabeto[0]

    for fila in range(len(matriz_vacia)):
      print(matriz_vacia[fila])

  def jugar(self, player):
    while len(self.answers) > 0 and self.award not in player.inventory and player.lives > 0:
      for x in range(len(self.answers)):
        self.answers[x] = self.answers[x].lower()
      user_answer = input('> ').lower()
      if user_answer == 'p':
        if player.clues > 0 and len(self.clues) > 0:
          print(self.clues[0])
          player.clues -= 1
          self.clues.pop(0)
          print(f'Usaste una pista, te quedan {len(self.clues)} en este juego, y {player.clues} a nivel global.')

        elif user_answer == 'p' and len(self.clues) <= 0:
          print('No te quedan pistas en este juego.')

        elif user_answer == 'p' and player.clues <= 0:
          print('No te quedan más pistas, buena suerte.')

      elif user_answer in self.answers:
        print(f'Elegiste: {user_answer}, y eso es CORRECTO!')
        self.answers.pop(self.answers.index(user_answer))

      elif user_answer not in self.answers:
        player.lives -= 0.5
        print(f'INCORRECTO! Has perdido media vida y te quedan {player.lives}.')

    if len(self.answers) <= 0:
        player.inventory.append(self.award)
        player.lives += 1
        print(f'\n-------------------------------------------\nGANASTE! Has desbloqueado {self.award.upper()} para tus siguientes retos, te quedan ahora {player.lives} vidas...')
    
    if self.award in player.inventory:
      print('Ya has ganado este juego! No puedes volver a jugarlo.')
