import requests
import Player
import random
import sympy

api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, 600, ['contraseña', 'llave'])

user_answer = 0
x = sympy.Symbol('x')
funcion_api = api.json()[1]["objects"][1]["game"]["questions"][2]["question"]
f = funcion_api.split('f(x)=')
f = (f[-1]).replace(' ', '')
f = sympy.parse_expr(f)
print(f, type(f))
derivada_f = f.diff(x)
#print(derivada_f.evalf(60, subs = {x: 60}))


def f(x,y):
  return sen(x)/5 - tan(x)