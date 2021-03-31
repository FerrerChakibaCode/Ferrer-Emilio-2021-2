import requests
import random
from Player import *
import juegos

api = requests.get("https://api-escapamet.vercel.app/")


def check_character(word):
  for c in word:
    if c.isalpha():
      return True

def check_number(word):
  for c in word:
    if c.isnumeric():
      return True

def crear_usuario(username):

  avatars = ['Scharifker', 'Eugenio Mendoza', 'Pelusa', 'Gandhi', 'Maradona', 'Tostadora marca Oster']

  while " " in username or (not check_character(username)):
    username = input('Ingrese su nombre de usuario, únicamente caracteres y números')

  while True:
    try:
      password = input('Creando nuevo usuario, ingrese por favor su contraseña: ')
      if len(password) < 8 or (not check_character(password)) or (not check_number(password)):
        raise Exception
      break
    except:
      print('Ingrese una contraseña con mínimo 8 caracteres, 1 letra y 1 número')

  while True:
    try:
      age = int(input('Ingrese su edad, solo disponible para mayores de edad: '))
      if age < 18:
        raise Exception
      break
    except:
      print('Edad inválida...')
  
  for i, ava in enumerate(avatars):
    print(f"{i+1}. {ava}")
  avatar_sel = input('Seleccione el número correspondiente al avatar que desea escoger: ')
  avatar_sel = int(avatar_sel)

  for i, ava in enumerate(avatars):
    if avatar_sel == i+1:
      avatar = ava

  return username, password, age, avatar

def crear_partida(): #TODO averiguar cómo hacer lo del tiempo
  difficulty = input('''Seleccione una dificultad para jugar:
  1. Easy Peasy, Lemon Squeezy: 5 vidas | 5 pistas | Tiempo: 5 minutos
  2. Memedium: 3 vidas | 3 pistas | Tiempo: 3 minutos
  3. Hard, hard, lemon hard: 1 vida | 2 pistas | Tiempo: 1 minuto''')
  while int(difficulty) not in range (1,4):
    difficulty = input('Ingrese una dificultad válida, por favor: ')
  
  if int(difficulty) == 1:
    lives = 5.0
    clues = 5

  elif int(difficulty) == 2:
    lives = 3.0
    clues = 3
  
  elif int(difficulty) == 3:
    lives = 1.0
    clues = 2

  return lives, clues
  #TODO RECORDAR RECORD E INVENTARIO

def main():
  emilio = Player('emiferrer', 'az0909az', 19, 'Tostadora marca Oster', 5, 5, ['contraseña'])
  users_db = [emilio]
  # narrativa_1 = f"Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {tiempo_según_dificultad} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?"
  # narrativa_2 = f"Bienvenido {nombre_avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto."
  # narrativa_3 = f"¡Felicidades! Has logrado evitar una catástrofe en la Unimet, entonces... (Se deja libre al estudiante continuar con el desenlace del final a nivel narrativo)."

  main_menu_opcion = input(f'''Bienvenido a Escapemet! El Escape room más difícil de toda la Unimet...
  Qué quieres hacer?
  1- Crear una partida...
  2- Ver las instrucciones del juego...
  3- Highscores!!
  ''')

  if main_menu_opcion == '1':
    username = input('Ingrese su username: ') # TODO REVISAR QUE YA EXISTA EL USERNAME, CREAR UNA DB
    for user in users_db:
      if username in user[0]:
        crear_partida(username) #TODO 
    else:
      username, password, age, avatar = crear_usuario(username)
      lives, clues = crear_partida()
      player = Player(username, password, age, avatar, lives, clues) 

  juegos.lab_left(player)
  #juegos.lab_left(player)

if __name__ == '__main__':
  main()

#TODO ver los juegos...
#TODO arreglar que revise la base de datos de players + si ya el player está creado que no se vuelva puré el main
#TODO base de datos de los players
#TODO guardar records y todo en el .txt
#TODO Condicionales y dirección hacia donde se mueve la persona, ver el video de nuevo
#TODO Gráficas
#TODO meterle los textos a las gráficas directamente + eliminarlos de las funciones en juegos