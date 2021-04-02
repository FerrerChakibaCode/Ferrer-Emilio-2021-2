import requests
import random
from Player import *
import juegos
import Adivinanza

api = requests.get("https://api-escapamet.vercel.app/")


def check_character(word):
  for c in word:
    if c.isalpha():
      return True

def check_number(word):
  for c in word:
    if c.isnumeric():
      return True

def datos_basicos_usuario(username):

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

def selec_dificultad():
  difficulty = input('''Seleccione una dificultad para jugar:
  1. Easy Peasy, Lemon Squeezy: 5 vidas | 5 pistas | Tiempo: 5 minutos
  2. Memedium: 3 vidas | 3 pistas | Tiempo: 3 minutos
  3. Hard, hard, lemon hard: 1 vida | 2 pistas | Tiempo: 1 minuto
  > ''')
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

def main():
  while True:
    emilio = Player('emilioferrer', 'az0909az', 19, 'Maradona', 5, 5, [])
    users_db = [emilio]
    
    main_menu_opcion = input(f'''Bienvenido a Escapemet! El Escape room más difícil de jugar y de programar, en toda la Unimet...
    Qué quieres hacer?
    1- Crear una partida...
    2- Ver las instrucciones del juego...
    3- Highscores!!
    ''')

    if main_menu_opcion == '1':
      username = input('Ingrese su username: ') # TODO REVISAR QUE YA EXISTA EL USERNAME, CREAR UNA DB
      for x in range(len(users_db)):
        if username == users_db[x].username:
          
          player = users_db[x]
          password = input('Ingresa tu clave para validar que seas tú\n> ')
          if password == player.password:
            lives, clues = selec_dificultad()
            player.lives = lives
            player.clues = clues
            break
      else:
        username, password, age, avatar = datos_basicos_usuario(username)
        lives, clues = selec_dificultad()
        player = Player(username, password, age, avatar, lives, clues) 
        users_db.append(player)
      #juegos.library_center(player)
    #juegos.lab_left(player)

    elif main_menu_opcion not in range(1,4):
      print('Goodbye moonman...\n')
      break

    Adivinanza.Adivinanza(api.json()[0], api.json()[0]["objects"][2], api.json()[0]["objects"]["game"]["name"], api.json()[0]["objects"]["game"]["requirement"], api.json()[0]["objects"]["game"]["award"], api.json()[0]["objects"]["game"]["rules"])

    # lista_usuarios = [player.show for user in users_db]
    # print(f'USUARIOS: {lista_usuarios}')

main()
#Preguntas para algún preparador: SOBRE EL DEL FORMATO DE 50$, sobre quiénes deberían ser objetos, sobre el juego de preguntas matemáticas
#TODO ver los juegos...
#TODO mostrar lista de usuarios
#TODO guardar records y todo en el .txt
#TODO Condicionales y dirección hacia donde se mueve la persona, ver el video de nuevo
#TODO Gráficas
#TODO meterle los textos a las gráficas directamente + eliminarlos de las funciones en juegos
#TODO Herencia, intentar poner a los Cuartos como objetos y a los Objetos como Subclases de los Cuartos
#TODO revisar que no sea rompible el juego si los profesores decidiesen meterle más o menos RESPUESTAS, las preguntas están cool
#TODO poner los requirements directos desde la API (en los juegos) y no escritos, excepto el de la clave de la Computadora
#TODO DIAGRAMA DE CLASES