import enquiries
import random
import requests
import Player
import graficos
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, 600, ['contraseña', 'llave'])
def jugar(player):
  pregunta = [['😀', '🙄', '🤮', '🥰'],
  ['🤮', '😨', '🤓', '😷'],
  ['😨', '🤓', '🥰', '😷'],
  ['🤑', '🤑', '🙄', '😀']]

  memoria = []
  random.shuffle(pregunta)
  for fila in pregunta:
    random.shuffle(fila)
    memoria.append([])
    for emoji in fila:
      memoria[-1].append('?')



  while player.lives > 0:
    print(pregunta[0])
    print(pregunta[1])
    print(pregunta[2])
    print(pregunta[3])
    print(graficos.small_spaces)
    # print(graficos.small_spaces)
    print(memoria[0])
    print(memoria[1])
    print(memoria[2])
    print(memoria[3])    

    if memoria == pregunta:
      print('GANASTE!')
      break

    filas_columnas = [1, 2, 3, 4]

    pick_1_fila = (enquiries.choose('ELIJA FILA DEL PRIMER EMOJI →', filas_columnas)) - 1
    pick_1_columna = (enquiries.choose('ELIJA COLUMNA DEL PRIMER EMOJI ↑', filas_columnas)) - 1

    while memoria[pick_1_fila][pick_1_columna] != '?':

      print('CUIDADO! Esa ya la memorizaste.')
      pick_1_fila = (enquiries.choose('ELIJA FILA DEL PRIMER EMOJI →', filas_columnas)) - 1
      pick_1_columna = (enquiries.choose('ELIJA COLUMNA DEL PRIMER EMOJI ↑', filas_columnas)) - 1

    print(f"Elegiste que el primer emoji está en la fila: {pick_1_fila + 1} y en la columna: {pick_1_columna + 1}")

    pick_2_fila = (enquiries.choose('ELIJA FILA DEL SEGUNDO EMOJI →', filas_columnas)) - 1
    pick_2_columna = (enquiries.choose('ELIJA COLUMNA DEL SEGUNDO EMOJI ↑', filas_columnas)) - 1

    while memoria[pick_2_fila][pick_2_columna] != '?' or f'{pick_2_fila},{pick_2_columna}' != f'{pick_1_fila}, {pick_1_columna}':

      print('CUIDADO! Revisa qué estás seleccionando.')
      pick_2_fila = (enquiries.choose('ELIJA FILA DEL SEGUNDO EMOJI →', filas_columnas)) - 1
      pick_2_columna = (enquiries.choose('ELIJA COLUMNA DEL SEGUNDO EMOJI ↑', filas_columnas)) - 1

    print(f"Elegiste que el segundo emoji está en la fila: {pick_2_fila + 1} y en la columna: {pick_2_columna + 1}")

    if pregunta[pick_1_fila][pick_1_columna] == pregunta[pick_2_fila][pick_2_columna]:
      print('memoria!')
      memoria[pick_1_fila][pick_1_columna] = pregunta[pick_1_fila][pick_1_columna]
      memoria[pick_2_fila][pick_2_columna] = pregunta[pick_2_fila][pick_2_columna]

    elif pregunta[pick_1_fila][pick_1_columna] != pregunta[pick_2_fila][pick_2_columna]:
      player.lives -= 0.25
      print(f'fallaste, pierdes un cuarto de vida y te quedan {player.lives}')

jugar(emilio)