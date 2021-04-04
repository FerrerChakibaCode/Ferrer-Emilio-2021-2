import requests
import Player
import random
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr

api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 'Easy', 5, 5, 600, ['contraseña'])

funcion_api = api.json()[1]["objects"][1]["game"]["questions"][2]["question"]

f = funcion_api.split('f(x)=') #Tomamos la función del api y la dividimos para tomar la función en sí
x = (f[0].split())[-1] # Antes de seguir modificando la variable 'f', tomamos nuestra X
f = f[-1].replace(' ', '')
f = f.replace('sen', 'sin')
symbols = {'x': Symbol('x', real = True)}
x = parse_expr(x, symbols) # Convertimos a X en type que acepte Sympy
print(type(x))
f = parse_expr(f, symbols)
# print(diff(f, symbols['x']))

derivada_f = diff(f, symbols['x'])
print(derivada_f)

evaluar_derivada_en_x = derivada_f.evalf(subs = {symbols['x']: x})
evaluar_derivada_en_x = round(evaluar_derivada_en_x, 2)
print(evaluar_derivada_en_x)