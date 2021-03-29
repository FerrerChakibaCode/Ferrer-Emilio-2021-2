import requests
import random

api = requests.get("https://api-escapamet.vercel.app/")

# Preguntas sobre Python
def lab_left(cable_hdmi = False, jugador):
  if cable_hdmi:
    print(f'REGLAS DEL JUEGO -> {api.json()[0]["objects"][1]["game"]["rules"]}.\n')
    
    n = random.randint(0,1)
    
    if n == 0:
      
      pistas = [api.json()[0]["objects"][1]["game"]["questions"][n]["clue_1"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_2"], api.json()[0]["objects"][1]["game"]["questions"][n]["clue_3"]]
      print(api.json()[0]["objects"][1]["game"]["questions"][n]["question"])
      # str = "tengo en mi cuenta 50,00 $"
      # str = str.split()
      # str = [int(str[i]) for i in range(len(str)) if (str[i].replace(",",".")).isnumeric()]
      user_answer = input("Seleccione 'p' si desea una pista. Si no quiere una pista, escriba su respuesta.\n").lower()
      while USER.PISTAS != 0:
        if user_answer == 'p': #TODO VALIDACIÓN DE LA CANTIDAD DE PISTAS QUE LE QUEDAN AL USER
          print(pistas[0])
          pistas.pop(0)
          print(f"\nLe quedan USER.PISTAS cantidad de pistas, si desea otra pista, seleccione 'p'") # TODO PISTAS DEL USUARIO
      


        
  
  else:
    print(api.json()[0]["objects"][1]["game"]["message_requirement"])

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
  avatar = input('Seleccione el número correspondiente al avatar que desea escoger: ')

  for i, avatar in enumerate(avatars):
    if int(avatar) == i+1
    avatar = ava

  return username, password, age, avatar

def crear_partida(username):
  pass  

# TODO CREAR OBJETO DEL JUGADOR DEPENDIENDO DE DIFICULTAD, CANTIDAD DE VIDAS Y PISTAS, + TIEMPO PARA JUGAR
def main():

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
    if username in users_db["username"]:
      crear_partida(username)
    else:
      crear_partida(crear_usuario(usuario))
  lab_left(True)


if __name__ == '__main__':
  main()