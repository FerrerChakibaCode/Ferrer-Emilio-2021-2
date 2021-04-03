import enquiries
import random
import requests
import Player
import graficos
from Game import Game

class Criptograma(Game): #1,2
  def __init__(self, room, objeto):
    super().__init__(room, objeto)
    self.game = self.objeto["game"]
    self.message_requirement = self.game["message_requirement"]
    self.requirement = self.game["requirement"]
    self.award = self.game["award"]
    self.name = self.game["name"]
    self.rules = self.game["rules"]

  def jugar(self, player):
    n = random.randint(0,(len(self.game["questions"]))-1) # Seleccionador random de qué pregunta toca responder
    self.question = self.game["questions"][n]
    print(f'\n-------------------------------------------\n{self.game["name"].title()}\n\nREGLAS DEL JUEGO -> {self.rules.capitalize()}.\n\n')
    self.answer = self.question["question"]
    self.clues = [self.question[f"clue_{x}"] for x in range (1, len(self.question) - 2)]
    alfabeto_ordenado_largo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    desplazamiento = self.question["desplazamiento"]
    alfabeto_desplazado = []
    for x in range(26):
      alfabeto_desplazado.append(alfabeto_ordenado_largo[x + desplazamiento])
    if self.requirement in player.inventory:
      self.answer = list((self.answer).lower())
      mensaje_cifrado = []
      #cifrar mensaje
      for letter in self.answer:
        if letter == 'á':
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
      mensaje_cifrado = ''.join(map(str, mensaje_cifrado))
      
      while player.lives > 0 :
        print(mensaje_cifrado)
        
        print(graficos.alfabeto_desplazado[desplazamiento])
        print(graficos.small_spaces)
        user_answer = input('> ')
        if user_answer.lower() in answers_list:
          player.inventory.append(self.award)
          print('\n-------------------------------------------\nCORRECTO! Has desbloqueado el CABLE HDMI para tus siguientes retos...')
          player.show()
          break

        elif len(user_answer) != len(self.answer):
          print('CONSEJO: da como respuesta algo igual de largo a lo que te doy...')

        elif user_answer not in answers_list:
          player.lives -= 1
          print(f"Incorrecto! Has perdido 1 vida, te quedan {player.lives} vidas.")
    
    else:
      print(self.message_requirement)


# def library_right(player): # Criptograma
#   # castigo = 1 vida por partida perdida, award = api.json()[1]["objects"][2]["game"]["award"], preguntas, alfabetos
#   if api.json()[1]["objects"][2]["game"]["requirement"] in player.inventory: # Chequear si tiene el requirement

#     print(f'\n-------------------------------------------\n{(api.json()[1]["objects"][2]["game"]["name"]).title()}\n\nREGLAS DEL JUEGO -> {api.json()[0]["objects"][2]["game"]["rules"]}.\n\n')

#     n = random.randint(0,len(api.json()[1]["objects"][2]["game"]["questions"]) - 1)

#     alfabeto_ordenado_largo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    
#     desplazamiento = api.json()[1]["objects"][2]["game"]["questions"][n]["desplazamiento"]
#     alfabeto_desplazado = []

#     for x in range(26):
#       alfabeto_desplazado.append(alfabeto_ordenado_largo[x + desplazamiento])
    
#     mensaje_original = list((api.json()[1]["objects"][2]["game"]["questions"][n]["question"]).lower())
#     mensaje_cifrado = []
#     #cifrar mensaje
#     for letter in mensaje_original:
#       if letter == 'á':
#         letter = 'a'
#       elif letter == 'é':
#         letter = 'e'
#       elif letter == 'í':
#         letter = 'i'
#       elif letter == 'ó':
#         letter = 'o'
#       elif letter == 'ú':
#         letter = 'u'
#       if letter != ' ':
#         index = alfabeto_ordenado_largo.index(letter)
#         if index > 26:
#           index -= 26
#         print(index)
#         mensaje_cifrado.append(alfabeto_desplazado[index])
#       if letter == ' ':
#         mensaje_cifrado.append(' ')
#     print(mensaje_original, '   ', mensaje_cifrado)
#     break

#     while True:
#       print(question) 
#       user_answer = input('> ')
#   else:
#     print(api.json()[1]["objects"][2]["game"]["message_requirement"])