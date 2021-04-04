import requests
import Player
import random
from sympy import diff, Symbol
from sympy.parsing.sympy_parser import parse_expr

api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, 600, ['contraseña', 'llave'])

# user_answer = 0
# x = sympy.Symbol('x')

# f = sympy.parse_expr(f)
# print(f, type(f))
# derivada_f = f.diff(x)
# print(derivada_f.evalf(60, subs = {x: 60}))

funcion_api = api.json()[1]["objects"][1]["game"]["questions"][2]["question"]

f = funcion_api.split('f(x)=')
f = f[-1].replace(' ', '')
f = f.replace('sen', 'sin')
symbols = {'x': Symbol('x', real = True)}
f = parse_expr(f, symbols)
# print(diff(f, symbols['x']))

derivada_en_x = diff(f, symbols['x'])
print(derivada_en_x)

derivada_en_pi3 = derivada_en_x.subs(x, 5)
print(derivada_en_x(5))