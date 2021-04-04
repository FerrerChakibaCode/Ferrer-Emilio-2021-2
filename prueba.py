import requests
import Player
import random
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr

api = requests.get("https://api-escapamet.vercel.app/")
# emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

pregunta = api.json()[2]["objects"][2]["game"]["questions"][0]["question"]
pregunta = pregunta.replace('\n','')
pregunta = pregunta.replace('[', '')
pregunta = pregunta.replace(']', '')
pregunta = pregunta.replace(' ', '')
pregunta = list(pregunta.split(','))
pregunta = [pregunta[:4], pregunta[4:8], pregunta[8:12], pregunta[12:]]
# for fila in question:
#   for emoji in fila:
#     emoji = emoji.replace("'", '')
print(pregunta)
# question = question.replace(' ','')
# print(question)
# question = list(question.split(','))
# print(type(question))
# print('ahora es como lista:\n', question)
# for fila in question:
#   fila = fila.replace('[','')
#   fila = fila.replace(']','')
# print('\n\n\n',question)