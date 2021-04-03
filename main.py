import requests
import random
from Player import *
import juegos
import Adivinanza
import PreguntasPython
import Ahorcado
import Criptograma
import graficos
import enquiries

api = requests.get("https://api-escapamet.vercel.app/")

# narrativa_1 = f"Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {(player.time)/60} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?"
# narrativa_2 = f"Bienvenido {player.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto."
# narrativa_final = "¡Felicidades! Has logrado evitar una catástrofe en la Unimet, entonces... (Se deja libre al estudiante continuar con el desenlace del final a nivel narrativo).  "

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
  while True:
    try:
      difficulty = int(input('''Seleccione una dificultad para jugar:
      1. Easy Peasy, Lemon Squeezy: 5 vidas | 5 pistas | Tiempo: 5 minutos
      2. Memedium: 3 vidas | 3 pistas | Tiempo: 3 minutos
      3. Hard, hard, lemon hard: 1 vida | 2 pistas | Tiempo: 1 minuto
      > '''))
      if difficulty not in range(1,4):
        raise Exception
      break
    
    except:
      print('Ingrese un valor entre 1 y 3, por favor.')
      
  if difficulty == 1:
    lives = 5.0
    clues = 5
    time = 600

  elif difficulty == 2:
    lives = 3.0
    clues = 3
    time = 300
  
  elif difficulty == 3:
    lives = 1.0
    clues = 2
    time = 250

  return lives, clues, time

def start(users_db):
  username = input('Ingrese su username: ') # TODO REVISAR QUE YA EXISTA EL USERNAME, CREAR UNA DB
  if (len(users_db)) > 0:
    for x in range(len(users_db)):
      if username == users_db[x].username:
        player = users_db[x]
        password = input('Ingresa tu clave para validar que seas tú\n> ')
        if password == player.password:
          lives, clues, time = selec_dificultad()
          player.lives = lives
          player.clues = clues
          player.time = time
          return player

  else:
    username, password, age, avatar = datos_basicos_usuario(username)
    lives, clues, time = selec_dificultad()
    player = Player(username, password, age, avatar, lives, clues, time) 
    users_db.append(player)
    return player

def main():
  
  while True:
    emilio = Player('ferrer', 'az0909az', 19, 'Maradona', 5, 5, 600, ["llave"])
    users_db = [emilio]
    
    main_menu_opcion = input(f'''Bienvenido a Escapemet! El Escape room más difícil de jugar y de programar, en toda la Unimet...
    Qué quieres hacer?
    1- Crear una partida...
    2- Ver las instrucciones del juego...
    3- Highscores!!
    ''')

    if main_menu_opcion == '1':
      player = start(users_db)
      time_minutos = divmod(player.time, 60)
      print(graficos.spaces, f"Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {time_minutos} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?", graficos.small_spaces)
      start_choice = enquiries.choose('',['Sí, claro.', 'No, soy una gallina.'])
      if start_choice == 'Sí, claro.':
        cesar_salad = Criptograma.Criptograma(1, 2)
        cesar_salad.jugar(player)

        # ahorcado = Ahorcado.Ahorcado(1,0)
        
        # ahorcado.jugar(player)
        
        # preguntas = PreguntasPython.PreguntasPython(0,1)
        # if preguntas.requirement in player.inventory:
        #   user_answer = input('> ')
        #   preguntas.jugar(user_answer, player) #PROGRAMAR LOS CAMINOS AQUÍ
        # else:
        #   print(preguntas.message_requirement)
      else:
        print(f'{graficos.good_bye}')
        break
    

    elif main_menu_opcion not in range(1,4):
      print(f'{graficos.good_bye}')
      break

    

    # lista_usuarios = [player.show for user in users_db]
    # print(f'USUARIOS: {lista_usuarios}')

main()

#TODO regalar una vida si decide leer un libro en la biblioteca
#TODO stay in the loop
#TODO guardar records y todo en el .txt
#TODO Condicionales y dirección hacia donde se mueve la persona, ver el video de nuevo
#TODO Gráficas
#TODO meterle los textos a las gráficas directamente + eliminarlos de las funciones en juegos
#TODO poner los requirements directos desde la API (en los juegos) y no escritos, excepto el de la clave de la Computadora
#TODO comentar todo el código
#TODO DIAGRAMA DE CLASES