import enquiries
import random
import requests
import Player
import graficos
from Game import Game

api = requests.get("https://api-escapamet.vercel.app/")

class MemoriaEmoji(Game):
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]
    
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    self.clue = [self.game["questions"][n]["clue_1"]]

  def jugar(self, player):
    if self.award not in player.inventory:
      # pregunta = [['😀', '🙄', '🤮', '🥰'],
      # ['🤮', '😨', '🤓', '😷'],
      # ['😨', '🤓', '🥰', '😷'],
      # ['🤑', '🤑', '🙄', '😀']]
      pregunta = self.question["question"] # PARA QUE FUNCIONE TIENEN QUE RESPONDERME LOS PREPARADORES SOBRE QUÉ HACER CON LOS \N
      pregunta = list((((pregunta.replace('\n','')).replace('[','')).replace(']','')).replace(' ','').split(','))
      pregunta = [pregunta[:4], pregunta[4:8], pregunta[8:12], pregunta[12:]]
      memoria = []
      random.shuffle(pregunta)
      for fila in pregunta:
        random.shuffle(fila)
        memoria.append([])
        for emoji in fila:
          memoria[-1].append(' ? ')

      while player.lives > 0:
        
        print(memoria[0])
        print(memoria[1])
        print(memoria[2])
        print(memoria[3])    
        print(graficos.spaces)
        if memoria == pregunta:
          player.inventory.append(self.award)
          print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award.upper()} para tus siguientes retos...')
          break

        filas_columnas = [1, 2, 3, 4]

        pick_1_fila = (enquiries.choose('ELIJA FILA DEL PRIMER EMOJI →', filas_columnas)) - 1
        pick_1_columna = (enquiries.choose('ELIJA COLUMNA DEL PRIMER EMOJI ↑', filas_columnas)) - 1


        while memoria[pick_1_fila][pick_1_columna] != ' ? ':

          print('CUIDADO! Esa ya la memorizaste.')
          pick_1_fila = (enquiries.choose('ELIJA FILA DEL PRIMER EMOJI →', filas_columnas)) - 1
          pick_1_columna = (enquiries.choose('ELIJA COLUMNA DEL PRIMER EMOJI ↑', filas_columnas)) - 1

        print(f"Elegiste que el primer emoji está en la fila: {pick_1_fila + 1} y en la columna: {pick_1_columna + 1}. Y es {pregunta[pick_1_fila][pick_1_columna]}")
        
        if len(self.clue) > 0:
          options = ['Sí', 'No']
          pick_2 = enquiries.choose('Quieres una pista?', options)
          if pick_2 == options[0]:
            player.clues -= 1
            posicion_pista = ''
            for fila in pregunta:
              for emoji in fila:
                if pregunta[pregunta.index(fila)][fila.index(emoji)] == pregunta[pick_1_fila][pick_1_columna]:
                  posicion_pista += f'\nFila: {pregunta.index(fila)+1}\nColumna: {fila.index(emoji)+1}'
      

            print(f'Ahora te quedan {player.clues} pistas... La pareja de tu emoji está en la posición\n{posicion_pista}')
            self.clue.pop(0)

        pick_2_fila = (enquiries.choose('ELIJA FILA DEL SEGUNDO EMOJI →', filas_columnas)) - 1
        pick_2_columna = (enquiries.choose('ELIJA COLUMNA DEL SEGUNDO EMOJI ↑', filas_columnas)) - 1

        while (pick_1_columna == pick_2_columna and pick_1_fila == pick_2_fila):
          print('CUIDADO! Revisa qué estás seleccionando.')

          pick_2_fila = (enquiries.choose('ELIJA FILA DEL SEGUNDO EMOJI →', filas_columnas)) - 1
          pick_2_columna = (enquiries.choose('ELIJA COLUMNA DEL SEGUNDO EMOJI ↑', filas_columnas)) - 1

        print(f"Elegiste que el segundo emoji está en la fila: {pick_2_fila + 1} y en la columna: {pick_2_columna + 1} y es {pregunta[pick_2_fila][pick_2_columna]}")

        if pregunta[pick_1_fila][pick_1_columna] == pregunta[pick_2_fila][pick_2_columna]:
          print('memoria!')
          memoria[pick_1_fila][pick_1_columna] = pregunta[pick_1_fila][pick_1_columna]
          memoria[pick_2_fila][pick_2_columna] = pregunta[pick_2_fila][pick_2_columna]

        elif pregunta[pick_1_fila][pick_1_columna] != pregunta[pick_2_fila][pick_2_columna]:
          player.lives -= 0.25
          print(f'Fallaste, pierdes un cuarto de vida y te quedan {player.lives}')
          # print(pregunta[pick_1_fila][pick_1_columna], pregunta[pick_2_fila][pick_2_columna])
          
    elif self.award in player.inventory:
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')

# memoji = MemoriaEmoji(2, 2)
# memoji.jugar(emilio)