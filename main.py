import enquiries
import Adivinanza
import Ahorcado
import Criptograma
import Game
import graficos
import LogicaResuelve
import MemoriaEmoji
import Player
import PreguntasPython
import PreguntasMatematicas
import Quizizz

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
  difficulties = ['Easy Peasy, Lemon Squeezy: 5 vidas | 5 pistas | Tiempo: 5 minutos', 'Memedium: 3 vidas | 3 pistas | Tiempo: 3 minutos', 'Hard, hard, lemon hard: 1 vida | 2 pistas | Tiempo: 1 minuto']
  difficulty = enquiries.choose('Seleccione la dificultad en la quiere jugar.', difficulties)
      
  if difficulty == difficulties[0]:
    lives = 5.0
    clues = 5
    time = 600
    difficulty = 'Easy'

  elif difficulty == difficulties[1]:
    lives = 3.0
    clues = 3
    time = 300
    difficulty = 'Medium'
  
  elif difficulty == difficulties[2]:
    lives = 1.0
    clues = 2
    time = 250
    difficulty = 'Hard'

  return difficulty, lives, clues, time

def start(users_db):
  username = input('Ingrese su username: ')
  while len(username) < 3 or len(username) > 20:
    username = input('Ingrese su username: ')
  if (len(users_db)) > 0:
    for x in range(len(users_db)):
      if username == users_db[x].username:
        player = users_db[x]
        password = input('Bienvenido de vuelta. Ingresa tu clave\n> ')
        while password != player.password:
          password = input('Clave incorrecta\n> ')
        if password == player.password:
          difficulty, lives, clues, time = selec_dificultad()
          player.difficulty = difficulty
          player.lives = lives
          player.clues = clues
          player.time = time
          return player

  else:
    username, password, age, avatar = datos_basicos_usuario(username)
    difficulty, lives, clues, time = selec_dificultad()
    player = Player(username, password, age, avatar, lives, clues, time) 
    users_db.append(player)
    return player

def start_game(player):
  while True:
    #BIBLIOTECA
    room = 1
    print(graficos.library)
    
    movimientos = ['Ir hacia la PLAZA DEL RECTORADO', 'Ir hacia el PASILLO DE LABORATORIOS'] # Hacia dónde se puede mover
    objetos = ['Mueble de sentarse', 'Mueble de libros', 'Mueble con gabetas'] # Objetos que puede elegir
    
    accion_choices = ['Inspeccionar objeto', 'Salir de la biblioteca'] # Acciones que puede hacer
    accion = enquiries.choose('', accion_choices) # Elige qué acción hacer
    
    if accion == 'Inspeccionar objeto': # Si elige ver objetos
      objeto_choice = enquiries.choose('', objetos) # Elige el objeto
      
      if objeto_choice == 'Mueble de sentarse':
        objeto = 1
        preguntar = PreguntasMatematicas.PreguntasMatematicas(room, objeto) # PreguntasMatematicas
        preguntar.jugar(player) # Jugar Preguntas Matemáticas
        print('llegue hasta aca')
      
      elif objeto_choice == 'Mueble de libros':
        objeto = 0
        ahorcar = Ahorcado.Ahorcado(room, objeto) # Ahorcado
        ahorcar.jugar(player) # Jugar al Ahorcado
      
      elif objeto_choice == 'Mueble con gabetas':
        objeto = 2
        cifrado_cesar = Criptograma.Criptograma(room, objeto) # Criptograma
        cifrado_cesar.jugar(player) # Jugar al Criptograma

    else: # Si elige salir de la BIBLIOTECA
      desplazamiento = enquiries.choose('', movimientos)
      
      if desplazamiento == 'Ir hacia la PLAZA DEL RECTORADO':
        # PLAZA DEL RECTORADO
        while True:
          room = 2
          print(graficos.plaza_rectorado)
          
          movimientos = ['Ir hacia la BIBLIOTECA'] # Hacia dónde se puede mover
          objetos = ['Banco 1', 'Samán', 'Banco 2'] # Objetos que puede elegir
          
          accion_choices = ['Inspeccionar objeto', 'Salir de la plaza del rectorado'] # Acciones que puede hacer
          accion = enquiries.choose('', accion_choices) # Elige qué acción hacer
          
          if accion == 'Inspeccionar objeto':
            objecto_choice = enquiries.choose('', objetos)
            
            if objecto_choice == 'Banco 1':
              objeto = 1
              quizizz = Quizizz.Quizizz(room, objeto) # Quizizz
              quizizz.jugar(player) # Jugar a Quizizz
            
            elif objecto_choice == 'Samán':
              objeto = 0
              logresuelve = LogicaResuelve.LogicaResuelve(room, objeto) # Lógica y resuelve
              logresuelve.jugar(player) # Jugar a Lógica y resuelve

            elif objecto_choice == 'Banco 2':
              objeto = 2
              memojis = MemoriaEmoji.MemoriaEmoji(room, objeto) # Memoria emoji
              memojis.jugar(player) # Jugar a Memoria emoji
          
          elif accion == 'Salir de la plaza del rectorado':
            desplazamiento = enquiries.choose('', movimientos)
            if desplazamiento == 'Ir hacia la BIBLIOTECA':
              break

          elif accion == 'Salir de la plaza del rectorado':
            pass
      else: # Elige ir a PASILLO LABORATORIOS
        pass


  



def main():
  
  while True:
    emilio = Player.Player('ferrer', 'az0909az', 19, 'Maradona', 'Easy', 5, 5, 600, ["llave", "libro de matemáticas"])
    users_db = [emilio]
    print('Bienvenido a Escapemet! El Escape room más difícil de jugar y de programar, en toda la Unimet...', graficos.small_spaces)
    main_menu_opciones = ['Crear una partida', 'Ver las instrucciones del juego', 'Estadísticas de jugadores']
    main_menu_opcion = enquiries.choose('', main_menu_opciones)

    if main_menu_opcion == main_menu_opciones[0]: # Crear partida
      player = start(users_db)
      time_minutos = divmod(player.time, 60)
      print(graficos.spaces, f"Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {time_minutos} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?", graficos.small_spaces)
      start_choice = enquiries.choose('',['Sí, claro.', 'No, soy una gallina.'])
      if start_choice == 'Sí, claro.': # Comienza el juego
      # Narrativa 2
        print(f"Bienvenido {player.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.") 
        start_game(player)
    elif main_menu_opcion == main_menu_opciones[1]: # Ver instrucciones del juego
      print('Instrucciones')
    
    elif main_menu_opcion == main_menu_opciones[2]:
      print('Highscores')

    else: # Si no elige una opción válida
      print(f'{graficos.good_bye}')
      break

    

    # lista_usuarios = [player.show for user in users_db]
    # print(f'USUARIOS: {lista_usuarios}')

main()

#TODO Eval para el de Pregunta Python
#TODO regalar una vida si decide leer un libro en la biblioteca
#TODO stay in the loop
#TODO guardar records y todo en el .txt
#TODO Condicionales y dirección hacia donde se mueve la persona, ver el video de nuevo
#TODO Gráficas
#TODO meterle los textos a las gráficas directamente + eliminarlos de las funciones en juegos
#TODO comentar todo el código
#TODO DIAGRAMA DE CLASES