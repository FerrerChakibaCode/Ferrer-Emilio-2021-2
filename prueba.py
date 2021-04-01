import requests
import Player
import random
api = requests.get("https://api-escapamet.vercel.app/")
emilio = Player.Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña'])

n = (0,(len(api.json()[1]["objects"][1]["game"]["questions"]))-1)
print(questions)