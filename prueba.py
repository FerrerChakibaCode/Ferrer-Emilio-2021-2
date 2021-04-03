import requests
import Player
import random
import sympy

api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, 600, ['contraseña', 'llave'])

lista = ['e', 'm', 'i']

list_a_str = ''.join(map(str, lista))
print(list_a_str)
#library_right(emilio) 