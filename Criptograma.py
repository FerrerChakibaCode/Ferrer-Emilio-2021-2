import enquiries
import random
import requests
import Player
import graficos
from Game import Game

# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])
class Criptograma(Game): #1,2
  def __init__(self, room, objeto):
    super().__init__(room, objeto) # Se trae del padre: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    self.game = self.objeto["game"] # Todos los valores del juego completo
    self.message_requirement = self.game["message_requirement"] # Mensaje por si no tiene el requisito
    self.requirement = self.game["requirement"] # Requisito
    self.award = self.game["award"] # Item del award
    self.name = self.game["name"] # Nombre del juego
    self.rules = self.game["rules"] # Reglas por si se equivoca

  def jugar(self, player):
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de CUÁNTO se desplaza el alfabeto
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    self.answer = self.question["question"]
    self.clues = [self.question[f"clue_{x}"] for x in range (1, len(self.question) - 2)]
    alfabeto_ordenado_largo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    desplazamiento = self.question["desplazamiento"]
    alfabeto_desplazado = [] # Alfabeto cifrado que vamos a armar
    for x in range(26): #Iteramos del largo de un alfabeto normal
      alfabeto_desplazado.append(alfabeto_ordenado_largo[x + desplazamiento]) # Añadimos al alfabeto cifrado la letra
    if self.requirement in player.inventory:
      self.answer = list((self.answer).lower())
      mensaje_cifrado = []
      #cifrar mensaje
      for letter in self.answer:
        if letter == 'á': # Quitamos los acentos
          self.answer[self.answer.index(letter)] = 'a'
        elif letter == 'é':
          self.answer[self.answer.index(letter)] = 'e'
        elif letter == 'í':
          self.answer[self.answer.index(letter)] = 'i'
        elif letter == 'ó':
          self.answer[self.answer.index(letter)] = 'o'
        elif letter == 'ú':
          self.answer[self.answer.index(letter)] = 'u'
        elif letter != ' ':
          index = alfabeto_ordenado_largo.index(letter)
          if index > 26:
            index -= 26
          mensaje_cifrado.append(alfabeto_desplazado[index])
        elif letter == ' ':
          mensaje_cifrado.append(' ')

      self.answer = ''.join(map(str,self.answer))
      answers_list = [self.answer,'si te graduas pisas el samán' ,'si te gradúas pisas el samán' ,'si te gradúas pisas el saman']
      mensaje_cifrado = ''.join(map(str, mensaje_cifrado)) # Juntamos el mensaje cifrado
      
      while player.lives > 0 :
        print(mensaje_cifrado)
        
        print(graficos.alfabeto_desplazado[desplazamiento])
        print(graficos.small_spaces)
        user_answer = input('> ')
        if user_answer.lower() in answers_list: 
          player.inventory.append(self.award)
          print(f'\n-------------------------------------------\nCORRECTO! Has desbloqueado {self.award} para tus siguientes retos...')

          break

        elif len(user_answer) != len(self.answer): # Si su respuesta no tiene el length que es, le advierto
          print('CONSEJO: da como respuesta algo igual de largo a lo que te doy...')

        elif user_answer not in answers_list: # Si se equivoca
          player.lives -= 1
          print(f"Incorrecto! Has perdido 1 vida, te quedan {player.lives} vidas.")
    
    elif self.award in player.inventory: # Si quiere repetir el juego por el award.
      print(f'Ya tienes {self.award.upper()} en tu inventario, no puedes volver a jugar este juego.')

    else: # Si no tiene el requisito
      print(graficos.small_spaces, self.message_requirement)