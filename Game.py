import requests

api = requests.get("https://api-escapamet.vercel.app/") # Guardar la API en una variable 'api'

class Game:
  def __init__(self, room, objeto): # Las preguntas y las pistas pasarlas en la clase heredada
     # PARA SABER: Room = api.json()[room], Objeto = api.json()[room]["objects"][objeto]
    self.room = api.json()[room]
    self.objeto = api.json()[room]["objects"][objeto]
  
  def show(self):
    return(f"| Cuarto: {self.room} | Objeto: {self.objeto} |")

