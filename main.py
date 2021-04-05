import Adivinanza
import Ahorcado
import Criptograma
import enquiries
import EscogeNumero
import FinalBoss
import Game
import graficos
import json
import LogicaBooleana
import LogicaResuelve
import MemoriaEmoji
import PalabraMezclada
import Player
import PreguntasPython
import PreguntasMatematicas
import requests
import SopaLetras
import time
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
  
  avatar = enquiries.choose('ELija su avatar', avatars)

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
  if username in users_db:
    data_player = users_db[f'{username}']
    password = input('Bienvenido de vuelta. Ingresa tu clave\n> ')
    while password != player[1]:
      password = input('Clave incorrecta\n> ')

    difficulty, lives, clues, time = selec_dificultad()
    player = Player.Player(username = data_player[0], password = data_player[1], age = data_player[2], avatar = data_player[3], difficulty = difficulty, lives = lives, clues = clues, time = time, record = data_player[-1], inventory = [])
    return player


  else:
    username, password, age, avatar = datos_basicos_usuario(username)
    difficulty, lives, clues, time = selec_dificultad()
    player = Player.Player(username = username, password = password, age = age, avatar = avatar, difficulty = difficulty, lives = lives, clues = clues, time = time, inventory = [], record = [0, 0, 0]) 
    
    return player

# define the countdown func.
def countdown(t, player):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds

  
# function call

def record_to_json(player, users_db):
  users_db[f'{player.username}'] = [player.username, player.password, player.age, player.avatar, player.record]


  filename_conext = './users_db.json'
  with open(filename_conext, 'w') as fp:
    json.dump(users_db, fp)

