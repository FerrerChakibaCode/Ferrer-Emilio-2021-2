import enquiries
import random
import requests
import Player
import graficos
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr
from Game import Game

class FinalBoss(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto) 
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirements = self.game["requirement"]
    self.award = self.game["award"]
    self.name = 'La vieja'
    self.rules = self.game["rules"]
    
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    
    print(self.requirements)

  def jugar(self, player):

    matriz = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    ganador = 2
    n = 0
    while ganador == 2 and player.lives > 0:
      ganador = 2
      if n == 0: #Juega primero el user
        for x in range(len(matriz)):
          if matriz[x][0] == 'X' and  matriz[x][1] == 'X' and  matriz[x][2] == 'X':
            ganador = 0
            print('llegué hasta acá')
            break

          elif matriz[0][x] == 'X' and  matriz[1][x] == 'X' and  matriz[2][x] == 'X':
            ganador = 0
            break
            
          elif matriz[x][x] == 'X' and  matriz[x][x] == 'X' and  matriz[x][x] == 'X':
            ganador = 0
            break

          elif matriz[x][0] == 'O' and  matriz[x][1] == 'O' and  matriz[x][2] == 'O':
            ganador = 1
            break

          elif matriz[0][x] == 'O' and  matriz[1][x] == 'O' and  matriz[2][x] == 'O':
            ganador = 1
            break
            
          elif matriz[x][x] == 'O' and  matriz[x][x] == 'O' and  matriz[x][x] == 'O':
            ganador = 1
            break
          
        if ganador != 2:
          break
        else:
          continue

        print(matriz[0])
        print(matriz[1])
        print(matriz[2])
        print(graficos.small_spaces)
        choice = [1, 2, 3]
        fila = (enquiries.choose('← Elija fila →', choice)) - 1
        columna = (enquiries.choose('↓ Elija columna ↑', choice)) - 1
        while True:
          try:
            if matriz[fila][columna] != '_':
              raise Exception
            elif matriz[fila][columna] == '_':
              matriz[fila][columna] = 'X'
              break
          except: 
            fila = (enquiries.choose('← ELIJA BIEN, FILA →', choice)) - 1
            columna = (enquiries.choose('↓ ELIJA BIEN, COLUMNA ↑', choice)) - 1

        n = 1

      if n == 1:
        for x in range(len(matriz)):
          if matriz[x][0] == 'X' and  matriz[x][1] == 'X' and  matriz[x][2] == 'X':
            ganador = 0
            break

          elif matriz[0][x] == 'X' and  matriz[1][x] == 'X' and  matriz[2][x] == 'X':
            ganador = 0
            break
            
          elif matriz[x][x] == 'X' and  matriz[x][x] == 'X' and  matriz[x][x] == 'X':
            ganador = 0
            break

          elif matriz[x][0] == 'O' and  matriz[x][1] == 'O' and  matriz[x][2] == 'O':
            ganador = 1
            break

          elif matriz[0][x] == 'O' and  matriz[1][x] == 'O' and  matriz[2][x] == 'O':
            ganador = 1
            break
            
          elif matriz[x][x] == 'O' and  matriz[x][x] == 'O' and  matriz[x][x] == 'O':
            ganador = 1
            break

        if ganador != 2:
          break
        else:
          continue

        print(matriz[0])
        print(matriz[1])
        print(matriz[2])
        print(graficos.small_spaces)
        fila = random.randint(0,2)
        columna = random.randint(0,2)
        while True:
          try:
            if matriz[fila][columna]!= '_':
              # print('llegué hasta acá')
              raise Exception
            elif matriz[fila][columna] == '_':
              matriz[fila][columna] = 'O'
              break
          except: 
            fila = random.randint(0,2)
            columna = random.randint(0,2)
        ganador = 2
        n = 0
    
    if ganador == 0:
      print(f'¡Felicidades, {player.avatar}! Has logrado evitar una catástrofe en la Unimet, gracias al DISCO DURO que recuperaste Sirius funcionará de nuevo, y te podrán descontar la deuda que tienes desde hace años. Ah no, es que no pagaste nunca... bueno, feliz día!')
      player.inventory.append(self.award)
    
    elif ganador == 1:
      player.lives -= 1
      print(f'PERDISTE! Has perdido media vida y te quedan {player.lives}.')