def start_game(player, users_db):
  continuar = True
  while player.lives > 0 and continuar:
    # t = player.time
    # countdown(t, player)
    #BIBLIOTECA
    # first_time = time.perf_counter()
    boss = FinalBoss.FinalBoss(4,0)
    boss.jugar(player)
    room = 1
    print(graficos.small_spaces, graficos.library)
    
    movimientos = ['Ir hacia atrás, la PLAZA DEL RECTORADO', 'Ir hacia la derecha, el PASILLO DE LABORATORIOS', 'Cancelar'] # Hacia dónde se puede mover
    objetos = ['Mueble de sentarse', 'Mueble de libros', 'Mueble con gabetas', 'Cancelar'] # Objetos que puede elegir
    
    accion_choices = ['Inspeccionar objeto', 'Salir de la biblioteca'] # Acciones que puede hacer
    accion = enquiries.choose('', accion_choices) # Elige qué acción hacer
    
    if accion == 'Inspeccionar objeto': # Si elige ver objetos
      objeto_choice = enquiries.choose('', objetos) # Elige el objeto
      
      if objeto_choice == 'Mueble de sentarse':
        objeto = 1
        preguntar = PreguntasMatematicas.PreguntasMatematicas(room, objeto) # PreguntasMatematicas
        preguntar.jugar(player) # Jugar Preguntas Matemáticas
      
      elif objeto_choice == 'Mueble de libros':
        objeto = 0
        ahorcar = Ahorcado.Ahorcado(room, objeto) # Ahorcado
        ahorcar.jugar(player) # Jugar al Ahorcado
        # time_2 = time.perf_counter()
        print(f'Te tardaste: {time_2-first_time} segundos')
      
      elif objeto_choice == 'Mueble con gabetas':
        objeto = 2
        cifrado_cesar = Criptograma.Criptograma(room, objeto) # Criptograma
        cifrado_cesar.jugar(player) # Jugar al Criptograma


    elif accion == 'Salir de la biblioteca': # Si elige salir de la BIBLIOTECA
      desplazamiento = enquiries.choose('', movimientos)
      
      if desplazamiento == 'Ir hacia atrás, la PLAZA DEL RECTORADO':
        # PLAZA DEL RECTORADO
        while player.lives > 0 and continuar:
          room = 2
          print(graficos.small_spaces, graficos.plaza_rectorado)
          
          movimientos = ['Ir hacia la izquierda, BIBLIOTECA', 'Cancelar'] # Hacia dónde se puede mover
          objetos = ['Banco 1', 'Samán', 'Banco 2', 'Cancelar'] # Objetos que puede elegir
          
          accion_choices = ['Inspeccionar objeto', 'Salir de la plaza del rectorado'] # Acciones que puede hacer
          accion = enquiries.choose('', accion_choices) # Elige qué acción hacer
          
          if accion == 'Inspeccionar objeto': # Si elige ver objetos
            objeto_choice = enquiries.choose('', objetos)  # Elige el objeto
            
            if objeto_choice == 'Banco 1':
              objeto = 1
              quizizz = Quizizz.Quizizz(room, objeto) # Quizizz
              quizizz.jugar(player) # Jugar a Quizizz
            
            elif objeto_choice == 'Samán':
              objeto = 0
              logresuelve = LogicaResuelve.LogicaResuelve(room, objeto) # Lógica y resuelve
              logresuelve.jugar(player) # Jugar a Lógica y resuelve

            elif objeto_choice == 'Banco 2':
              objeto = 2
              memojis = MemoriaEmoji.MemoriaEmoji(room, objeto) # Memoria emoji
              memojis.jugar(player) # Jugar a Memoria emoji
          
          elif accion == 'Salir de la plaza del rectorado':
            desplazamiento = enquiries.choose('', movimientos)
            if desplazamiento == 'Ir hacia la izquierda, BIBLIOTECA':
              break

      elif desplazamiento == 'Ir hacia la derecha, el PASILLO DE LABORATORIOS': # Elige ir a PASILLO LABORATORIOS
        # PASILLO DE LABORATORIOS
        while player.lives > 0 and continuar:
          room = 3
          print(graficos.small_spaces, graficos.pasillo_laboratorios)

          movimientos = ['Ir hacia la derecha, LABORATORIOS SL001', 'Ir hacia la izquierda, BIBLIOTECA', 'Cancelar'] # Hacia dónde se puede mover
          objetos = ['Puerta', 'Cancelar']  # Objetos que puede elegir
          
          accion_choices = ['Inspeccionar objeto', 'Salir del pasillo de laboratorios']  # Acciones que puede hacer
          accion = enquiries.choose('', accion_choices)  # Elige qué acción hacer
    
          if accion == 'Inspeccionar objeto': # Si elige ver objetos
            objeto_choice = enquiries.choose('', objetos) # Elige el objeto

            if objeto_choice == 'Puerta':
              objeto = 0
              logbooleana = LogicaBooleana.LogicaBooleana(room, objeto) # Lógica booleana
              logbooleana.jugar(player) # Jugar lógica booleana
            
          elif accion == 'Salir del pasillo de laboratorios': # SI elige salir del pasillo de laboratorios
            desplazamiento = enquiries.choose('', movimientos)

            if desplazamiento == 'Ir hacia la izquierda, BIBLIOTECA':
              break #Rompe el While del PASILLO, lo que lo deja en BIBLIOTECA de nuevo

            elif desplazamiento == 'Ir hacia la derecha, LABORATORIOS SL001':
              #LABORATORIOS SL001
              while player.lives > 0 and continuar:
                room = 0
                print(graficos.laboratorios_sl001)

                movimientos = ['Ir hacia la derecha, SERVIDORES', 'Ir hacia la izquierda, PASILLO DE LABORATORIOS', 'Cancelar']
                objetos = ['PC 1', 'Pizarra', 'PC 2', 'Cancelar']

                accion_choices = ['Inspeccionar objeto', 'Salir de los LABORATORIOS SL001']  # Acciones que puede hacer
                accion = enquiries.choose('', accion_choices)  # Elige qué acción hacer

                if accion == 'Inspeccionar objeto':
                  objeto_choice = enquiries.choose('', objetos)

                  if objeto_choice == 'PC 1': # Si elige la izquierda
                    objeto = 1
                    pypreg = PreguntasPython.PreguntasPython(room, objeto) # Preguntas sobre python
                    pypreg.jugar(player) # Jugar Preguntas sobre python
                  
                  elif objeto_choice == 'Pizarra': # Si elige el centro
                    objeto = 0
                    sopa = SopaLetras.SopaLetras(room, objeto)
                    sopa.llenar_matriz()
                    sopa.jugar(player)
                    

                  elif objeto_choice == 'PC 2': # Si elige la derecha
                    objeto = 2
                    adivinar = Adivinanza.Adivinanza(room, objeto) # Adivinanzas
                    adivinar.jugar(player) # Jugar Adivinanzas
                
                elif accion == 'Salir de los LABORATORIOS SL001':
                  desplazamiento = enquiries.choose('', movimientos)
                  
                  if desplazamiento == 'Ir hacia la izquierda, PASILLO DE LABORATORIOS':
                    break # Rompe el While de Laboratorio, para volver al pasillo de laboratorios
                  
                  elif desplazamiento == 'Ir hacia la derecha, SERVIDORES':
                    # SERVIDORES
                    while player.lives > 0 and continuar:
                      room = 4
                      print(graficos.small_spaces, graficos.cuarto_servidores)

                      movimientos = ['Ir hacia la izquierda, LABORATORIOS SL001', 'Cancelar']
                      objetos = ['Papelera', 'Puerta', 'Rack']

                      accion_choices = ['Inspeccionar objeto', 'Salir del CUARTO DE SERVIDORES']  # Acciones que puede hacer
                      accion = enquiries.choose('', accion_choices)  # Elige qué acción hacer

                      if accion == 'Inspeccionar objeto':
                        objeto_choice = enquiries.choose('', objetos)

                        if objeto_choice == 'Papelera':
                          objeto = 2
                          escoge = EscogeNumero.EscogeNumero(room, objeto) # Escoge un número entre
                          escoge.jugar(player) # Jugar Escoge un número entre

                        elif objeto_choice == 'Puerta':
                          objeto = 0
                          # finalboss = FinalBoss.FinalBoss(room, objeto) FINAL EN CONSTRUCCIÓN
                          # finalboss.jugar(player) FINAL EN CONSTRUCCIÓN
                          if api.json()[4]["objects"][0]["game"]["requirement"][0] in player.inventory and api.json()[4]["objects"][0]["game"]["requirement"][1]:
                            print('FELICIDADES, GANASTE!')
                            if player.difficulty == 'Easy':
                              player.record[0] += 1
                            elif player.difficulty == 'Medium':
                              player.record[1] += 1
                            elif player.difficulty == 'Hard':
                              player.record[2] += 1
                            users_db[f'{player.username}'] = [player.username, player.password, player.age, player.avatar, player.record] # Guardar variables del player que nos interesan en el Users_DB
                            record_to_json(player, users_db) # Guardar Users_DB diccionario al JSON
                          
                          # if finalboss.award in player.inventory:
                          #   print('FELICIDADES, GANASTE!')
                            
                          #   if player.difficulty == 'Easy':
                          #     player.record[0] += 1
                          #     users_db[f'{player.username}'] = [player.username, player.password, player.age, player.avatar, player.record]
                          #     record_to_json(player, users_db)
                              

                          #   elif player.difficulty == 'Medium':
                          #     player.record[1] += 1
                          #     users_db[f'{player.username}'] = [player.username, player.password, player.age, player.avatar, player.record]
                          #     record_to_json(player, users_db)

                          #   elif player.difficulty == 'Hard':
                          #     player.record[-1] += 1
                          #     users_db[f'{player.username}'] = [player.username, player.password, player.age, player.avatar, player.record]
                          #     record_to_json(player, users_db)
                          continuar = False

                          # else:
                          #   print(graficos.small_spaces, graficos.good_bye, graficos.small_spaces)

                        elif objeto_choice == 'Rack':
                          objeto = 1
                          palabramezcla = PalabraMezclada.PalabraMezclada(room, objeto) # Palabra mezclada
                          palabramezcla.jugar(player) # Jugar Palabra mezclada

                      elif accion == 'Salir del CUARTO DE SERVIDORES':
                        desplazamiento = enquiries.choose('', movimientos)
                        if desplazamiento == 'Ir hacia la izquierda, LABORATORIOS SL001':
                          break # Rompe el While de Servidores, para volver al pasillo

def main():
  
  while True:
    users_db = json.load(open('users_db.json'))
    print(users_db)
    print(graficos.small_spaces,graficos.escape_met_title, graficos.small_spaces)
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
        start_game(player, users_db)
    elif main_menu_opcion == main_menu_opciones[1]: # Ver instrucciones del juego
      print('Instrucciones')
    
    elif main_menu_opcion == main_menu_opciones[2]:
      print('Highscores')

    else: # Si no elige una opción válida
      print(f'{graficos.good_bye}')
      break


main()
#TODO revisar sopa de letras
#TODO tiempo
#TODO programar cuando le gana al boss
#TODO guardar records y todo en el .txt
#TODO Estadísticas
#TODO Reglas del juego para el menú principal
#TODO comentar todo el código
#TODO DIAGRAMA DE CLASES